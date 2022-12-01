print("how many numbers should i sum up")
numbers_to_sum = int(input())
summed = 1
print()
total = 0
while summed <= numbers_to_sum:
    print(f"please enter number {summed} of {numbers_to_sum}")
    number = int(input())
    total = total + number
    summed = summed + 1

print(f"the answer is {total}")