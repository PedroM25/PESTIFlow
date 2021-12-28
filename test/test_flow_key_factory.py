
import unittest

from model.algorithms.airbus.graylog_extraction_algorithm import GraylogExtractionAlgorithm
from model.algorithms.pcap.bi_pcap_extraction_algorithm import BiPcapExtractionAlgorithm
from model.algorithms.pcap.uni_pcap_extraction_algorithm import UniPcapExtractionAlgorithm
from model.bi_flow_key import BiFlowKey
from model.factories.flow_key_factory import FlowKeyFactory
from model.uni_flow_key import UniFlowKey


class FlowKeyFactoryTest(unittest.TestCase):
	"""
	Tests for methods in the FlowKeyFactory class.
	"""

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		self.fkf = FlowKeyFactory()

	def tearDown(self):
		pass

	def test_create_feature_vector_1(self):
		alg = BiPcapExtractionAlgorithm(None)

		fv = self.fkf.create_flow_key(alg)
		self.assertIsInstance(fv, BiFlowKey)

	def test_create_feature_vector_2(self):
		alg = GraylogExtractionAlgorithm(None)

		fv = self.fkf.create_flow_key(alg)
		self.assertIsInstance(fv, BiFlowKey)

	def test_create_feature_vector_3(self):
		alg = UniPcapExtractionAlgorithm(None)

		fv = self.fkf.create_flow_key(alg)
		self.assertIsInstance(fv, UniFlowKey)
