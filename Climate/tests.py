import unittest
import numpy as np

from ashrae import _calculate_dew_point_temperature, check_acceptability

class TestStringMethods(unittest.TestCase):
	temp_vector = np.array([-20, -5, 10, 25])
	humidity_vector = np.array([0.2, 0.5, 0.8, 0.3])

	def test_dew_point(self):
		golden_vector = np.array([-37.26, -13.83, 6.71, 6.21])

		answer = _calculate_dew_point_temperature(self.temp_vector, self.humidity_vector)
		self.assertTrue(np.allclose(answer, golden_vector, rtol=0.02))

	def test_acceptability(self):
		golden_vector = np.array([False, False, False, True])

		answer = check_acceptability(self.temp_vector, self.humidity_vector)
		self.assertTrue(np.array_equal(answer, golden_vector))

if __name__ == '__main__':
    unittest.main()
