from abc import ABC, abstractmethod


class UniFeaturesInterface(ABC):
    """ This class must NOT be instantiated. It is assumed that all the following methods are only executed if the
    cleanup() was executed before them hence, not verifications are performed such as if the packet contains IP,
    IPv6, TCP or UDP. This class exists just as a way to simplify the process of creating each feature for a certain
    input file in the future. It also helps
    """

    @abstractmethod
    def tot_l_fw_pkt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def transport_proto(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def fl_dur(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def tot_fw_pkt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def ts_beginning(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def s_tos(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def tcp_flags_fw(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def ts_end(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def fin_cnt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def syn_cnt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def rst_cnt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def psh_cnt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def ack_cnt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def urg_cnt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def land(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def fw_pkt_l_avg(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def fw_iat_tot(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def label(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def attack_type(self, some_data_instances):
        """ Right now the behavior is: Normal, NA | Normal, ddos | NA, NA
        """
        raise NotImplementedError

    @abstractmethod
    def src_ip(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def dst_ip(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def src_port(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def dst_port(self, some_data_instances):
        raise NotImplementedError
