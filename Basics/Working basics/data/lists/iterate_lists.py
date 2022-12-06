def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("please select a direction")
    option = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")

def run():
    menu()

if __name__ == "__main__":
  run()