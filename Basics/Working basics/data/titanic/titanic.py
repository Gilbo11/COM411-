import csv

records = []
headings = []

def load_data(file_path):
    print("loading data", end="")
    with open (file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)
    print("done")

def run():
    load_data("titanic.csv")
    num_records = len(records)
    print(f"successfully loaded {num_records} records")
run()