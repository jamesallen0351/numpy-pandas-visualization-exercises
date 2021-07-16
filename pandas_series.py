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

### Exercises Part II
### Explore more attributes and methods while you continue to work with the fruits Series.

# 1 Capitalize all the string values in fruits.
print(fruits.str.upper())

# 2 Count the letter "a" in all the string values (use string vectorization).
count_fruit = fruits.str.count('a').sum()
print(count_fruit)

# 3 Output the number of vowels in each and every string value.
num_vowels = fruits.str.count(r'[aeiou]')
print(num_vowels)

# 4 Write the code to get the longest string value from fruits.
fruit_length = fruits.str.len()
fruit_length.max()

#4 easier one liner
fruit_length_1 = max(fruits.str.len())
print(fruit_length_1)
# max(fruits, key=len)

# 5 Write the code to get the string values with 5 or more letters in the name.
fruit_length_5 = fruit_length[fruit_length >= 5]
print(fruit_length_5)

# 6 Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
mask = fruits.apply(lambda n: n.count('o') >= 2)
print(fruits[mask])

# 7 Write the code to get only the string values containing the substring "berry".
# mask = fruits.apply(lambda row: 'berry' in row)
# fruits[mask]
berry_mask = fruits.apply(lambda n: "berry" in n)
print(fruits[berry_mask])

# 8 Write the code to get only the string values containing the substring "apple".
#print(data[data.str.contains("apple")])
apple_1 = fruits[fruits.str.contains("apple")]
print(apple_1)

# 9 Which string value contains the most vowels?
#fruits[fruits.apply(vowel_counter) == fruits.apply(vowel_counter).max()]

fruits[max(fruits.str.count(r'[aeiou]'))]