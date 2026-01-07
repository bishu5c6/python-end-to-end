# # 1) Check the given number is Positive or nagitive
# # 2) Check the largest of 2 numbers
# # 3) Check the largest of 3 numbers
# # 4) Print week number if you provide weekname as input.
#
# #check whether given number is positive or not
# a = int(input("enter a number: "))
#
#
# if a==1:
#     print("it is a positive number")
# elif a ==-1:
#     print("it is a negative number")
#
# else:
#     print("It is a number either give valid number")
#
# #2 method
# a = int(input("enter a number: "))
# if a > 0:
#     print("It is a postive number")
# else:
#     print("Negavtive number")
#
# # 2) Check the largest of 3 numbers
# #In a list of numbers finding the largest of two numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
#
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3
#
# print(f"The largest number is {largest}")

#3) find the largest of two numbers

# a = int(input("enter a number: "))
# b = int(input("enter a second number: "))
# if a>b:
#     print("The largedt of the two numbers is a: ",a)
# else:
#     print("B is the largest number: ",b)


# # 4) Print week number if you provide weekname as input.
week = int(input("Enter the week name: "))


if week ==1:
    print("Monday")
elif week ==2:
    print("Tuesday")
elif week ==3:
    print("wednesday")
elif week ==4:
    print("thursday")
elif week ==5:
    print("friday")
elif week ==6:
    print("Saturday")
elif week ==7:
    print("Sunday")
else:
    print("Invalid week number")

