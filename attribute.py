from email.errors import MalformedHeaderDefect
from unicodedata import name


class student():
    name= 'Arjun'
    age=20
    state='Kerala'
print(getattr(student,'name'))


delattr(student,'name')

""""
Or using dot notation 
"""
print(student.age)
student.gender='Male'
print(student.gender)

