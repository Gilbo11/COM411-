print("what level of brightness is required")
brightness_required = int(input())
print("adjusting brightness")
for brightness in range(2, brightness_required+1, 2):
    print(f"Beeps brightness level {'*' * brightness}")
    print(f"Bops brightness level {'*' * brightness}")
