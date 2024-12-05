# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	05/12/2024

"""
Day 7: Machine Learning 

- Percentiles are used in statistics to give you a number 
- that describes the value that a given percent of the values are lower than.
"""

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

percentage = 75
percentile_age = numpy.percentile(ages, percentage)

print(f'Percentile: {percentile_age}')


# <!--Data Distribution -->

'''
- In the real world, the data sets are much bigger, 
- but it can be difficult to gather real world data, at least at an early stage of a project.

Random Data Distribution


Normal/Gaussian data distribution
- In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, 
- after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.
'''
import matplotlib.pyplot as plt

data_set = numpy.random.uniform(0.0, 5.0, 100000)
data_set_normal = numpy.random.normal(0.0, 5.0, 100000)

# print(f'Data Set: {data_set}')

plt.hist(data_set, 100)
plt.show()
plt.hist(data_set_normal, 100)
plt.show()

# <!-- Scatter Plot -->

'''
A scatter plot is a diagram where each value in the data set is represented by a dot.
'''

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()