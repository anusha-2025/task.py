#Write a program to check if a number is even or odd. An even number is divisible by 2, while an odd number is not
num=10
if num%2==0:
    print("even")
else:
    print("odd")    

#Check if a Year is a Leap Year
# A year is a leap year if:
# It is divisible by 4, but not divisible by 100, or
# It is divisible by 400.
year=2024
if year%4==0 or year%100!=0 and year%400==0:
    print("it is divisible")
else:
    print("it is not divisible") 

# Write a program that checks if a number is divisible by both 3 and 5. If it is, print "Divisible by 3 and 5", otherwise print "Not divisible by 3 and  5
num=15
if num%3==0 or num%5==0:
    print("it is divisible by 3and 5")
else:
    print("not divisible")

#Write a program that checks if a person is eligible to vote. The eligibility condition is that the person's age should be 18 or older
age=20
if age>18:
    print("elligible to vote")
else:
    print("not elligible") 

#Write a program to check if a given number is a multiple of 10.
a=20
if a%10==0:
    print("it is multiple of 10")

#Write a program to compare two numbers and print the smaller one
num1=4
num2=5 
if num1>num2:
    print("num1")
else:
    print("num2")    

#Write a program that asks the user for a number and prints:
#"Even" if the number is divisible by 2,
#"Odd" if the number is not divisible by 2,
#"Divisible by 5" if the number is divisible by 5 (but not by 2),
#"Not divisible by 2 or 5" if the number is neither divisible by 2 nor 5.
num=int(input("enter a number:"))
if num%2==0 and num%5==0:
    print("even")
elif num%2!=0 and num%5==0:
    print("divisible by 5")
elif num%2!=0 and num%5!=0:
    print("odd")
else:
    print("neither divisible by 2 or 5")

#Write a program that asks for the user’s age and classifies them into the following categories:
#"Child" if the age is less than 13,
#"Teenager" if the age is between 13 and 19,
#"Adult" if the age is between 20 and 59,
#"Senior" if the age is 60 or more
age=int(input("enter age:"))
if age<13:
    print("child")
elif age>=13 and age<=19:
    print("teenager")
elif age>=20 and age<=59:
    print("adult")
#Write a program that takes a number from the user and checks in which range it falls:
#"Below 0" if the number is less than 0,
#"Between 0 and 10" if the number is between 0 and 10 (exclusive),
#"Between 10 and 50" if the number is between 10 and 50 (exclusive),
#"Above 50" if the number is greater than 5
num=int(input("enter a number:"))
if num<0:
    print("below 0")
elif num<0:
    print("between 0 and 10")
elif num<50:
    print("between 10 and 50")
else:
    print("above 50")

#Write a program that converts temperature from Celsius to Fahrenheit. Ask the user to input the temperature in Celsius, and then:
#If the temperature is below 0°C, print "Below freezing point".
#If the temperature is between 0°C and 25°C, print "Cool".
#If the temperature is between 25°C and 40°C, print "Warm".
temp=int(input("enter temp:"))
if temp<0:
    print("below freezing point")
elif temp>0 and temp<25:
    print("cool")
elif temp>25 and temp<40:
    print("warm")
else:
    print("hot")
#Write a program that checks if a given grade (0-100) is valid or not. The grade is valid if it’s between 0 and 100 (inclusive). Otherwise, print "Invalid grade". Then, use elif to check:
#"Excellent" for a grade above or equal to 90,
#"Good" for a grade between 75 and 89,
#"Average" for a grade between 50 and 74,
#"Fail" for a grade below 50.
grade=int(input("enter grade:"))
if grade>=90:
    print("excellent")
elif grade>75 and grade<89:
    print("good")
elif grade>50 and grade<74:
    print("average")
elif grade<=50:
    print("fail")
else:
    print("invalid grade")

#Write a program that checks if a given number is positive, negative, or zero and prints the result
num=10
if num>0:
    print("positive")
else:
    print("negative")

#Write a program that accepts three numbers and determines the largest number among them.
n1=1
n2=2
n3=3
if n1>n2 and n1>n3:
    print("largest nbr1")
elif n2>n3 and n2>n1:
    print("largest nbr2")
else:
    print("largest is nbr3")
          
#Write a program to check if a given number is a prime number. A prime number is a number greater than 1 that is divisible only by 1 and itself.
a=7
if a>=1 or a%1==0 and a%7==0:
    print("prime")
else:
    print("not prime")

#Write a program that checks if a given character is a vowel or a consonant. The vowels are `a`, `e`, `i`, `o`, `u` (both uppercase and lowercase)
cha="anusha"
if (cha=="a" or cha=="e" or cha=="i" or cha=="o" or cha=="u" or cha=="A" or cha=="E" or cha=="I" or cha=="O" or cha=="U"):
    print("vowels")
else:
    print("consonents")  

#Print numbers from 1 to 10 using a for loop.
for i in range(1,11,1):
    print(i)

#Print all even numbers from 2 to 20 using a for loop
for i in range(2,21,2):
    print(i)   

#Print the square of each number from 1 to 10
for i in range(1,11):
    print(i*2)
     
#Print each letter of a given word (e.g., "Python") on a new line.
a="python"
for i in a:
    print(i)
#Find the sum of numbers from 1 to 10 using a for loop.
d=0
for i in range(1,11):
    d=d+1
print(d)    
#Print the multiplication table of a given number (e.g., 5).
for i in range(1,11):
    print(i*5)

#Reverse a given word using a for loop. 
a="anusha"
for i in range(len(a)-1,-1,-1):
    print(a[i])

#Find the factorial of a given number (e.g., 5!)
num=5
fact=0
for i in range(1,num+1):
    fact=fact*1
print(fact)    

#Count the number of vowels in a given word.
a="anusha"
v="aeiou"
c=0
for i in a:
    if i in v:
        c=c+1
print(c)    

#Write a function called book_details that takes two positional arguments (title and author) and one keyword argument (year, defaulting to 2024).
#Call the function with different argument orders and observe the output.
def book_details(title,author,year=2024):
    return title,author,year
print(book_details("amma diary lo konni pagilu","ravi mantri","2020"))
print(book_details("the wings on fire","kalam","2002"))
print(book_details("ramayanam","vedhavyasa")
      





















     
          


        









