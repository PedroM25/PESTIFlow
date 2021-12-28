
import unittest

from model.algorithms.pcap.pcap_extraction_algorithm import PcapExtractionAlgorithm
from model.algorithms.pcap.uni_pcap_extraction_algorithm import UniPcapExtractionAlgorithm
from model.read_analyze_output import ReadAnalyzeOutput


class PcapExtractionAlgorithmTest(unittest.TestCase):
	"""
	Tests for methods in the PcapExtractionAlgorithm class.
	"""

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_read_and_analyze_data_instances_1(self):
		path_file = "test_resources/pcap/pcap_test_file_1.pcap"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 7
		rao.n_invalid_instances = 2
		rao.n_read_data_instances = 9

		ret = UniPcapExtractionAlgorithm(None).read_and_analyze_data_instances(path_file, 15)
		self.assertEqual(rao.n_valid_instances, ret.n_valid_instances)
		self.assertEqual(rao.n_invalid_instances, ret.n_invalid_instances)
		self.assertEqual(rao.n_read_data_instances, ret.n_read_data_instances)

	def test_read_and_analyze_data_instances_2(self):
		path_file = "test_resources/pcap/pcap_test_file_2.pcap"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 745
		rao.n_invalid_instances = 15
		rao.n_read_data_instances = 760

		ret = UniPcapExtractionAlgorithm(None).read_and_analyze_data_instances(path_file, 15)
		self.assertEqual(rao.n_valid_instances, ret.n_valid_instances)
		self.assertEqual(rao.n_invalid_instances, ret.n_invalid_instances)
		self.assertEqual(rao.n_read_data_instances, ret.n_read_data_instances)


