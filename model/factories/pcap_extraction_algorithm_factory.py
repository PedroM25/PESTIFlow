from model.algorithms.pcap.bi_pcap_extraction_algorithm import BiPcapExtractionAlgorithm
from model.algorithms.pcap.uni_pcap_extraction_algorithm import UniPcapExtractionAlgorithm


class PcapExtractionAlgorithmFactory:
    def create_pcap_extraction_algorithm(self, bi_flows, gt):
        if bi_flows:
            return BiPcapExtractionAlgorithm(gt)
        else:
            return UniPcapExtractionAlgorithm(gt)
