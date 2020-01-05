import numpy as np
from opmpolhemus.utils.parser import mat_parser
from opmpolhemus.cluster.clusters import cluster_opms
from opmpolhemus.handler.frame import Frame
from opmpolhemus.main import coreg
import os
import unittest
dir_path = os.path.dirname(os.path.realpath(__file__))
test_file = os.path.join(dir_path, 'test_files', 'test01.txt')


class Test(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(type(mat_parser(test_file)).__name__, 'ndarray')
        self.assertEqual(np.shape(mat_parser(test_file))[1], 3)

    def test_cluster(self):
        frame = Frame(style='top')
        pcl = mat_parser(test_file)
        cluster = cluster_opms(pcl, frame)
        self.assertIsInstance(cluster, dict)
        self.assertGreater(len(cluster.keys()), 0)
        for value in cluster.values():
            self.assertIsInstance(value, dict)
            for val in value.values():
                self.assertIsInstance(val, list)

    def test_main(self):
        test_reg = coreg(test_file, 'top', log_level=0)
        self.assertIsInstance(test_reg, list)


if __name__ == '__main__':
    unittest.main()
