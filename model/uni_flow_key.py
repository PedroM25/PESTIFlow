class UniFlowKey:
    def __init__(self):
        self.src_ip = None
        self.dst_ip = None
        self.src_port = None
        self.dst_port = None
        self.proto = None

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__))
