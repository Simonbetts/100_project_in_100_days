# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	05/12/2024

"""
Day 7: Machine Learning 

Learning how to use machine learning with Python

In Machine Learning (and in mathematics) there are often three values that interests us:

Mean - The average value
Median - The mid point value
Mode - The most common value


"""

import numpy
from math import sqrt
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# <!-- Calculate Mean, Median, Mode -->

mean_speed:float = numpy.mean(speed)
median_speed = numpy.median(speed)
mode_speed = stats.mode(speed)

# <!-- Display Results -->
print(f'Mean: {mean_speed}')
print(f'Median: {median_speed}')
print(f'Mode: {mode_speed}')

# <!-- Standard Deviation and Variance -->

'''
Standard Diviation 
- Standard deviation is a number that describes how spread out the values are.
- A low standard deviation means that most of the numbers are close to the mean (average) value.
- A high standard deviation means that the values are spread out over a wider range.

Variance
- Variance is another number that indicates how spread out the values are.
- In fact, if you take the square root of the variance, you get the standard deviation!
- Or the other way around, if you multiply the standard deviation by itself, you get the variance!
Standard Deviation is often represented by the symbol Sigma: σ
Variance is often represented by the symbol Sigma Squared: σ2
'''

standard_diviation_speed = numpy.std(speed)
variance_speed = numpy.var(speed)

print(f'')
print(f'Standard Dication: {standard_diviation_speed}')
print(f'Variance {variance_speed}')

print(f'Square Root of Variance: {sqrt(variance_speed)}')