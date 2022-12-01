import random
print("please enter the minimum value")
min_value = int(input())
print("please enter the maximum value")
max_value = int(input())
random_number = random.randrange(max_value, min_value)
print(f"i am thinking of a number between {min_value} and {max_value} can you guess what it is")
guessed_correctly = False


