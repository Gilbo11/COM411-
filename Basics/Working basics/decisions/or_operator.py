print("what type of adventure should i have")
adventure_type = input()
if (adventure_type == "scary") or (adventure_type == "short"):
    print("entering the dark forest")
elif (adventure_type == "safe") or (adventure_type == "long"):
    print("taking the safe route")
else:
    print("not sure which route to take")