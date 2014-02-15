#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("/data/projects/aniversario_peru_github/arturito")
import lib

class LibTest(unittest.TestCase):

    def test_tuit_inside_jail(self):
        status_id = 431779534288199680
        poly = [(-77.019896,-12.17337), (-77.019171,-12.172693), (-77.018152,-12.173726), (-77.018903,-12.174392)]
        result = lib.tuit_inside_jail(status_id, poly)
        self.assertEqual(result, True)

        status_id = 431779534288199680
        poly = [(-77.035468,-12.057237),(-77.034532,-12.05715),(-77.034435,-12.058),(-77.035369,-12.058097),(-77.035393,-12.05796),(-77.035393,-12.05796),(-77.035304,-12.057386),(-77.035449,-12.057381)]
        result = lib.tuit_inside_jail(status_id, poly)
        self.assertEqual(result, False)

        status_id = 433371957300428801
        poly = [(-77.035468,-12.057237),(-77.034532,-12.05715),(-77.034435,-12.058),(-77.035369,-12.058097),(-77.035393,-12.05796),(-77.035393,-12.05796),(-77.035304,-12.057386),(-77.035449,-12.057381)]
        result = lib.tuit_inside_jail(status_id, poly)
        self.assertEqual(result, True)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
