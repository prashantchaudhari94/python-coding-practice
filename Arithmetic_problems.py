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
