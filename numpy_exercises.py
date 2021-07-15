# numpy_exercises

import numpy as np 

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1 How many negative numbers are there?
len(a[a<0])

print("The total number of negative numbers is", len(a[a<0]))

## also can be done this way 
(a < 0).sum()

## this works too
np.count_nonzero(a < 0)

## also this one
a[a < 0].size

# 2 How many positive numbers are there?
len(a[a>=0])

# another way to answer
(a > 0).sum()

print("The total number of positive numbers is", len(a[a>=0]))

# 3 How many even positive numbers are there?
step_1 = (a[a % 2 == 0]) 
step_2 = step_1 > 0
step_1[step_2]

#another way : do not count zero as a positive numbers
#is_positive = a > 0
#is_even = a 2 % == 0

#mask = is_positive & is_even

#a[mask]

# additional way
#((a.0) & (a%2==0)).sum()
print("The totat number of positive even numbers is", len(step_1[step_2]))

# 4 If you were to add 3 to each data point, how many positive numbers would there be?
step_a = a + 3
step_b = len(a[a >= 0])
step_b

print("If you were to add 3 to each data point, how many positive numbers would there be?", step_b)

## another way

plus_three = a + 3
(plus_three > 0).sum()


# 5 If you squared each number, what would the new mean and standard deviation be?
step_sq = a ** 2
step_mn = step_sq.mean
step_std = step_sq.std

step_sq
step_mn()
step_std()

#another way
(a ** 2).mean()
(a ** 2).std()

print("If you squared each number, what would the new mean and standard deviation be?", "mean", step_mn(), "standard deviation", step_std())

# 6 A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set.
a - a.mean()
# check 
(a-a.mean()).mean()

print("This is done by subtracting the mean from each data point. Center the data set.", a-a.mean())

# 7 Calculate the z-score for each data point.
from scipy import stats

stats.zscore(a)
 
print("The z-score for each data point is", stats.zscore(a))

#another way

numerator = (a-a.mean())
denominator = a.std()
z_score = numerator / denominator
print("another way to get the z-score", z_score)

# 8 Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

import numpy as np
# Life w/o numpy to life with numpy
print("More Numpy Practice Exercises")
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("a now =", a)
# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
a = np.array([1,2,3,4,5,6,7,8,9,10])

sum_of_a = a.sum()

print("The sum of 'a' is", sum_of_a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a.min()

print("The min of 'a' is", min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a.max()

print("The max of 'a' is", max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a.mean

print("The mean of 'a' is", mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.prod(np.array(a))  

print("The product of multiplying all the numbers in 'a' is", product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a ** 2

print("The squares of 'a' are", squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = (a[a%2==1])    

print("The odds in a are", odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = (a[a % 2 == 0])

print("The evens in 'a' are", evens_in_a)


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

np.b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b_1 = b.sum
print("The sum of 'b' is", sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

print("The min of 'b' is", min_of_b)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

print("The max of B")

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print("The odds in b are", odds_in_b)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.

# Exercise 10 - transpose the array b.

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2