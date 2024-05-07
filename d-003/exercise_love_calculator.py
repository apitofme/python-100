"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-

Coding Exercise: Love Calculator (L.38)
"""
"""
Slide 1: Task
- Write a program that tests the compatibility between two people

To work out the "love score" between two people we will need to check
for how many times the letters in the words "TRUE" and "LOVE" occur in
each name, then combine these to give a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
-- "Your score is *x*, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
-- "Your score is *y*, you are alright together."

Otherwise, the message will just be their score. e.g.:
-- "Your score is *z*."

[HINT]
These functions will help you:
lower() count()
"""
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?

"""
Slide 2: Solution
"""
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

"""
My Solution:
- Ignoring the hint about using 'lower()' and 'count()', I used my
previous knowledge to iterate over each letter with a for-loop.
"""
t_count = 0
l_count = 0

# Concatenate both names together and make it all uppercase
# Then use a loop to check through each letter in turn...
for ltr in str(name1+name2).upper():
    # First counting if the letter is in 'TRUE'
    if ltr in 'TRUE':
        t_count += 1
    # Then counting (separately) if the letter is in 'LOVE'
    if ltr in 'LOVE':
        l_count += 1

# After the loop finishes we concatenate the two counts together as
# strings (because we don't want to "add" the numbers mathematically)
# BUT we convert the overall score back to an integer to store it
score = int(str(t_count) + str(l_count))

# Then we conditionally test the score to output the appropriate message
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/6bd4bb59-cd10-4657-b677-a79a6f03f44b?sl=3232881b-77b4-4179-b219-1ebca53fbb09&st=o5bSZ3jIbWAHysFhKE3t59IiQY4M0jLS
"""
