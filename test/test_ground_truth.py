import unittest
from datetime import datetime
import utilities
from model.ground_truth import GroundTruth


class GroundTruthTest(unittest.TestCase):
    """
    Tests for methods in the GroundTruth class.
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.gt1 = GroundTruth("test_resources/ground_truth/ground_truth_test_file_1.txt")
        self.gt2 = None

    def tearDown(self):
        pass

    def test_flow_status_1(self):
        # flow begins AFTER attack begins and ends BEFORE attack ends
        ret = self.gt1.flow_status("10.0.0.1", "10.0.0.2",
                                   datetime.strptime("2020/11/26 19:12:00", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 19:55:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.ATTACK, ret)

    def test_flow_status_2(self):
        # flow begins AFTER attack begins and ends AFTER attack ends
        ret = self.gt1.flow_status("10.0.0.1", "10.0.0.2",
                                   datetime.strptime("2020/11/26 19:12:00", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 20:05:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.ATTACK, ret)

    def test_flow_status_3(self):
        # flow begins BEFORE attack begins and ends AFTER attack ends
        ret = self.gt1.flow_status("10.0.0.1", "10.0.0.2",
                                   datetime.strptime("2020/11/26 18:35:14", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 20:09:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.NORMAL, ret)

    def test_flow_status_4(self):
        # flow begins BEFORE attack begins but ends BEFORE attack ends
        ret = self.gt1.flow_status("10.0.0.1", "10.0.0.2",
                                   datetime.strptime("2020/11/26 18:35:14", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 19:34:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.NORMAL, ret)

    def test_flow_status_5(self):
        # flow begins BEFORE attack begins and ends BEFORE attack begins
        ret = self.gt1.flow_status("10.0.0.1", "10.0.0.2",
                                   datetime.strptime("2020/11/26 10:27:14", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 12:08:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.NORMAL, ret)

    def test_flow_status_6(self):
        # flow begins AFTER attack begins and ends BEFORE attack ends
        ret = self.gt1.flow_status("10.0.0.2", "10.0.0.1",
                                   datetime.strptime("2020/11/26 19:12:00", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 19:55:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.ATTACK_RESPONSE, ret)

    def test_flow_status_7(self):
        # flow begins AFTER attack begins and ends AFTER attack ends
        ret = self.gt1.flow_status("10.0.0.2", "10.0.0.1",
                                   datetime.strptime("2020/11/26 19:12:00", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 21:15:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.ATTACK_RESPONSE, ret)

    def test_flow_status_8(self):
        # flow begins BEFORE attack begins and ends AFTER attack ends
        ret = self.gt1.flow_status("10.0.0.2", "10.0.0.1",
                                   datetime.strptime("2020/11/26 18:35:14", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 20:09:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.NORMAL, ret)

    def test_flow_status_9(self):
        # flow begins BEFORE attack begins but ends BEFORE attack ends
        ret = self.gt1.flow_status("10.0.0.2", "10.0.0.1",
                                   datetime.strptime("2020/11/26 18:35:14", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 19:34:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.NORMAL, ret)

    def test_flow_status_10(self):
        # flow begins BEFORE attack begins and ends BEFORE attack begins
        ret = self.gt1.flow_status("10.0.0.2", "10.0.0.1",
                                   datetime.strptime("2020/11/26 10:27:14", GroundTruth._DATE_FORMAT),
                                   datetime.strptime("2020/11/26 12:08:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(utilities.NORMAL, ret)

    # -------

    def test_get_attack_type_1(self):
        # flow begins AFTER attack begins and ends BEFORE attack ends
        ret = self.gt1.get_attack_type("10.0.0.1", "10.0.0.2",
                                       datetime.strptime("2020/11/26 19:12:00", GroundTruth._DATE_FORMAT),
                                       datetime.strptime("2020/11/26 19:55:00", GroundTruth._DATE_FORMAT))
        self.assertEqual("attack_2", ret)

    def test_get_attack_type_2(self):
        # flow begins AFTER attack begins and ends AFTER attack ends
        ret = self.gt1.get_attack_type("10.0.0.1", "10.0.0.2",
                                       datetime.strptime("2020/11/26 19:12:00", GroundTruth._DATE_FORMAT),
                                       datetime.strptime("2020/11/26 20:05:00", GroundTruth._DATE_FORMAT))
        self.assertEqual("attack_2", ret)

    def test_get_attack_type_3(self):
        # flow begins BEFORE attack begins and ends AFTER attack ends
        ret = self.gt1.get_attack_type("10.0.0.1", "10.0.0.2",
                                       datetime.strptime("2020/11/26 18:35:14", GroundTruth._DATE_FORMAT),
                                       datetime.strptime("2020/11/26 20:09:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(None, ret)

    def test_get_attack_type_4(self):
        # flow begins BEFORE attack begins but ends BEFORE attack ends
        ret = self.gt1.get_attack_type("10.0.0.1", "10.0.0.2",
                                       datetime.strptime("2020/11/26 18:35:14", GroundTruth._DATE_FORMAT),
                                       datetime.strptime("2020/11/26 19:34:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(None, ret)

    def test_get_attack_type_5(self):
        # flow begins BEFORE attack begins and ends BEFORE attack begins
        ret = self.gt1.get_attack_type("10.0.0.1", "10.0.0.2",
                                       datetime.strptime("2020/11/26 10:27:14", GroundTruth._DATE_FORMAT),
                                       datetime.strptime("2020/11/26 12:08:00", GroundTruth._DATE_FORMAT))
        self.assertEqual(None, ret)
