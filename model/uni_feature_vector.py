class UniFeatureVector:
    _DEFAULT_VALUE = ""

    def __init__(self):
        # Source IP
        self.src_ip = self._DEFAULT_VALUE
        # Destination IP
        self.dst_ip = self._DEFAULT_VALUE
        # Layer 3 source port
        self.src_port = self._DEFAULT_VALUE
        # Layer 3 destination port
        self.dst_port = self._DEFAULT_VALUE
        # Transport layer protocol
        self.transport_proto = self._DEFAULT_VALUE
        # Timestamp (beginning of the flow)
        self.ts_beginning = self._DEFAULT_VALUE
        # Timestamp (end of the flow)
        self.ts_end = self._DEFAULT_VALUE
        # Flow duration
        self.fl_dur = self._DEFAULT_VALUE
        # Total # of packets sent in the forward direction
        self.tot_fw_pkt = self._DEFAULT_VALUE
        # Average size of packet in forward direction
        self.fw_pkt_l_avg = self._DEFAULT_VALUE
        # Total size of packets (in bytes) sent in forward direction
        self.tot_l_fw_pkt = self._DEFAULT_VALUE
        # Total time between two packets sent in the forward direction
        self.fw_iat_tot = self._DEFAULT_VALUE
        # TCP flags which were set on packets sent in forward direction (ex. "FSA" for the flags FIN, SYN and ACK)
        self.tcp_flags_fw = self._DEFAULT_VALUE
        # Source TOS byte value
        self.s_tos = self._DEFAULT_VALUE
        # Number of packets with FIN
        self.fin_cnt = self._DEFAULT_VALUE
        # Number of packets with SYN
        self.syn_cnt = self._DEFAULT_VALUE
        # Number of packets with RST
        self.rst_cnt = self._DEFAULT_VALUE
        # Number of packets with PST
        self.psh_cnt = self._DEFAULT_VALUE
        # Number of packets with ACK
        self.ack_cnt = self._DEFAULT_VALUE
        # Number of packets with URG
        self.urg_cnt = self._DEFAULT_VALUE
        # If source and destination IP addresses equal and port numbers equal then, this variable takes value 1 else 0
        self.land = self._DEFAULT_VALUE

        # Class label (attack vs normal)
        self.label = self._DEFAULT_VALUE
        # Type of Attack (portScan, dos, bruteForce, -)
        self.attack_type = self._DEFAULT_VALUE

    def all_features(self):
        return self.__dict__.keys()  # Change this if a new order is ever required

    def all_variables(self):
        return self.__dict__

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__))
