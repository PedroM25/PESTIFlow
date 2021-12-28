import utilities
from model.algorithms.uni_extraction_algorithm import UniExtractionAlgorithm
from model.bi_features_interface import BiFeaturesInterface


class BiExtractionAlgorithm(UniExtractionAlgorithm, BiFeaturesInterface):
    """This class must NOT be instantiated."""

    def bw_pkt_l_avg(self, packets_of_flow):
        try:
            return self.tot_l_bw_pkt(packets_of_flow) / self.tot_bw_pkt(packets_of_flow)
        except ZeroDivisionError:
            return utilities.NOT_AVAILABLE
