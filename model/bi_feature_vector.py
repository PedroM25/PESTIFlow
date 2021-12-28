from model.uni_feature_vector import UniFeatureVector


class BiFeatureVector(UniFeatureVector):

    def __init__(self):
        super().__init__()
        # Total size of packets (in bytes) sent in backward direction
        self.tot_l_bw_pkt = self._DEFAULT_VALUE
        # Total # of packets sent in the backward direction
        self.tot_bw_pkt = self._DEFAULT_VALUE
        # Mean size of packet in backward direction
        self.bw_pkt_l_avg = self._DEFAULT_VALUE
        # Total time between two packets sent in the backward direction
        self.bw_iat_tot = self._DEFAULT_VALUE
