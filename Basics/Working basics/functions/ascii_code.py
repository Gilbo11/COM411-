print("program started")
print("please enter a standard character")
character = input()
if len(character) ==1:
    print(f"the ascii code for {character} is {ord (character)}")
else:
    print("Error single character is needed")
print("program ended")