import numpy as np

# creating arrays

np.zeros(10)
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

# takes one arugment (size of the array) and fill the entire array with 0s
# or with ones:
np.ones(10)
# array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

# fill with some arbitary number
# parameters: size of the array, elements to fill with: 
np.full(10, 2.5)
# array([2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5])

# insert lists into array
a = np.array([1, 2, 3, 5, 7, 12])
a
# array([ 1,  2,  3,  5,  7, 12])

# To access an element of the array: use index
a[2]
# 3

#reassign values:
a[2] = 10
a
# array([ 1,  2, 10,  5,  7, 12])

# array functions

# arrange: creates a range of numbers (lower, upper), upper bound not inclusive
np.arange(3, 10)
# array([3, 4, 5, 6, 7, 8, 9])

# linespace: create an array of a given sized filled with numbers evenly spaced between the first and second parameter
np.linspace(0, 100, 11)
# array([  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90., 100.])


# Multi-dimensional arrays
# basically a list of lists

# parameters: first number is the numbe rof row, second number is the number of columns
n = np.zeros((5, 2))
#array([[0., 0.],  [0., 0.], [0., 0.], [0., 0.], [0., 0.]])

# accessing elements: indicate row and column
n[0, 1]
# 0

# reassign elements
n[0, 1] = 20
n
# the array but with first row of the second element (column) replaced with 1

# if we only pass one index, we get an entire row:
n[2]
# array([0, 0, 0])

# rewriting entire row:
n[2] = [1, 1]
# array same array but with the third row rewritten

# rewriting entire column:
n[:, 1]
# array([20,  5,  1])


# Randomly generated arrays:


# generating a 2D array with 5 rows and 2 columns
np.random.rand(5, 2)
# an array with random numbers btween 0 and 1, sampled from the standard uniform distribution

# to get reproducible result, we seed it
np.random.seed(2)
# now the cells after this seed, the results would be the same random sample we got

# if we want to specify the boundary of the numbers generated:
np.random.randint(low =0, high=100, size=(5, 2))


# Element-wise operations
a1 = np.arange(5)
a1
# array([0, 1, 2, 3, 4])

# add/multipy/divide all the number to the array or combine arrays
a1 + 1
# array([1, 2, 3, 4, 5])
a1 * 2
# array([0, 2, 4, 6, 8])


# Comparison operations


a1 >= 2
# array([False, False,  True,  True,  True])
# comparison between arrays also works too

# also preserve the reuslt for when the condition is true
a1[a1 > a]
# select the element of a for which the condition is true


# summarizing operations

a1.min()
a1.sum()
a1.mean()
a1.std()
n.min()
# this works for 2d arrays two


