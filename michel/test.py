import unittest
from abbreviation import Abbrev


class abbrev_test(unittest.TestCase):

    def test_one(self):
        # Checking for upper case
        obj = Abbrev('steven garcia is a student at holberton school')
        self.assertTrue(obj.initials().isupper())

    def test_two(self):
        # checking if it is a string
        obj = Abbrev('steven garcia acuna')
        self.assertEqual(obj.initials().split(), ['S', 'G', 'A'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            obj.initials().split(2)

    def test_three(self):
        # Checking for the right initials
        obj = Abbrev('checking initials')
        assert obj.initials() == 'C I'


if __name__ == '__main__':
    unittest.main()
