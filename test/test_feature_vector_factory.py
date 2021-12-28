
import unittest

from model.algorithms.airbus.graylog_extraction_algorithm import GraylogExtractionAlgorithm
from model.algorithms.pcap.bi_pcap_extraction_algorithm import BiPcapExtractionAlgorithm
from model.algorithms.pcap.uni_pcap_extraction_algorithm import UniPcapExtractionAlgorithm
from model.bi_feature_vector import BiFeatureVector
from model.factories.feature_vector_factory import FeatureVectorFactory
from model.uni_feature_vector import UniFeatureVector


class FeatureVectorFactoryTest(unittest.TestCase):
	"""
	Tests for methods in the FeatureVectorFactory class.
	"""

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		self.fvf = FeatureVectorFactory()

	def tearDown(self):
		pass

	def test_create_bi_feature_vector_1(self):
		alg = BiPcapExtractionAlgorithm(None)

		fv = self.fvf.create_feature_vector(alg)
		self.assertIsInstance(fv, BiFeatureVector)

	def test_create_bi_feature_vector_2(self):
		alg = GraylogExtractionAlgorithm(None)

		fv = self.fvf.create_feature_vector(alg)
		self.assertIsInstance(fv, BiFeatureVector)

	def test_create_uni_feature_vector_1(self):
		alg = UniPcapExtractionAlgorithm(None)

		fv = self.fvf.create_feature_vector(alg)
		self.assertIsInstance(fv, UniFeatureVector)
