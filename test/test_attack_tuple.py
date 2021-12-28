
import unittest

from model.attack_tuple import AttackTuple


class AttackTupleTest(unittest.TestCase):
	"""
	Tests for methods in the AttackTuple class.
	"""

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		self.instance1 = AttackTuple("25.0.0.3", "25.0.0.4", "2020/07/20 11:49:01", "2020/07/20 11:49:50")
		self.instance2 = AttackTuple("25.0.0.3", "25.0.0.4", "2020/07/20 11:49:01", "2020/07/20 11:49:50")
		self.instance3 = AttackTuple("25.0.0.4", "25.0.0.3", "2020/07/20 11:49:01", "2020/07/20 11:49:50")
		self.instance4 = "Test"

	def tearDown(self):
		pass

	def test_eq_1(self):
		self.assertEqual(self.instance1, self.instance2)

	def test_eq_2(self):
		self.assertNotEqual(self.instance1, self.instance3)

	def test_eq_3(self):
		self.assertNotEqual(self.instance1, self.instance4)

	def test_hash(self):
		list1 = ["test1", "test2"]
		test_dict = {}
		test_dict[self.instance1] = ["test1"]
		test_dict[self.instance2].append("test2")

		self.assertEqual(test_dict[self.instance1], test_dict[self.instance2])

