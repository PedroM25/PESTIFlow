from datetime import datetime

from scapy.layers.inet import IP, TCP
from scapy.layers.inet6 import IPv6

import utilities
from model.algorithms.pcap.pcap_extraction_algorithm import PcapExtractionAlgorithm


class UniPcapExtractionAlgorithm(PcapExtractionAlgorithm):
    """ It is assumed that all the following methods are only executed if the cleanup() was executed before them.
    Hence, not verifications are performed such as if the packet contains IP, IPv6, TCP or UDP
    """

    def tot_l_fw_pkt(self, packets_of_flow):
        session_sender_ip = packets_of_flow[0][1].src

        ret = 0
        for packet in packets_of_flow:
            if packet[1].src == session_sender_ip:
                ret += len(packet)
        return ret

    def transport_proto(self, packets_of_flow):
        """The first packet is chosen to obtain this feature but any packet would serve."""
        first_packet = packets_of_flow[0]
        if IP in first_packet:
            return first_packet[IP].proto
        elif IPv6 in first_packet:
            return first_packet[IPv6].nh

    def tot_fw_pkt(self, packets_of_flow):
        session_sender_ip = packets_of_flow[0][1].src

        ret = 0
        for packet in packets_of_flow:
            if packet[1].src == session_sender_ip:
                ret += 1
        return ret

    def ts_beginning(self, packets_of_flow):
        return datetime.fromtimestamp(float(packets_of_flow[0].time))

    def s_tos(self, packets_of_flow):
        first_packet = packets_of_flow[0]
        if IP in first_packet:
            return first_packet[IP].tos
        elif IPv6 in first_packet:
            return utilities.NOT_AVAILABLE

    def tcp_flags_fw(self, packets_of_flow):
        # Right now returns in hex but can be changed to return in str like "ASU" where each letter is a flag
        session_sender_ip = packets_of_flow[0][1].src

        ret = 0
        for packet in packets_of_flow:
            if TCP in packet:
                if packet[1].src == session_sender_ip:
                    ret |= int(packet[TCP].flags)
            else:
                return utilities.NOT_AVAILABLE
                # In case the packet has UDP protocol
        return hex(ret)

    def ts_end(self, packets_of_flow):
        return datetime.fromtimestamp(float(packets_of_flow[-1].time))

    def fin_cnt(self, packets_of_flow):
        ret = 0
        for packet in packets_of_flow:
            if TCP in packet:
                if packet[TCP].flags.F:
                    ret += 1
            else:
                return utilities.NOT_AVAILABLE
                # In case the packet has UDP protocol
        return ret

    def syn_cnt(self, packets_of_flow):
        ret = 0
        for packet in packets_of_flow:
            if TCP in packet:
                if packet[TCP].flags.S:
                    ret += 1
            else:
                return utilities.NOT_AVAILABLE
                # In case the packet has UDP protocol
        return ret

    def rst_cnt(self, packets_of_flow):
        ret = 0
        for packet in packets_of_flow:
            if TCP in packet:
                if packet[TCP].flags.R:
                    ret += 1
            else:
                return utilities.NOT_AVAILABLE
                # In case the packet has UDP protocol
        return ret

    def psh_cnt(self, packets_of_flow):
        ret = 0
        for packet in packets_of_flow:
            if TCP in packet:
                if packet[TCP].flags.P:
                    ret += 1
            else:
                return utilities.NOT_AVAILABLE
                # In case the packet has UDP protocol
        return ret

    def ack_cnt(self, packets_of_flow):
        ret = 0
        for packet in packets_of_flow:
            if TCP in packet:
                if packet[TCP].flags.A:
                    ret += 1
            else:
                return utilities.NOT_AVAILABLE
                # In case the packet has UDP protocol
        return ret

    def urg_cnt(self, packets_of_flow):
        ret = 0
        for packet in packets_of_flow:
            if TCP in packet:
                if packet[TCP].flags.U:
                    ret += 1
            else:
                return utilities.NOT_AVAILABLE
                # In case the packet has UDP protocol
        return ret

    def fw_iat_tot(self, packets_of_flow):
        session_sender_ip = packets_of_flow[0][1].src

        ret = 0
        for ind in range(1, len(packets_of_flow)):
            if packets_of_flow[ind][1].src == session_sender_ip:
                ret += packets_of_flow[ind].time - packets_of_flow[ind - 1].time
        return ret

    # Right now the behavior is: Normal, NA | Normal, ddos | NA, NA

    def src_ip(self, packets_of_flow):
        return packets_of_flow[0][1].src

    def dst_ip(self, packets_of_flow):
        return packets_of_flow[0][1].dst

    def src_port(self, packets_of_flow):
        return packets_of_flow[0][2].sport

    def dst_port(self, packets_of_flow):
        return packets_of_flow[0][2].dport
