# Author --> Atharv Trivedi
# This is a maths table generator program built using python


# Taking input from user and storing it inside variable num
num = input("Enter the number whose mathematics table you want to print")

# Checking if the user has entered only a number or anything else
if num.isdigit():
    num = int(num)  # Typecasting the variable num to integer
    for x in range(1, 11):
        print(f"{num} x {x} = {num*x}")
else:
    print("Kindly enter a valid number")


# The same program can be built using while loop
# Try making the same program using while loop
# Good Luck !
