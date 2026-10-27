# store many items
ages = [21, 72, 43, 76, 23, 78, 88, 90, 15]  # list

names = ["Zack", "Jane", "Jack", "Moha", "Rick", "Jack"]  # 10 9
# functions
ages.append(31)
# ages.clear()
# ages.sort()
# ages.reverse()
print(ages)

names.sort()
print(names)

jack_count = names.count("Jack")
print(jack_count)

print(len(names))
print(len(ages))

print(sum(ages) / len(ages))

# retrieve an element
# print(ages[0])
# print(ages[5]) # index
#
# print(names[0])
# 3
# print(names[-1]) # python specific
# print(names[-2])
# print(names[-5:]) # slicing
#
# print(ages[3:])
# print(ages[3:5]) # slicing
#
# print(ages[:3])
#
# print(ages[:5])

# set
scores = {88, 78, 88, 65, 77, 78}  # no duplicates
print(scores)
print(scores)
scores.add(90)
scores.remove(65)

# tuple immutable
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(weekdays[0])

# dictionary
person = {"name": "Jason", "age": 22, "weight": 53, "height": 1.88}
print(person["name"])
print(person["age"])

people = [
    {"name": "Aria", "age": 29},
    {"name": "Morris", "age": 20},
    {"name": "Hellen", "age": 23}
]

print(people[0]["age"])



