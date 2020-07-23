"""
Numpy vs Lists
"""

"""
Size of an array
Shape of an array
Reshaping an array
Extracting a specific value from an array
Extracting multiple values from an array
Reversing the order of an array
Finding the max, min, sum of an array
Finding the mean, median, variance and standard deviation
"""


"""
Task
	import numpy as np,nan
	
	n = np.array([[nan, 0.30163819, nan],
	       [0.54629113, 0.67017515, 0.9620984 ],
	       [0.71410713, nan, 0.56288168],
	       [ nan, 0.60435705, 0.83555395]])
	n


	Given the above numpy array,do the following:

		- Create a new numpy array num_one from n and replace all the null values (i.e nan) with 0.
		- Create a new numpy array num_two from n and replace all null values (i.e nan) with the mean of the whole array(num)
		- Create a new numpy array num_three from n and replace the null values (i.e nan) of each row with the mean of the row it's in.
		- Create a new numpy array from num_four from n and replace the null values (i.e nan) with the mean of the column it's in.
"""