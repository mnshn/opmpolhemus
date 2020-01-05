from opmpolhemus.utils.parser import mat_parser
import os
import unittest
dir_path = os.path.dirname(os.path.realpath(__file__))
test_file = os.path.join(dir_path, 'test_files', 'test01.txt')


class Test(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(type(mat_parser(test_file)).__name__, 'ndarray')


if __name__ == '__main__':
    unittest.main()
