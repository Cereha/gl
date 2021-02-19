import unittest

def get_second_to_fifth_elements(a):
    return a[2:5]

class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_roman_tkalenko_2(self):
        self.assertEqual(2, 2)

    def test_Olya_Koroban_FI94(self):
        a=[1,2,3,4,5,6,7,8,9]
        self.assertEqual(get_second_to_fifth_elements(a),[3,4,5])


if __name__ == '__main__':
    unittest.main()
