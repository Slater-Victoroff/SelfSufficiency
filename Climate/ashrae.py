from constants import wetbulb_b, wetbulb_c, acceptable_temps

import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_dew_point_temperature(temp, humidity):
	"""
	Dew point temperature calculated via Magnus formula.

	Assumes inputs are vectorized

	Humidity should be given as a number from 0-100
	"""
	internal_formula = np.log(humidity) + ((wetbulb_b * temp) / (wetbulb_c + temp))
	return (wetbulb_c * internal_formula) / (wetbulb_b - internal_formula)

def check_acceptability(temp, humidity):
	"""
	Given a temperature and humidity, determine if the conditions are ASHRAE compliant
	"""
	acceptable_range = mplPath.Path(acceptable_temps)
	dew_point = calculate_dew_point_temperature(temp, humidity)
	print dew_point
	return acceptable_range.contains_point((temp, dew_point))

if __name__ == "__main__":
	temp_vector = np.array([-20, -5, 10, 25])
	humidity_vector = np.array([0.2, 0.5, 0.8, 0.3])
	golden_vector = np.array([-37.26, -13.83, 6.71, 6.21])
	print calculate_dew_point_temperature(temp_vector, humidity_vector)

	print check_acceptability(21, 0.4)
