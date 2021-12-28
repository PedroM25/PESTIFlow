
import unittest

from model.algorithms.pcap.bi_pcap_extraction_algorithm import BiPcapExtractionAlgorithm
from model.algorithms.pcap.uni_pcap_extraction_algorithm import UniPcapExtractionAlgorithm
from model.factories.pcap_extraction_algorithm_factory import PcapExtractionAlgorithmFactory


class PcapExtractionAlgorithmFactoryTest(unittest.TestCase):
	"""
	Tests for methods in the PcapExtractionAlgorithmFactory class.
	"""

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		self.peaf = PcapExtractionAlgorithmFactory()

	def tearDown(self):
		pass

	def test_create_pcap_extraction_algorithm_1(self):
		alg = self.peaf.create_pcap_extraction_algorithm(True, None)
		self.assertIsInstance(alg, BiPcapExtractionAlgorithm)

	def test_create_pcap_extraction_algorithm_2(self):
		alg = self.peaf.create_pcap_extraction_algorithm(False, None)
		self.assertIsInstance(alg, UniPcapExtractionAlgorithm)