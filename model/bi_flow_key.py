from model.uni_flow_key import UniFlowKey


class BiFlowKey(UniFlowKey):

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__ or \
                   (self.src_ip == other.dst_ip and
                    self.dst_ip == other.src_ip and
                    self.src_port == other.dst_port and
                    self.dst_port == other.src_port and
                    self.proto == other.proto)
        return NotImplemented

    def __hash__(self):
        return hash((self.src_ip, self.src_port)) | hash((self.dst_ip, self.dst_port))
