from datetime import datetime

import utilities
from model.attack_tuple import AttackTuple
from model.services.io_service import IOService


class GroundTruth:
    """ File containing ground truth information must be in CSV and follow a display info in the following order:
    "attacker IP, victim IP, beginning of attack, end of attack, attack type". Dates provided must be in the following
    format: %d/%m/%Y %H:%M:%S"""

    _ATTACKER_IP = 0
    _VICTIM_IP = 1
    _TS_BEGIN = 2
    _TS_END = 3
    _ATT_TYPE = 4

    _DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

    def __init__(self, gt_path):
        self.gt_info = self._read_from_file(gt_path)

    def _read_from_file(self, gt_path):
        temp_gt_info = {}
        for current_line in IOService().read_lines_csv_file(gt_path, utilities.DELIM):
            # Each line is an attack
            at = AttackTuple(current_line[self._ATTACKER_IP], current_line[self._VICTIM_IP],
                             datetime.strptime(current_line[self._TS_BEGIN], self._DATE_FORMAT),
                             datetime.strptime(current_line[self._TS_END], self._DATE_FORMAT))
            try:
                temp_gt_info[at] = current_line[self._ATT_TYPE]
            except IndexError:
                temp_gt_info[at] = None
        return temp_gt_info

    def flow_status(self, fl_sender_ip, fl_receiver_ip, fl_begin, fl_end):
        for attack_tuple in self.gt_info:
            if fl_begin >= attack_tuple.att_begin and fl_end > attack_tuple.att_begin:
                if fl_sender_ip == attack_tuple.att_ip and \
                        fl_receiver_ip == attack_tuple.vic_ip:
                    return utilities.ATTACK
                elif fl_sender_ip == attack_tuple.vic_ip and \
                        fl_receiver_ip == attack_tuple.att_ip:
                    return utilities.ATTACK_RESPONSE
        return utilities.NORMAL  # Immediately returned when an empty groundtruth file is given

    def get_attack_type(self, fl_sender_ip, fl_receiver_ip, fl_begin, fl_end):
        """ If the flow passed as several parameters does not
        """
        for attack_tuple in self.gt_info:
            if fl_begin >= attack_tuple.att_begin and fl_end > attack_tuple.att_begin and \
                    fl_sender_ip == attack_tuple.att_ip and \
                    fl_receiver_ip == attack_tuple.vic_ip:
                return self.gt_info[attack_tuple]
        return None # Immediately returned when an empty groundtruth file is given
