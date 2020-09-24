from alternate_energy import WindEnergy
import numpy as np
import random

import unittest

class TestWindEnergy(unittest.TestCase):
    def test_average_speed(self):
        dates = np.array(["9/21/2020", "9/22/2020", "9/23/2020"])
        speeds = np.array([random.randint(1, 50) for x in dates])

        average = np.sum(speeds)/len(speeds)
        wind = WindEnergy(dates, speeds)

        self.assertAlmostEqual(wind.average_speed(), average)


if __name__ == '__main__':
    unittest.main()
