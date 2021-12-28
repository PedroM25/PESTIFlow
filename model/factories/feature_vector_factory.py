from model.bi_feature_vector import BiFeatureVector
from model.bi_features_interface import BiFeaturesInterface
from model.uni_feature_vector import UniFeatureVector
from model.uni_features_interface import UniFeaturesInterface


class FeatureVectorFactory:
    def create_feature_vector(self, algo):
        if issubclass(algo.__class__, BiFeaturesInterface):
            return BiFeatureVector()
        elif issubclass(algo.__class__, UniFeaturesInterface):
            return UniFeatureVector()
