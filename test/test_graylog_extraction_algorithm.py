
import unittest

from model.algorithms.airbus.graylog_extraction_algorithm import GraylogExtractionAlgorithm
from model.read_analyze_output import ReadAnalyzeOutput


class GraylogExtractionAlgorithmTest(unittest.TestCase):
	"""
	Tests for methods in the GraylogExtractionAlgorithm class.
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

	def test_read_and_analyze_json_entries_1(self):
		path_file_1 = "test_resources/graylog/graylog_test_file_1.json"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 2
		rao.n_invalid_instances = 4
		rao.n_read_data_instances = 6

		ret = GraylogExtractionAlgorithm(None).read_and_analyze_json_entries(path_file_1)
		self.assertEqual(ret.n_valid_instances, rao.n_valid_instances)
		self.assertEqual(ret.n_invalid_instances, rao.n_invalid_instances)
		self.assertEqual(ret.n_read_data_instances, rao.n_read_data_instances)

	def test_read_and_analyze_json_entries_2(self):
		path_file_2 = "test_resources/graylog/graylog_test_file_2.json"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 0
		rao.n_invalid_instances = 0
		rao.n_read_data_instances = 0

		ret = GraylogExtractionAlgorithm(None).read_and_analyze_json_entries(path_file_2)
		self.assertEqual(ret.n_valid_instances, rao.n_valid_instances)
		self.assertEqual(ret.n_invalid_instances, rao.n_invalid_instances)
		self.assertEqual(ret.n_read_data_instances, rao.n_read_data_instances)
