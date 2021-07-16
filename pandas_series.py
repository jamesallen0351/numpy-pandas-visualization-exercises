# panda exercises

# Part 1

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# Use pandas to create a Series named fruits from the following list:

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

print(fruits)

#1 Determine the number of elements in fruits.

fruits.describe()
fruits.count()
print(fruits.describe())
print(fruits.count())

#2 Output only the index from fruits.

index = fruits.sort_index()
print(index)

#3 Output only the values from fruits.

values = fruits.sort_values()
print(values)

#4 Confirm the data type of the values in fruits.

fruit_types = type(fruits)
print(fruit_types)

#5 Output only the first five values from fruits. 
#Output the last three values. 
#Output two random values from fruits.

first_five = fruits.head(5)
last_three = fruits.tail(3)
two_random = fruits.sample(2)
print(first_five, last_three, two_random)

#6 Run the .describe() on fruits to see what information it returns when called on a Series with string values.

describe_fruits = fruits.describe()
print(describe_fruits)

#7 Run the code necessary to produce only the unique string values from fruits.

unique_fruits = fruits.unique()
print(unique_fruits)

#8 Determine how many times each unique string value occurs in fruits.

unique_value = fruits.value_counts()
print(unique_value)

#9 Determine the string value that occurs most frequently in fruits.

most_frequent_fruits = fruits.value_counts().nlargest(n = 1, keep = "all")
print(most_frequent_fruits)

#10 Determine the string value that occurs least frequently in fruits.

counts = fruits.value_counts()
min_count = counts.min()
print(counts.where(counts == min_count).dropna())

# another way to answer #10 Determine the string value that occurs least frequently in fruits.
least_frequent_fruit = fruits.value_counts().nsmallest(n = 1, keep = "all")
print(least_frequent_fruit)
