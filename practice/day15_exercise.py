import random

user_num_one = int(input("Enter the first number: "))
user_num_two = int(input("Enter the second number: "))

random_number = random.randint(user_num_one, user_num_two)
print(random_number)