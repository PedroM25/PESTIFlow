from model.algorithms.bi_extraction_algorithm import BiExtractionAlgorithm
from model.algorithms.pcap.uni_pcap_extraction_algorithm import UniPcapExtractionAlgorithm


class BiPcapExtractionAlgorithm(UniPcapExtractionAlgorithm, BiExtractionAlgorithm):

    # Sender is the source IP of the first packet seen in a session

    def tot_l_bw_pkt(self, packets_of_flow):
        session_receiver_ip = packets_of_flow[0][1].dst

        ret = 0
        for packet in packets_of_flow:
            if packet[1].src == session_receiver_ip:
                ret += len(packet)
        return ret

    def tot_bw_pkt(self, packets_of_flow):
        session_receiver_ip = packets_of_flow[0][1].dst

        ret = 0
        for packet in packets_of_flow:
            if packet[1].src == session_receiver_ip:
                ret += 1
        return ret

    def bw_iat_tot(self, packets_of_flow):
        session_receiver_ip = packets_of_flow[0][1].dst

        ret = 0
        for ind in range(1, len(packets_of_flow)):
            if packets_of_flow[ind][1].src == session_receiver_ip:
                ret += packets_of_flow[ind].time - packets_of_flow[ind - 1].time
        return ret
