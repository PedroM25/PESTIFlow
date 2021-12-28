class ReadAnalyzeOutput:
    def __init__(self):
        self.n_valid_instances = 0
        self.n_invalid_instances = 0
        self.n_read_data_instances = 0

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__))
