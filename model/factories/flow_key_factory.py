from model.bi_features_interface import BiFeaturesInterface
from model.bi_flow_key import BiFlowKey
from model.uni_features_interface import UniFeaturesInterface
from model.uni_flow_key import UniFlowKey


class FlowKeyFactory:
    def create_flow_key(self, algo):
        if issubclass(algo.__class__, BiFeaturesInterface):
            return BiFlowKey()
        elif issubclass(algo.__class__, UniFeaturesInterface):
            return UniFlowKey()
