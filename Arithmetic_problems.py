"""11. Print the cube of a number.
12. Find the remainder of two numbers.
13. Find the average of three numbers.
14. Convert Celsius to Fahrenheit.
15. Convert Fahrenheit to Celsius.
16. Calculate the area of a rectangle.
17. Calculate the perimeter of a rectangle.
18. Calculate the area of a square.
19. Calculate the circumference of a circle.
20. Calculate the area of a circle."""

#Print the cube of a number.

"""num=int(input("Enter a number: "))
cube=num**3
print(f"The cube of {num} is {cube}")"""

#Find the remainder of two numbers.
#formula Remainder = Dividend - (Divisor × Quotient)
#way1
"""num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
remander=num1%num2
print(f"The remander of {num1} and {num2} is {remander}")"""

#way 2
"""num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
if num2==0:
    print("Division by zero is not allwed")
else:
    print("Remainder is",num1%num2)"""

#Find the average of three numbers
#way 1- simple
"""num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=int(input("Enter another number: "))
average=(num1+num2+num3)/3
print("average is",average)"""
#way 2- using List
"""list=[1,2,3,4,5,6,7,8,9,10] #55

print(sum(list)/len(list))"""

#way 3- without using sum

"""list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in list:
   sum=sum+i
averge=sum/len(list)
print("average is",averge)"""


#Average of N Numbers (Interview Program)
"""n=int(input("Enter a how many numbers:"))
sum=0
for i in range(n):
    num=int(input("Enter the number:"))
    sum=sum+num
print(sum/n)"""

#14. Convert Celsius to Fahrenheit.
"""Take input from user for celcius value
write a formula
final result print
"""
celsius=int(input("Enter a number: "))
fahrenheit=(celsius*9/5)+32
print(f"The farenheit of {celsius} is {fahrenheit}")
 ######Input/Output & Variables##########

1. Print Hello World

print("Hello World")

2. Print your name and age

name=input("Enter the name:")
age=int(input("Enter the age:"))
print(f"name:{name}")
print(f"age:{age}")

3. Add two numbers

num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print(f"Addition of two number is:{num1+num2}")

4. Subtract two numbers
try:
    num1=int(input("Enter the number:"))
    num2=int(input("Enter the number:"))
    print(f"Subtraction of two number is:{num1-num2}")
except ValueError:
    print("Please enter valid integer")

5. Multiply two numbers
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print(f"multiplication of two number is {num1*num2}")

6. Divide two numbers
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print(f"Division of two number is {num1/num2}")

7. Swap two variables

var1=int(input("enter the first number:"))
var2=int(input("enter the second number:"))
#way1
temp=var1
var1=var2
var2=temp
#way 2
#var1,var2=var2,var1

#way 3
#10 VAR1
#20 VAR2
var1=var1+var2 #10+20=30
var2=var1-var2 #30-20=10
var1=var1-var2 #30-10=20
#print(f"Swap value for var1 is {var1} and for var2 is{var2}")


#8. Convert Celsius to Fahrenheit
celsius=float(input("Enter the number:"))

F = celsius * 1.8 + 32

print(f"{celsius} celcius to fahrenheit is {F} ")

#10. Calculate Simple Interest
#s=Amount*Time*rate of interset/100
amount=float(input("Enter the principal amount:"))
time=float(input("Enter the time:"))
interest=float(input("Enter the rate of intrest:"))
simple_interest=(amount*time*interest)/100
print(f"simple interest is {simple_interest}")

#11. Check even or odd
#simple way
num=int(input("Enter the number:"))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
#exception handling
try:
    num = int(input("Enter the number:"))
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
except ValueError:
    print("Please Enter valid integer")
#using function
num=int(input("enter the number:"))
def check_even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
result=check_even_odd(num)
print(result)


#12. Check positive, negative, or zero

num=int(input("Enter the number:"))
if num<0:
    print(f"{num} Negative number")
elif num>0:
    print(f"{num} positive number")
else:
    print("zero")