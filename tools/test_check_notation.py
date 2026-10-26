"""Regression checks for round axle bearings and ordinary pin joins.

Run from the repository root: python -m unittest discover -s tools -p test_check_notation.py
"""
import unittest
import tempfile
from pathlib import Path

from check_notation import mode, stage1


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

    def test_three_quarter_pin_rotates_in_gear_carrier(self):
        self.assertEqual(mode('pin stop (round)', 'pin hole (round)', ['32002', '87408']), 'TURNS')

    def test_cross_axle_locks_in_cross_hole(self):
        self.assertEqual(mode('axle stop (cross)', 'axle hole (cross)', ['59426', '32270']), 'LOCKED')

    def test_round_pin_does_not_fit_cross_hole(self):
        self.assertIsNone(mode('pin stop (round)', 'axle hole (cross)', ['43093', '32270']))


class RackMeshes(unittest.TestCase):
    def mesh_errors(self, part):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'training.tbl'
            path.write_text(f'STEP 1\nADD pinion 32270 black\nADD driven {part} black\nMESH pinion.teeth driven.teeth\nWHY Checks the driven part.\n', encoding='utf8')
            return [c for c in stage1(path)[1] if c['code'] == 'MESH_NO_TEETH']

    def test_rack_mesh_does_not_need_a_rotary_tooth_count(self):
        self.assertEqual(self.mesh_errors('87761'), [])

    def test_smooth_beam_still_cannot_mesh(self):
        self.assertEqual(len(self.mesh_errors('32316')), 1)


if __name__ == '__main__':
    unittest.main()
