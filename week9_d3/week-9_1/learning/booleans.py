# video notes

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.




############################################################################
# Boolean expressions are statements that can be either True or False. In Python, the boolean data type is represented by the built-in data type bool.

# Boolean expressions are commonly used for decision-making in programming.

# Here's a breakdown with examples:

# 1. Comparison Operators:
# These operators are used to compare two values:

# == (Equal to): Checks if the two values are equal.


# print(5 == 5)  # True
# print(5 == 6)  # False
# print(10 == 10)  # True
# print(5 != 8)    # True
# print(7 < 3)     # False
# != (Not equal to): Checks if two values are not equal.


# print(5 != 5)  # False
# print(5 != 6)  # True
# < (Less than): Checks if the left value is less than the right value.


# print(5 < 6)  # True
# print(6 < 5)  # False
# > (Greater than): Checks if the left value is greater than the right value.


# print(5 > 6)  # False
# print(6 > 5)  # True
# <= (Less than or equal to): Checks if the left value is less than or equal to the right value.


# print(5 <= 6)  # True
# print(6 <= 6)  # True
# >= (Greater than or equal to): Checks if the left value is greater than or equal to the right value.


# print(5 >= 6)  # False
# print(6 >= 6)  # True
# 2. Logical Operators:
# These operators are used to combine conditional statements:

# and: Returns True if both statements are true.

# x = 5
# print(x > 3 and x < 10)  # True
# age = 18
# print(age >= 18 and age < 65)  # True
# print(age < 18 or age >= 65)   # False
# or: Returns True if at least one of the statements is true.

# x = 5
# print(x > 3 or x > 10)  # True
# not: Reverse the result, returns False if the result is true.

# x = 5
# print(not(x > 3 and x < 10))  # False
# 3. Membership Operators:
# in: Returns True if a sequence with the specified value is present in the object.

# x = [1, 2, 3, 4, 5]
# print(3 in x)  # True
# not in: Returns True if a sequence with the specified value is not present in the object.

# x = [1, 2, 3, 4, 5]
# print(6 not in x)  # True
# 4. Identity Operators:
# is: Returns True if both variables are the same object.

# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x
# print(x is z)  # True, because z is the same object as x
# print(x is y)  # False, because x and y are not the same objects
# is not: Returns True if both variables are not the same object.

# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x is not y)  # True
# fruits = ['apple', 'banana', 'cherry']
# print('apple' in fruits)      # True
# print('grape' not in fruits)  # True
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
# print(a is c)       # True
# print(a is not b)   # True
# Remember, every boolean expression will evaluate to either True or False, and understanding this concept is fundamental for decision-making in programming.


#######################boolean expressions challenges#####################
# 20 points each challenge...
# problem 1: Check if a number is both even and divisible by 5.
# The program prompts the user for a number, checks whether it meets both conditions 
# (even and divisible by 5), and then outputs the result to the console.

# Prompt the user for a number

# Check if the number is even and divisible by 5

# Output the result to the console


# Problem 2: Number in Range
# Description:
# Create a program that checks whether a given number falls within a specified range, such as 10 to 20 (inclusive).

# Input: A number (integer)
# Output: "The number is within the range." or "The number is outside the range."
# Hint:
# Use the and operator to check if the number is greater than or equal to 10 and less than or equal to 20.

# Problem 3: Password Strength Checker
# Description:
# Write a program that checks if a user's password meets the following criteria:

# At least 8 characters long

# Contains at least one digit (0-9)

# Input: Password (string)

# Output: "Password is strong." or "Password is weak."

# Hint:
# Use the len() function to check the length and the any() function with a generator expression to check for a digit.

# Problem 4: Odd or Even and Multiple of 3
# Description:
# Create a program that determines if a number is odd or even and also checks if it is a multiple of 3.

# Input: A number (integer)
# Output:
# "Even and a multiple of 3."
# "Even but not a multiple of 3."
# "Odd and a multiple of 3."
# "Odd but not a multiple of 3."
# Hint:
# Use % for both the even check and the multiple of 3 check.

# Problem 5: Vowel or Consonant
# Description:
# Write a program that takes a single character as input and checks whether it is a vowel or a consonant. Assume the input is a lowercase letter.

# Input: A character (string of length 1)
# Output: "Vowel" or "Consonant"
# Hint:
# Use the in operator to check if the character belongs to the set {'a', 'e', 'i', 'o', 'u'}.