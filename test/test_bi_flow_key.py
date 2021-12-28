
import unittest

from model.bi_flow_key import BiFlowKey


class BiFlowKeyTest(unittest.TestCase):
	"""
	Tests for methods in the BiFlowKey class.
	"""

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		self.instance1 = BiFlowKey()
		self.instance1.src_ip = "10.0.0.1"
		self.instance1.dst_ip = "10.0.0.2"
		self.instance1.src_port = "100"
		self.instance1.dst_port = "200"
		self.instance1.proto = "TCP"

		self.instance2 = BiFlowKey()
		self.instance2.src_ip = "10.0.0.1"
		self.instance2.dst_ip = "10.0.0.2"
		self.instance2.src_port = "100"
		self.instance2.dst_port = "200"
		self.instance2.proto = "TCP"

		self.instance3 = BiFlowKey()
		self.instance3.src_ip = "10.0.0.1"
		self.instance3.dst_ip = "10.0.0.2"
		self.instance3.src_port = "150"  # different
		self.instance3.dst_port = "200"
		self.instance3.proto = "TCP"

		self.instance4 = BiFlowKey()
		self.instance4.src_ip = "10.0.0.2"
		self.instance4.dst_ip = "10.0.0.1"
		self.instance4.src_port = "200"
		self.instance4.dst_port = "100"
		self.instance4.proto = "TCP"

	def tearDown(self):
		pass

	def test_eq_1(self):
		self.assertEqual(self.instance1, self.instance2)

	def test_eq_2(self):
		self.assertNotEqual(self.instance1, self.instance3)

	def test_eq_3(self):
		self.assertEqual(self.instance1, self.instance4)

	def test_hash_1(self):
		list1 = ["test1", "test2"]
		test_dict = {}
		test_dict[self.instance1] = ["test1"]
		test_dict[self.instance2].append("test2")

		self.assertEqual(test_dict[self.instance1], test_dict[self.instance2])

	def test_hash_2(self):
		list1 = ["test1", "test2"]
		test_dict = {}
		test_dict[self.instance1] = ["test1"]
		self.assertRaises(KeyError, lambda: test_dict[self.instance3].append("test2"))

	def test_hash_3(self):
		list1 = ["test1", "test2"]
		test_dict = {}
		test_dict[self.instance1] = ["test1"]
		test_dict[self.instance4].append("test2")

		self.assertEqual(test_dict[self.instance1], test_dict[self.instance4])

