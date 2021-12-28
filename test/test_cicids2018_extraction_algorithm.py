
import unittest

from model.algorithms.cicids2018_extraction_algorithm import CICIDS2018ExtractionAlgorithm
from model.read_analyze_output import ReadAnalyzeOutput


class CICIDS2018ExtractionAlgorithmTest(unittest.TestCase):
	"""
	Tests for methods in the CICIDS2018ExtractionAlgorithm class.
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

	def test_read_and_analyze_entries_1(self):
		path_file = "test_resources/cicids2018/cicids2018_test_file_1.csv"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 124
		rao.n_invalid_instances = 1
		rao.n_read_data_instances = 125

		ret = CICIDS2018ExtractionAlgorithm(None).read_and_analyze_entries(path_file)
		self.assertEqual(ret.n_valid_instances, rao.n_valid_instances)
		self.assertEqual(ret.n_invalid_instances, rao.n_invalid_instances)
		self.assertEqual(ret.n_read_data_instances, rao.n_read_data_instances)

	def test_read_and_analyze_entries_2(self):
		path_file = "test_resources/cicids2018/cicids2018_test_file_2.csv"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 0
		rao.n_invalid_instances = 1
		rao.n_read_data_instances = 1

		ret = CICIDS2018ExtractionAlgorithm(None).read_and_analyze_entries(path_file)
		self.assertEqual(ret.n_valid_instances, rao.n_valid_instances)
		self.assertEqual(ret.n_invalid_instances, rao.n_invalid_instances)
		self.assertEqual(ret.n_read_data_instances, rao.n_read_data_instances)
