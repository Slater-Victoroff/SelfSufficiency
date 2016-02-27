import numpy as np

wetbulb_b = 17.62  # unitless
wetbulb_c = 243.12  # degrees C

# four pairs of operative temp, dew point temp in C
acceptable_temps = np.array([
	[20.28, 2.78],
	[20, 11.67],
	[25.83, 17.22],
	[27.22, 2.78],
])
