# this is one of the most important in python
# it can be used to modify the output
name = "biswanth"
age1 = 50
salary = 100.1
print("your name is: ", name)

print(f"your name is {name} and your age is {age1}")

# another approach
print("name is: %s, age is %d salary is %g" %(name, age1, salary))

print("name is {}, age is{}, salary is {}".format(name,age1, salary))