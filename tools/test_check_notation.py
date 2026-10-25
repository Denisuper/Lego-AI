"""Regression checks for round axle bearings and ordinary pin joins.

Run from the repository root: python -m unittest discover -s tools -p test_check_notation.py
"""
import unittest

from check_notation import mode


class BearingModes(unittest.TestCase):
    def test_smooth_stopped_axle_rotates_in_round_bearing(self):
        self.assertEqual(mode('pin stop (round)', 'pin hole (round)', ['59426', '32184']), 'TURNS')

    def test_smooth_center_stop_rotates_in_round_bearing(self):
        self.assertEqual(mode('pin stop (round)', 'pin hole (round)', ['99008', '32009']), 'TURNS')

    def test_cv_shaft_neck_rotates_in_its_support_hub(self):
        self.assertEqual(mode('pin stop (round)', 'pin hole (round)', ['92906', '10197']), 'TURNS')

    def test_cv_shaft_cross_end_still_locks_its_gear(self):
        self.assertEqual(mode('axle stop (cross)', 'axle hole (cross)', ['92906', '6589']), 'LOCKED')

    def test_friction_axle_pin_stays_stiff_on_its_round_end(self):
        self.assertEqual(mode('pin stop (round)', 'pin hole (round)', ['43093', '32316']), 'STIFF')

    def test_frictionless_pin_rotates(self):
        self.assertEqual(mode('pin stop (round)', 'pin hole (round)', ['3749', '32316']), 'TURNS')

    def test_cross_axle_locks_in_cross_hole(self):
        self.assertEqual(mode('axle stop (cross)', 'axle hole (cross)', ['59426', '32270']), 'LOCKED')

    def test_round_pin_does_not_fit_cross_hole(self):
        self.assertIsNone(mode('pin stop (round)', 'axle hole (cross)', ['43093', '32270']))


if __name__ == '__main__':
    unittest.main()
