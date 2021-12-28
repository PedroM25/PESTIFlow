import csv
import os
import unittest

from model.bi_feature_vector import BiFeatureVector
from model.feature_vector_list import FeatureVectorList
from model.services.io_service import IOService
from model.uni_feature_vector import UniFeatureVector


class IOServiceTest(unittest.TestCase):
    """
    Tests for methods in the IOService class.
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.path = "io_service_test.txt"
        self.f = open(self.path, "w")

    def tearDown(self):
        self.f.close()
        os.remove(self.path)

    def test_write_feature_vectors_to_csv(self):
        fvl = FeatureVectorList()

        fv1 = BiFeatureVector()
        fv1.src_ip = "10.0.0.1"
        fv1.src_port = "25"
        fv1.fw_pkt_l_avg = "444"

        fv2 = BiFeatureVector()
        fv2.src_ip = "10.0.0.2"
        fv2.src_port = "40"
        fv2.dst_ip = "10.0.0.50"
        fv2.dst_port = "22"

        fvl.add_feature_vector(fv1)
        fvl.add_feature_vector(fv2)

        ret = IOService().write_feature_vectors_to_csv(self.path, fvl)

        expected_return = ["src_ip,dst_ip,src_port,dst_port,transport_proto,ts_beginning,ts_end,fl_dur,tot_fw_pkt,fw_pkt_l_avg,tot_l_fw_pkt,fw_iat_tot,tcp_flags_fw,s_tos,fin_cnt,syn_cnt,rst_cnt,psh_cnt,ack_cnt,urg_cnt,land,label,attack_type,tot_l_bw_pkt,tot_bw_pkt,bw_pkt_l_avg,bw_iat_tot",
                           "10.0.0.1,,25,,,,,,,444,,,,,,,,,,,,,,,,,",
                           "10.0.0.2,10.0.0.50,40,22,,,,,,,,,,,,,,,,,,,,,,,"]

        i = 0
        with open(self.path, mode="rt", encoding="utf-8") as file:
            while (line := file.readline()) != "":
                # The EOF char is an empty string
                self.assertEqual(expected_return[i], line.rstrip("\n"))
                i += 1

        self.assertEqual(ret, 352)
