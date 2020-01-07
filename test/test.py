import numpy as np
from opmpolhemus.utils.parser import mat_parser
from opmpolhemus.cluster.clusters import cluster_opms
from opmpolhemus.cluster.process import post_process
from opmpolhemus.handler.frame import Frame
from opmpolhemus.handler.sensors import Sensors
from opmpolhemus.sensors import sensors
from opmpolhemus.constants import Constants

import os
import unittest
dir_path = os.path.dirname(os.path.realpath(__file__))
test_txt_file = os.path.join(dir_path, 'test_files', 'test01.txt')
test_fif_file = os.path.join(dir_path, 'test_files', 'test01_raw.fif')

parsed_txt = mat_parser(test_txt_file)
parsed_fif = mat_parser(test_fif_file)


class Test(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(type(parsed_txt).__name__, 'ndarray')
        self.assertEqual(np.shape(parsed_txt)[1], 3)
        self.assertEqual(type(parsed_fif).__name__, 'ndarray')
        self.assertEqual(np.shape(parsed_txt)[1], 3)
        for el in parsed_txt:
            self.assertEqual(type(el).__name__, 'ndarray')
        for el in parsed_fif:
            self.assertEqual(type(el).__name__, 'ndarray')

    def test_cluster(self):
        frame = Frame(style='top')
        pcl = parsed_txt
        cluster = cluster_opms(pcl, frame)
        self.assertIsInstance(cluster, dict)
        self.assertGreater(len(cluster.keys()), 0)
        for value in cluster.values():
            self.assertIsInstance(value, dict)
            for val in value.values():
                self.assertIsInstance(val, list)
                self.assertGreater(len(val), 0)
        self.assertGreater(len(post_process(cluster, pcl)), 0)
        for point in post_process(cluster, pcl):
            self.assertEqual(len(point), frame.order)

    def test_cluster_from_fif(self):
        frame = Frame(style='top')
        pcl = parsed_fif
        cluster = cluster_opms(pcl, frame, start=0)
        self.assertIsInstance(cluster, dict)
        self.assertGreater(len(cluster.keys()), 0)
        for value in cluster.values():
            self.assertIsInstance(value, dict)
            for val in value.values():
                self.assertIsInstance(val, list)
                self.assertGreater(len(val), 0)
        self.assertGreater(len(post_process(cluster, pcl)), 0)

        for point in post_process(cluster, pcl):
            self.assertEqual(len(point), frame.order)

    def test_main(self):
        test_reg_txt = sensors(test_txt_file, 'top', log_level=0)
        test_reg_fif = sensors(test_fif_file, 'top', log_level=0)
        self.assertIsInstance(test_reg_txt, list)
        self.assertIsInstance(test_reg_fif, list)


if __name__ == '__main__':
    unittest.main()
