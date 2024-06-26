import unittest
from array_list import ArrayList

class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.array_list = ArrayList()

    def test_add_and_get(self):
        self.array_list.add(1)
        self.array_list.add(2)
        self.array_list.add(3)
        self.assertEqual(self.array_list.get(0), 1)
        self.assertEqual(self.array_list.get(1), 2)
        self.assertEqual(self.array_list.get(2), 3)

    def test_get_out_of_bounds(self):
        self.array_list.add(1)
        with self.assertRaises(IndexError):
            self.array_list.get(1)
        with self.assertRaises(IndexError):
            self.array_list.get(-1)

    def test_remove(self):
        self.array_list.add(1)
        self.array_list.add(2)
        self.array_list.add(3)
        self.assertEqual(self.array_list.remove(1), 2)
        self.assertEqual(self.array_list.get(0), 1)
        self.assertEqual(self.array_list.get(1), 3)
        self.assertEqual(self.array_list.size(), 2)

    def test_remove_out_of_bounds(self):
        self.array_list.add(1)
        with self.assertRaises(IndexError):
            self.array_list.remove(1)
        with self.assertRaises(IndexError):
            self.array_list.remove(-1)

    def test_size(self):
        self.assertEqual(self.array_list.size(), 0)
        self.array_list.add(1)
        self.assertEqual(self.array_list.size(), 1)
        self.array_list.add(2)
        self.assertEqual(self.array_list.size(), 2)
        self.array_list.remove(0)
        self.assertEqual(self.array_list.size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.array_list.is_empty())
        self.array_list.add(1)
        self.assertFalse(self.array_list.is_empty())
        self.array_list.remove(0)
        self.assertTrue(self.array_list.is_empty())

    def test_clear(self):
        self.array_list.add(1)
        self.array_list.add(2)
        self.array_list.clear()
        self.assertEqual(self.array_list.size(), 0)
        self.assertTrue(self.array_list.is_empty())
        with self.assertRaises(IndexError):
            self.array_list.get(0)


if __name__ == '__main__':
    unittest.main()