import unittest

from model.data_instance_list import DataInstanceList


class DataInstanceListTest(unittest.TestCase):
    """
	Tests for methods in the DataInstanceList class.
	"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.dil = DataInstanceList()

    def tearDown(self):
        pass

    def test_add_data_instance(self):
        self.dil.add_data_instance("test")
        self.assertEqual(self.dil._data_instances[-1], "test")

    def test_iter(self):
        self.dil.add_data_instance("isep")
        self.dil.add_data_instance("porto")

        list1 = ["isep", "porto"]
        i = 0
        for di in self.dil:
            self.assertEqual(di, list1[i])
            i += 1

    def test_empty_list(self):
        self.assertEqual(len(self.dil._data_instances), 0)
