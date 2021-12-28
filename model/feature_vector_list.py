class FeatureVectorList:

    def __init__(self):
        self._feature_vectors = []

    def add_feature_vector(self, di):
        self._feature_vectors.append(di)

    def __iter__(self):
        return iter(self._feature_vectors)
