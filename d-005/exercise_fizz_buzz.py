"""
-=< 100 Days of Python >=-
-=[ Day 005 ]=-

Coding Exercise: FizzBuzz (Job Interview Question) (L.56)
"""
"""
Slide 1: Task
- Write a program that automatically solves the FizzBuzz game

>> FizzBuzz Rules:

Print each number from 1 to 100 in turn (including 100), except for:
    - when the number is divisible by 3 print "Fizz" instead
    - when the number is divisible by 5 print "Buzz"
    - and when the number is divisible by both 3 and 5 print "FizzBuzz"
"""
"""
Slide 2: Solution
"""
# loop through every number from 1 up to and including 100
for number in range(1, 101):
    # prepare an empty output string
    output = ""
    # if the number is divisible by 3
    if number % 3 == 0:
        # add "Fiz" to the output string
        output += "Fizz"
    # if the number is divisible by 5
    if number % 5 == 0:
        # add "Buzz" to the output string
        output += "Buzz"
    # if the output string is still empty
    # (i.e. number not divisible by 3 or 5)
    if output == "":
        # convert the number to a string and add that to the output
        output = str(number)
    # finally print the output string for this cycle of the loop
    print(output)

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/40e95268-2b4a-4b56-9dee-3df9e198213e?sl=f492fa95-de31-4f7f-ad16-62aef0a47d2b&st=YCckCNG1xhIk3qxZfa4NBuRPddqG5ure
"""
