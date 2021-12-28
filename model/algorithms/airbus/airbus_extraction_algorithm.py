from datetime import datetime

import utilities
from model.algorithms.bi_extraction_algorithm import BiExtractionAlgorithm


def _get_datetime(date_str):
    return datetime.fromisoformat(date_str[:-2] + ":" + date_str[-2:])


class AirbusExtractionAlgorithm(BiExtractionAlgorithm):
    _SRC_IP = "src_ip"
    _DST_IP = "dest_ip"
    _SRC_PORT = "src_port"
    _DST_PORT = "dest_port"
    _PROTO = "proto"

    _FLOW = "flow"
    _PKTS_TOSERVER = "pkts_toserver"
    _PKTS_TOCLIENT = "pkts_toclient"
    _BYTES_TOSERVER = "bytes_toserver"
    _BYTES_TOCLIENT = "bytes_toclient"
    _START = "start"
    _END = "end"
    _AGE = "age"

    _UDP = "udp"

    _TCP = "tcp"
    _TCP_FLAGS_TS = "tcp_flags_ts"

    _SOURCE = "source"
    _MESSAGE = "message"

    def entry_is_valid(self, dict_entry):
        if self._FLOW in dict_entry and \
                (dict_entry[self._PROTO].lower() == self._TCP or dict_entry[self._PROTO].lower() == self._UDP):
            return True
        return False

    def tot_l_fw_pkt(self, dict_entry):
        return dict_entry[self._FLOW][self._BYTES_TOSERVER]

    def transport_proto(self, dict_entry):
        return utilities.PROTO_TO_IANA_NO[dict_entry[self._PROTO].lower()]

    def tot_fw_pkt(self, dict_entry):
        return dict_entry[self._FLOW][self._PKTS_TOSERVER]

    def ts_beginning(self, dict_entry):
        return _get_datetime(dict_entry[self._FLOW][self._START])

    def s_tos(self, dict_entry):
        pass

    def tcp_flags_fw(self, dict_entry):
        try:
            return "0x" + dict_entry[self._TCP][self._TCP_FLAGS_TS]
        except KeyError:
            return utilities.NOT_AVAILABLE

    def ts_end(self, dict_entry):
        return _get_datetime(dict_entry[self._FLOW][self._END])

    def fin_cnt(self, dict_entry):
        pass

    def syn_cnt(self, dict_entry):
        pass

    def rst_cnt(self, dict_entry):
        pass

    def psh_cnt(self, dict_entry):
        pass

    def ack_cnt(self, dict_entry):
        pass

    def urg_cnt(self, dict_entry):
        pass

    def fw_iat_tot(self, dict_entry):
        pass

    def src_ip(self, dict_entry):
        return dict_entry[self._SRC_IP]

    def dst_ip(self, dict_entry):
        return dict_entry[self._DST_IP]

    def src_port(self, dict_entry):
        return dict_entry[self._SRC_PORT]

    def dst_port(self, dict_entry):
        return dict_entry[self._DST_PORT]

    def tot_l_bw_pkt(self, dict_entry):
        return dict_entry[self._FLOW][self._BYTES_TOCLIENT]

    def tot_bw_pkt(self, dict_entry):
        return dict_entry[self._FLOW][self._PKTS_TOCLIENT]

    def bw_iat_tot(self, dict_entry):
        pass
