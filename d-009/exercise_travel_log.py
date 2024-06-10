"""
-=< 100 Days of Python >=-
-=[ Day 009 ]=-

Coding Exercise: Travel Log (L.95)
Ref: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/58076521-a623-49e9-8d55-7a0c76c60464?sl=ee33719e-7ebe-4e83-aafa-fabf7184a81b&st=eaddaad3-4d91-4dcc-a6a1-d559022fe042
"""
"""
Slide 1: Task
- Write a program that adds to a 'travel log'

Given an existing "travel_log" Dictionary, create a Function that will
add new entries to the existing dictionary.

Your function should take:
    - Country Name (a String)
    - Number of Times Visited (an Integer)
    - Names of all Cities Visited (as a List)

i.e. -- add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])

* DO NOT modify 'travel_log' directly
"""
country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# Do NOT change the code above 👆


"""
Slide 2: Solution
"""


def add_new_country(country_name, num_of_visits, cities_visited):
    """exercise using nested Dictionaries within a List"""
    travel_log.append({
        "country": country_name,
        "visits": num_of_visits,
        "cities": cities_visited,
    })
# NOTE: passing in the dictionary being appended to would probably be better


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {
      travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
