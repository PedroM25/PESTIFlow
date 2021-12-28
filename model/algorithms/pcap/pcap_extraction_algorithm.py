from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.inet6 import IPv6

from model.algorithms.uni_extraction_algorithm import UniExtractionAlgorithm
from model.bi_features_interface import BiFeaturesInterface
from model.factories.flow_key_factory import FlowKeyFactory
from model.read_analyze_output import ReadAnalyzeOutput
from model.services.io_service import IOService
from model.uni_features_interface import UniFeaturesInterface
from model.services import io_service


class PcapExtractionAlgorithm(UniExtractionAlgorithm):

    def _calculate_packet_flow_key(self, packet):
        packet_flow_key = FlowKeyFactory().create_flow_key(self)

        # Step 1 - Find the 5 tuple of the packet
        if IP in packet:
            packet_flow_key.src_ip = packet[IP].src
            packet_flow_key.dst_ip = packet[IP].dst
            packet_flow_key.proto = str(packet[IP].proto)
        elif IPv6 in packet:
            packet_flow_key.src_ip = packet[IPv6].src
            packet_flow_key.dst_ip = packet[IPv6].dst
            packet_flow_key.proto = str(packet[IPv6].nh)
        else:
            return

        if TCP in packet or UDP in packet:
            packet_flow_key.src_port = str(packet[2].sport)
            packet_flow_key.dst_port = str(packet[2].dport)
        else:
            return

        return packet_flow_key

    def read_and_analyze_data_instances(self, input_path, timeout):

        ra_output = ReadAnalyzeOutput()
        flow_key_packets = {}
        # map containg a flow key as a key and a list of packets as values
        for current_packet in IOService().read_pcap(input_path):
            ra_output.n_read_data_instances += 1
            p_flow_key = self._calculate_packet_flow_key(current_packet)
            if p_flow_key is None:
                # Means that it is a packet with a non-IPv4, non-IPv6 L3 protocol or a non-TCP, non-UDP L4 protocol
                ra_output.n_invalid_instances += 1
                continue

            ra_output.n_valid_instances += 1

            # Flow ending condition #1 (time related)
            if p_flow_key in flow_key_packets:
                if current_packet.time - flow_key_packets[p_flow_key][-1].time < timeout:
                    flow_key_packets[p_flow_key].append(current_packet)
                else:
                    self.data_instances_per_flow.add_data_instance(flow_key_packets.pop(p_flow_key))
                    flow_key_packets[p_flow_key] = [current_packet]
            else:
                flow_key_packets[p_flow_key] = [current_packet]

            # Flow ending condition #2 (TCP exclusive)
            if TCP in current_packet:

                if issubclass(self.__class__, BiFeaturesInterface):
                    try:
                        last_packet = flow_key_packets[p_flow_key][-2]
                        before_last_packet = flow_key_packets[p_flow_key][-3]
                        if current_packet[TCP].flags.A and \
                                (last_packet[TCP].flags.A and last_packet[TCP].flags.F) and \
                                before_last_packet[TCP].flags.F:
                            self.data_instances_per_flow.add_data_instance(flow_key_packets.pop(p_flow_key))
                    except IndexError:
                        pass
                elif issubclass(self.__class__, UniFeaturesInterface):
                    try:
                        last_packet = flow_key_packets[p_flow_key][-2]
                        if current_packet[TCP].flags.A and last_packet[TCP].flags.F:
                            self.data_instances_per_flow.add_data_instance(flow_key_packets.pop(p_flow_key))
                    except IndexError:
                        pass
                    finally:
                        if current_packet[TCP].flags.F and current_packet[TCP].flags.A:
                            self.data_instances_per_flow.add_data_instance(flow_key_packets.pop(p_flow_key))

                if current_packet[TCP].flags.R:
                    self.data_instances_per_flow.add_data_instance(flow_key_packets.pop(p_flow_key))

        for p_flow_key in flow_key_packets:
            self.data_instances_per_flow.add_data_instance(flow_key_packets[p_flow_key])

        return ra_output
