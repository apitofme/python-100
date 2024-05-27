"""
-=< 100 Days of Python >=-
-=[ Day 008 ]=-

Coding Exercise: Prime Number Checker (L.85)
Ref: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/4e31e198-3cbb-4dae-aad9-c0d99be60fa2?sl=78555e13-d113-4d5a-b665-6575a6185b97&st=hzMUDF7hRx7MhXXymdpjbUnqEzO51wRp
"""
"""
Slide 1: Task
- Write a function that checks if a given number is a Prime Number or not.

Notes:
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
- https://en.wikipedia.org/wiki/Prime_number

e.g. 2 is a prime number because it's only divisible by 1 and 2.
But 4 is not a prime number because you can divide it by 1, 2 or 4.
"""
"""
Slide 2: Solution
"""


def prime_checker(number):
    """exercise to check if a number is Prime"""
    # assume number is a Prime (to begin with)
    is_prime = True
    # round up half the number being checked to use in the range
    # - this reduces the test range necessary (i.e. increases efficiency)
    range_upper = number // 2 + 1
    # loop through range
    for n in range(2, range_upper):
        # test modulo of number against range
        if number % n == 0:
            # no 'remainder' means clean division
            is_prime = False
            break

    # display required output
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
