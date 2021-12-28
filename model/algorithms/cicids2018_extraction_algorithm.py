from datetime import datetime

import utilities
from model.algorithms.bi_extraction_algorithm import BiExtractionAlgorithm
from model.read_analyze_output import ReadAnalyzeOutput
from model.services import io_service
from model.services.io_service import IOService


class CICIDS2018ExtractionAlgorithm(BiExtractionAlgorithm):
    _DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
    _BENIGN = "Benign"

    _DST_PORT = 0
    _PROTOCOL = 1
    _TIMESTAMP = 2
    _FLOW_DURATION = 3
    _TOT_FWD_PKTS = 4
    _TOT_BWD_PKTS = 5
    _TOTLEN_FWD_PKTS = 6
    _TOTLEN_BWD_PKTS = 7
    # _FWD_PKT_LEN_MAX = 8
    # _FWD_PKT_LEN_MIN = 9
    _FWD_PKT_LEN_MEAN = 10
    # _FWD_PKT_LEN_STD = 11
    # _BWD_PKT_LEN_MAX = 12
    # _BWD_PKT_LEN_MIN = 13
    _BWD_PKT_LEN_MEAN = 14
    # _BWD_PKT_LEN_STD = 15
    # _FLOW_BYTS_S = 16
    # _FLOW_PKTS_S = 17
    # _FLOW_IAT_MEAN = 18
    # _FLOW_IAT_STD = 19
    # _FLOW_IAT_MAX = 20
    # _FLOW_IAT_MIN = 21
    _FWD_IAT_TOT = 22
    # _FWD_IAT_MEAN = 23
    # _FWD_IAT_STD = 24
    # _FWD_IAT_MAX = 25
    # _FWD_IAT_MIN = 26
    _BWD_IAT_TOT = 27
    # _BWD_IAT_MEAN = 28
    # _BWD_IAT_STD = 29
    # _BWD_IAT_MAX = 30
    # _BWD_IAT_MIN = 31
    # _FWD_PSH_FLAGS = 32
    # _BWD_PSH_FLAGS = 33
    # _FWD_URG_FLAGS = 34
    # _BWD_URG_FLAGS = 35
    # _FWD_HEADER_LEN = 36
    # _BWD_HEADER_LEN = 37
    # _FWD_PKTS_S = 38
    # _BWD_PKTS_S = 39
    # _PKT_LEN_MIN = 40
    # _PKT_LEN_MAX = 41
    # _PKT_LEN_MEAN = 42
    # _PKT_LEN_STD = 43
    # _PKT_LEN_VAR = 44
    _FIN_FLAG_CNT = 45
    _SYN_FLAG_CNT = 46
    _RST_FLAG_CNT = 47
    _PSH_FLAG_CNT = 48
    _ACK_FLAG_CNT = 49
    _URG_FLAG_CNT = 50
    # _CWE_FLAG_COUNT = 51
    # _ECE_FLAG_CNT = 52
    # _DOWN_UP_RATIO = 53
    # _PKT_SIZE_AVG = 54
    # _FWD_SEG_SIZE_AVG = 55
    # _BWD_SEG_SIZE_AVG = 56
    # _FWD_BYTS_B_AVG = 57
    # _FWD_PKTS_B_AVG = 58
    # _FWD_BLK_RATE_AVG = 59
    # _BWD_BYTS_B_AVG = 60
    # _BWD_PKTS_B_AVG = 61
    # _BWD_BLK_RATE_AVG = 62
    # _SUBFLOW_FWD_PKTS = 63
    # _SUBFLOW_FWD_BYTS = 64
    # _SUBFLOW_BWD_PKTS = 65
    # _SUBFLOW_BWD_BYTS = 66
    # _INIT_FWD_WIN_BYTS = 67
    # _INIT_BWD_WIN_BYTS = 68
    # _FWD_ACT_DATA_PKTS = 69
    # _FWD_SEG_SIZE_MIN = 70
    # _ACTIVE_MEAN = 71
    # _ACTIVE_STD = 72
    # _ACTIVE_MAX = 73
    # _ACTIVE_MIN = 74
    # _IDLE_MEAN = 75
    # _IDLE_STD = 76
    # _IDLE_MAX = 77
    # _IDLE_MIN = 78
    _LABEL = 79

    def read_and_analyze_entries(self, input_path):
        ra_output = ReadAnalyzeOutput()
        headers = True
        for current_line in IOService().read_lines_csv_file(input_path, utilities.DELIM):
            ra_output.n_read_data_instances += 1
            if headers:
                ra_output.n_invalid_instances += 1
                headers = False
                continue
            ra_output.n_valid_instances += 1
            self.data_instances_per_flow.add_data_instance(current_line)
        return ra_output

    def tot_l_fw_pkt(self, entry):
        return entry[self._TOTLEN_FWD_PKTS]

    def transport_proto(self, entry):
        return entry[self._PROTOCOL]

    def tot_fw_pkt(self, entry):
        return entry[self._TOT_FWD_PKTS]

    def ts_beginning(self, entry):
        return datetime.strptime(entry[self._TIMESTAMP], self._DATE_FORMAT)

    def s_tos(self, entry):
        pass

    def tcp_flags_fw(self, entry):
        pass

    def ts_end(self, entry):
        pass

    def fin_cnt(self, entry):
        return entry[self._FIN_FLAG_CNT]

    def syn_cnt(self, entry):
        return entry[self._SYN_FLAG_CNT]

    def rst_cnt(self, entry):
        return entry[self._RST_FLAG_CNT]

    def psh_cnt(self, entry):
        return entry[self._PSH_FLAG_CNT]

    def ack_cnt(self, entry):
        return entry[self._ACK_FLAG_CNT]

    def urg_cnt(self, entry):
        return entry[self._URG_FLAG_CNT]

    def fw_iat_tot(self, entry):
        return entry[self._FWD_IAT_TOT]

    def src_ip(self, entry):
        pass

    def dst_ip(self, entry):
        pass

    def src_port(self, entry):
        pass

    def dst_port(self, entry):
        return entry[self._DST_PORT]

    def tot_l_bw_pkt(self, entry):
        return entry[self._TOTLEN_BWD_PKTS]

    def tot_bw_pkt(self, entry):
        return entry[self._TOT_BWD_PKTS]

    def bw_iat_tot(self, entry):
        return entry[self._BWD_IAT_TOT]

    def label(self, entry):
        if entry[self._LABEL].lower() == self._BENIGN.lower():
            return utilities.NORMAL
        else:
            return utilities.ATTACK

    def attack_type(self, entry):
        if entry[self._LABEL].lower() == self._BENIGN.lower():
            return utilities.NOT_AVAILABLE
        else:
            return entry[self._LABEL]

    def fl_dur(self, entry):
        return entry[self._FLOW_DURATION]

    def land(self, entry):
        pass

    def fw_pkt_l_avg(self, entry):
        return entry[self._FWD_PKT_LEN_MEAN]

    def bw_pkt_l_avg(self, entry):
        return entry[self._BWD_PKT_LEN_MEAN]
