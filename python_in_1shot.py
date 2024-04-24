text='hello parth'
text1="hello 'moto'"
text2=''' hello moto
how are you 
you are good or not
i hope you are fine'''
print(text2)

name="hello freshers to"
# print last character from string read string from the end
print(name[-1])
# print all characters from the 0th index
print(name[0:])
print(name[1:])
# print charactes between 0 to 5
print(name[0:5])
# copy string into another string
another=name[:]
print(another)
# it will print which not include first and last index
print(name[1:-1])

first="john"
last="wick"
print(first+'['+last+']'+"is a superhero")
# formated string
print(f'{name} [{last}] is a superhero')

# arithmetic operator

# it will divide 10 by 3 and return 3.333333333333 float value
print(10/3)
# but here by using double sign it return 3 integer value
print(10//3)
# print reminder
print(10%3)
# print 10 to the power 3
print(10**3)

# precedence rule
x=10+3*2**2
# output is 22
print(x)
y=(10+3)*2**2
# output is 52
print(y)
z=(10+3)*3-2
# output is 47
print(z)

x=2.9
# it will print 3
print(round(x))
y=-2.9
# it will print 2.9
print(abs(-2.9))

import math

# here the output is 2
print(math.floor(2.9))
# here the output is 3
print(math.ceil(2.9))

# if-else 
is_hot=True
is_cold=False

if is_hot:
    print("it is very hot day")
    print("drink more water")
if is_cold:
    print("it is cold weather")
    print("wear warm clothes")
else:
    print("enjoy your day")
print("good wish for for you")

price=100000
has_good_credit=True

if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f'down payment :${down_payment}')

# logical operator
has_good_income=True
has_good_family=False
# OR operator 
if has_good_income or has_good_family:
    print("you are living good life")
# AND operator
if has_good_income and  has_good_family:
    print("you are living good life")
# NOT operator
if has_good_income or not has_good_family:
    print("you are living good life")

# comparison operator
name="jay"
if(len(name)<5):
    print("name must contain atleast 5 characters")
elif(len(name)>50):
    print("name has maximum 50 characters")
else:
    print()

weight=int(input("enter weight"))
unit=input("L OR K :")
if unit.upper()=="L":
    converted=weight*0.45
    print(f"weight into kilos is {converted}")
else:
    converted=weight/0.45
    print(f"weight into pound is {converted}")

# guess number game
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=input("guess: ")
    guess_count+=1
    if guess==secret_number:
        print("you won")
        break
else:
    print("sorry you failed")

# car game
command=""
while command.lower()!="quit":
    command=input(">").lower()
    if command=="start":
        print("car started")
    elif command=="stop":
        print("car stopped")
    elif command=="help":
        print(""" 
               start-to start the car
               stop-to stop the car
              quit-to quit""")
    elif command=="quit":
        break;
    else:
        print("sorry i dont understand")   

# for loop
for item in "python":
    print(item)

for item in ["john","harry","tony"]:
    print(item)

# range function
for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,10,2):
    print(item)

prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(price)

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers=[5,2,5,2]
for x_count in numbers:
    print("x"*x_count)

# largest number in the list
numbers=[2,5,9,7,8,10,15]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)

numbers=[2,3,4,5,6,8,9]
# append 10 at after last index
numbers.append(10)
# insert 10 at 0th index
numbers.insert(0,10)
# it will pop last element
numbers.pop()
# it remove given element 
numbers.remove(8)
# it clear all the elements
numbers.clear()
# print number index
print(numbers.index(5))
# it will count occurence of the number
print(numbers.count(5))
# sort the given numbers
numbers.sort()
numbers.reverse()
print(numbers)

# remove duplicates in a list
duplicates=[2,2,3,3,4,4,5,5,6,6]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# unpacking
# in touple
coordinates=(1,2,3)
# in list
coordinates=[1,2,3]
x,y,z=coordinates
print(x)
print(y)
print(z)

# dictionary
customer={
    "name":"will smith",
    "is_eligible":True,
    "age":20
}
print(customer["name"])
# get is used to print none value if key value not exist
print(customer.get("name"))
# it will set birthdate 
print(customer.get("birthdate","1 jan 1980"))
# 2 nd method
customer["birthdate"]="1 jan 1980"
print(customer["birthdate"])

# exercise
phone=input("phone:")
digits_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"

}
output=""
for ch in phone:
   output+= digits_mapping(ch,"!")+""
print(output)

import math
math.sqrt()