value1 = 10
value2 = 100
value3 = "Sundeep"
# Example for string data type
print("Hello...I am coming.....({0}+{1})!!".format(value1, value2))

print(f"hi this is {value1}{value2}")

print(f"hi this is {value1+value2,value3}")

# Example for int data type
val1 = 100 #int
val2 = 3.14 #float

print(f"Addition:{val1+val2}")
print(f"Subtraction:{val1-val2}")
print(f"Multiplication:{val1*val2}")
print(f"Dividend:{val1/val2}")

# Example for if statement and if ternary example.
number = 5
if number == 5:
    print("Value is 5")
else:
    print("Value is not matching")

print(f"Value is {number}") if number == 5 else print("value is not matching")

# Example for lists

students = ["sundeep", "Sunny", "User1", "user2", "user3"]

print(len(students))

print(students[1:])
# Array slicer

print(students[1:-2])

students.reverse()

print(students)

# Example for For-loop

# method 1
for student in students:
    print(f"My Name is: {student}")

# method 2
x=0

for index in range(10):
    x+=10
    print(f"Current X-Men-{index} Value is:{x}")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# controlling the range in For-Loop

x=0

for index in range(5,10):
    x+=10
    print(f"Current X-Men-{index} Value is:{x}")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# controlling the range by 2 instead of 1 in For-Loop

x=0

for index in range(5,10,2):
    x+=10
    print(f"Current X-Men-{index} Value is:{x}")

# Example for dictionary

teachers = [
    {"name":"sunny","subject":"maths","score":"{0:.0f}%".format(1./3*100)},
    {"name":"sundeep","subject":"physics","score":"{0:.0f}%".format(1./3*100)}
]
print(teachers[0].values())
print(teachers[0].keys())
print(teachers['name'] == "sunny")