import unittest
import string
import random
import utils


class TestUtils(unittest.TestCase):

    # test linear search function
    def test_linear_search(self):
        results = utils.linear_search(self.manual_list, "a")
        rand_results = utils.linear_search(self.rand_list, self.rand_list[2])

        self.assertEqual(results, 0)
        self.assertNotEqual(results, "1")
        self.assertEqual(rand_results, 2)
        self.assertRaises(TypeError, utils.linear_search, "abcd", "a")

    # test index list function
    def test_index_list(self):
        results = utils.index_list(self.manual_list)
        is_tuple = type(results[0])
        rand_indexed_list = utils.index_list(self.rand_list_punctuation)
        ordered = rand_indexed_list[0][0] > rand_indexed_list[1][0]
        self.assertEqual(results, self.indexed_list)
        self.assertNotEqual(is_tuple, list)
        self.assertEqual(ordered, False)
        self.assertRaises(ValueError, utils.index_list, [])

    # test binary search function
    def test_binary_search(self):
        results = utils.binary_search(self.indexed_list, "a")
        rand_indexed_results = utils.index_list(self.rand_list)
        rand_binary_results = utils.binary_search(
            rand_indexed_results, self.rand_list[2]
        )

        self.assertEqual(results, 0)
        self.assertNotEqual(results, "0")
        self.assertEqual(rand_binary_results, 2)
        self.assertRaises(TypeError, utils.linear_search, "abcd", "a")

    # for each instance create three variables
    @classmethod
    def setUpClass(cls):
        cls.manual_list = ["a", "c", "d", "b"]
        cls.rand_list = random.choices(string.ascii_lowercase, k=10)
        cls.rand_list_punctuation = random.choices(string.punctuation, k=3)
        cls.indexed_list = [("a", 0), ("b", 3), ("c", 1), ("d", 2)]

    # for each instance delete those variables
    @classmethod
    def tearDownClass(cls):
        del cls.manual_list
        del cls.rand_list
        del cls.rand_list_punctuation
        del cls.indexed_list


if __name__ == "__main__":
    unittest.main()
