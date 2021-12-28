class AttackTuple:
    def __init__(self, att_ip, vic_ip, att_begin, att_end):
        self.att_ip = att_ip
        self.vic_ip = vic_ip
        self.att_begin = att_begin
        self.att_end = att_end

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__))
