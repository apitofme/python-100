"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-

Coding Exercise: BMI Calculator (L.23)
"""
"""
Slide 1: Task - write a program that calculates a person's BMI

BMI stand for "Body Mass Index" and it is used as a measure of a person's
weight relative to their height to determine what is considered "healthy"
for a given individual (though the method has it's flaws and critics).

The formula used to calculate BMI is given as:

                weight (kg)
    BMI =   -------------------
            height (m) squared      -- i.e. height x height (in meters)

So, with inputs given as "height (in meters)" and "weight (in kilograms)"
see if you can calculate the BMI and print it out as an integer.
"""
height = input()
weight = input()

"""
Slide 2: Solution
"""
# First we want to convert the inputs, which we receive as strings,
# in to numbers that we can perform mathematical operations on...
print(type(height))  # we can check the type of input value ('str')
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and BODMAS (a.k.a. PEMDAS)
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

"""
My Solution:
"""
# First convert the input strings to numerical values
height = float(height)
weight = float(weight)

# Then calculate the BMI (remembering BODMAS)
bmi = weight / height ** 2
# -- OR -- bmi = weight / (height * height)

# Finally, print out the BMI value as an integer
print(int(bmi))

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/3c6091ed-ef4e-4247-82ae-167a2cb5208f?sl=1ea8e61d-4da3-4d1b-9c45-aed9ac32a221&st=Lkstz5KiPP91iISobr9xtB8AeKba3EVt
"""
