# if else
import os

import sys

name = input("What is your name?:")

age = input("Enter the age:")  # 20 '20'

if not age.isnumeric():
    print("Invalid age")
    # teminate
    os._exit(0)
    # sys.exit()

if int(age) > 18:
    print(name + " is an adult")
else:
    print(name + " is a child")
# lists, booleans, tuples, dictionary, loops

