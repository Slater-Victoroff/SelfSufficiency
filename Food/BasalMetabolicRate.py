# BasalMetabolicRate.py
# Functions related to determining the energy necessary to sustain a human

# Enumerates the activity level multipliers for the BMR equation
class ActivityLevel:
    NONE = 1.2  # little to no exercise
    LIGHT = 1.375  # 1-3 days/wk
    MODERATE = 1.55  # 3-5 days/wk
    HEAVY = 1.725  # 6-7 days/wk
    VERY_HEAVY = 1.9  # 2/day, extra heavy workouts

"""
Finds the number of kCal needed to maintain current weight
Source: https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation
This uses the equations revised by Roza and Shizgal in 1984

@param weight - weight in kg
@param height - height in cm
@param age - age in years
@param isMale - boolean
@param activity_level - an ActivityLevel

@returns - the number of kilocalories needed per day
"""
def basal_metabolic_rate(weight, height, age, isMale, activity_level):
    if isMale:
        return (88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)) * activity_level
    else:
        return (447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)) * activity_level
