print("how many live cables must i avoid")
cables_to_avoid = int(input())
cables_avoided = 0
print()
while cables_avoided < cables_to_avoid:
    print("avoiding...", end="")
    cables_avoided = cables_avoided +1
    print(f"Done!{cables_avoided} cables avoided")