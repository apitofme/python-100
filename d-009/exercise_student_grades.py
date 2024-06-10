"""
-=< 100 Days of Python >=-
-=[ Day 009 ]=-

Coding Exercise: Student Grading Program (L.93)
Ref: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/56feec3f-61a3-47e9-95d9-7f9871a9a09a?sl=d568e30d-6f5e-46d3-9f36-167c874b232a&st=LjVbIcYUBnS3G9xyUt7QmjC6s8Yv8LBI
"""
"""
Slide 1: Task
- Write a program to convert student scores in to grades

The student scores 'database' will be given as a Dictionary, where the
student Names will be the Keys and the scores are the Values.

Your program should return a new Dictionary called 'student_grades' with
the student Names as Keys but now with the assigned grades as the Values.

This is the scoring criteria:
    - Scores 91 - 100: Grade = "Outstanding"
    - Scores 81 - 90: Grade = "Exceeds Expectations"
    - Scores 71 - 80: Grade = "Acceptable"
    - Scores 70 or lower: Grade = "Fail"

* DO NOT modify the 'student_scores' dictionary!
* DO NOT write any print statements!
"""
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

"""
Slide 2: Solution
"""
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for name, score in student_scores.items():
    grade = ""
    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[name] = grade

print(student_grades)
