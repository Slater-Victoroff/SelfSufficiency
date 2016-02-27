from constants import wetbulb_b, wetbulb_c, acceptable_temps

import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def _calculate_dew_point_temperature(temp, humidity):
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
	dew_point = _calculate_dew_point_temperature(temp, humidity)
	points = np.vstack((temp, dew_point)).T
	return acceptable_range.contains_points(points)
