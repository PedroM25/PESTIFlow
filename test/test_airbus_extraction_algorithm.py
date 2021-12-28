import json
import unittest

from model.algorithms.airbus.airbus_extraction_algorithm import AirbusExtractionAlgorithm
from model.algorithms.airbus.retourdeflamme_extraction_algorithm import RetourDeFlammeExtractionAlgorithm


class AirbusExtractionAlgorithmTest(unittest.TestCase):
	"""
	Tests for methods in the AirbusExtractionAlgorithm class.
	"""

	@classmethod
	def setUpClass(cls):
		pass #TODO

	@classmethod
	def tearDownClass(cls):
		pass #TODO

	def setUp(self):
		# Valid JSON from which the algorithm will be able to extract information.
		# From line 54 of the "Retour de Flamme" file provided for testing purposes
		valid_json = "{\"timestamp\":\"2018-12-12T08:33:33.000501+0100\",\"flow_id\":2053976700417061,\"event_type\":\"flow\",\"src_ip\":\"192.168.130.10\",\"src_port\":58987,\"dest_ip\":\"192.168.128.10\",\"dest_port\":53,\"proto\":\"UDP\",\"app_proto\":\"dns\",\"flow\":{\"pkts_toserver\":2,\"pkts_toclient\":2,\"bytes_toserver\":158,\"bytes_toclient\":158,\"start\":\"2018-12-12T08:24:10.324645+0100\",\"end\":\"2018-12-12T08:28:32.697873+0100\",\"age\":262,\"state\":\"established\",\"reason\":\"timeout\",\"alerted\":false}}"
		self.valid_dict_entry = json.loads(valid_json)

		# from line 1 of the "Retour de Flamme" file provided for testing purposes
		invalid_json_1 = "{\"timestamp\":\"2018-12-12T08:33:22.971961+0100\",\"flow_id\":789053033338041,\"in_iface\":\"ens33\",\"event_type\":\"dns\",\"src_ip\":\"192.168.128.10\",\"src_port\":4542,\"dest_ip\":\"103.86.96.100\",\"dest_port\":53,\"proto\":\"UDP\",\"dns\":{\"type\":\"query\",\"id\":52438,\"rrname\":\"fs.microsoft.com\",\"rrtype\":\"A\",\"tx_id\":0}}"
		self.invalid_dict_entry_1 = json.loads(invalid_json_1)

		self.rdfea = RetourDeFlammeExtractionAlgorithm(None)

	def tearDown(self):
		pass

	def test_entry_is_valid_1(self):
		self.assertTrue(AirbusExtractionAlgorithm.entry_is_valid(self.rdfea, self.valid_dict_entry))

	def test_entry_is_valid_2(self):
		self.assertFalse(AirbusExtractionAlgorithm.entry_is_valid(self.rdfea, self.invalid_dict_entry_1))
