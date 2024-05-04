"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-

Coding Exercise: BMI v2.0 (L.33)
"""
"""
Slide 1: Task
- Building on our previous BMI Calculator, write a program that
calculates a person's BMI given their height and weight (again).
Then, rather than just printing out the raw number, this time we will
print out the medical classification bracket that the BMi falls
under:
    - Under 18.5 they are underweight
    - Equal to or over 18.5 but below 25 they have a normal weight
    - Equal to or over 25 but below 30 they are slightly overweight
    - Equal to or over 30 but below 35 they are obese
    - Equal to or over 35 they are clinically obese.
"""
height = float(input())
weight = int(input())
"""
Slide 2: Solution
"""
# Calculate the BMI: weight divided by the height squared
bmi = weight / height ** 2
# Prepare the first part of the output string
output = f"Your BMI is {bmi}, "
# Use what we've learned about conditional statements to add the final
# part of the output string based on the BMI result
if bmi < 18.5:
    output += "you are underweight."
elif bmi < 25:
    output += "you have a normal weight."
elif bmi < 30:
    output += "you are slightly overweight."
elif bmi < 35:
    output += "you are obese."
else:
    output += "you clinically obese."
# Finally, print out the whole output string
print(output)

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/7a12b4b1-76d3-4d04-820d-938547daba55?sl=eb333545-4ecd-4273-bee6-62561b17c787&st=9HOXX6cF3RnnbdAcCm5XJ5PNq704Z9Mb
"""
