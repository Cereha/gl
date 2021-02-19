import unittest


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len(['b']), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_cut_out_element(self):
        a=['123456789']
        self.assertEqual(funk(a),'2345')


if __name__ == '__main__':
    unittest.main()
