# Writing the username
num_list = []
user_name : str = input("Write your name: ")
print()

# Let's collecting the three favorite numbers
for x in range(1, 4):
    num = int(input(f"Enter your {x} favorite number: "))
    num_list.append(num)

# Let's check if each number is even or odd
print(f"\n Hello, {user_name}! Let's explore your favorite numbers:\n")
for num in num_list:
    if num % 2 == 0:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")

# Let's display each number and its square
print()
for num in num_list:
    print(f"The number {num} and its square: ({num} , {num ** 2})")

# Let's calculate and display the sum of the numbers
sum_numbers = sum(num_list)
print(f"\nAmazing! The sum of your favorite number is: {sum_numbers} \n")

is_prime = True
if sum_numbers <=1:
    is_prime = False
for x in range (2, sum_numbers):
    if sum_numbers % x == 0:
        is_prime = False

# Let's check if the number is prime or composite
if is_prime:
    print(f"Wow! The number {sum_numbers} is a prime number!")
else:
    print(f"Great! The number {sum_numbers} is not a prime number")
