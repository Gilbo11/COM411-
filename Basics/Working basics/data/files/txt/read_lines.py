import os
def search(file_name):
    print("searching...")
    with open(file_name) as file:
        for location in file:
            print(f"looked in {location.strip()}")
            print("done")


def run():
    search(library.txt)


if __name__ == "__main__":
    run()
