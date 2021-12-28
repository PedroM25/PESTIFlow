from abc import ABC, abstractmethod


class BiFeaturesInterface(ABC):
    """ This class must NOT be instantiated. It is assumed that all the following methods are only executed if the
    cleanup() was executed before them. Hence, not verifications are performed such as if the packet contains IP,
    IPv6, TCP or UDP
    """

    @abstractmethod
    def tot_l_bw_pkt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def tot_bw_pkt(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def bw_pkt_l_avg(self, some_data_instances):
        raise NotImplementedError

    @abstractmethod
    def bw_iat_tot(self, some_data_instances):
        raise NotImplementedError
