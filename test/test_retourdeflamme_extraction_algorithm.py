
import unittest

from model.algorithms.airbus.retourdeflamme_extraction_algorithm import RetourDeFlammeExtractionAlgorithm
from model.read_analyze_output import ReadAnalyzeOutput


class RetourDeFlammeExtractionAlgorithmTest(unittest.TestCase):
	"""
	Tests for methods in the RetourDeFlammeExtractionAlgorithm class.
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
		path_file = "test_resources/retourdeflamme/retourdeflamme_test_file_1.log"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 5
		rao.n_invalid_instances = 8
		rao.n_read_data_instances = 13

		ret = RetourDeFlammeExtractionAlgorithm(None).read_and_analyze_entries(path_file)
		self.assertEqual(ret.n_valid_instances, rao.n_valid_instances)
		self.assertEqual(ret.n_invalid_instances, rao.n_invalid_instances)
		self.assertEqual(ret.n_read_data_instances, rao.n_read_data_instances)

	def test_read_and_analyze_entries_2(self):
		path_file = "test_resources/retourdeflamme/retourdeflamme_test_file_2.log"

		rao = ReadAnalyzeOutput()
		rao.n_valid_instances = 0
		rao.n_invalid_instances = 0
		rao.n_read_data_instances = 0

		ret = RetourDeFlammeExtractionAlgorithm(None).read_and_analyze_entries(path_file)
		self.assertEqual(ret.n_valid_instances, rao.n_valid_instances)
		self.assertEqual(ret.n_invalid_instances, rao.n_invalid_instances)
		self.assertEqual(ret.n_read_data_instances, rao.n_read_data_instances)
