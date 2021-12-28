
import unittest

from model.bi_feature_vector import BiFeatureVector
from model.feature_vector_list import FeatureVectorList
from model.uni_feature_vector import UniFeatureVector


class FeatureVectorListTest(unittest.TestCase):
	"""
	Tests for methods in the FeatureVectorList class.
	"""

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		self.fvl = FeatureVectorList()

		self.fv1 = BiFeatureVector()
		self.fv1.src_ip = "10.0.0.1"
		self.fv1.src_port = "25"

		self.fv2 = UniFeatureVector()
		self.fv2.src_ip = "10.0.0.2"
		self.fv2.src_port = "40"

	def tearDown(self):
		pass

	def test_add_feature_vector(self):

		self.fvl.add_feature_vector(self.fv1)

		test_fv = BiFeatureVector()
		test_fv.src_ip = "10.0.0.1"
		test_fv.src_port = "25"

		self.assertEqual(self.fvl._feature_vectors[-1], test_fv)

	def test_iter(self):
		self.fvl.add_feature_vector(self.fv1)
		self.fvl.add_feature_vector(self.fv2)

		test_fv1 = BiFeatureVector()
		test_fv1.src_ip = "10.0.0.1"
		test_fv1.src_port = "25"

		test_fv2 = UniFeatureVector()
		test_fv2.src_ip = "10.0.0.2"
		test_fv2.src_port = "40"

		list1 = [test_fv1, test_fv2]
		i = 0
		for fv in self.fvl:
			self.assertEqual(fv, list1[i])
			i += 1

	def test_empty_list(self):
		self.assertEqual(len(self.fvl._feature_vectors), 0)

