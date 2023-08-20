import sys
import csv

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

students=[]
#students.append({"first":"first", "last":"last", "house":"house"})
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first=row['name'].split(', ')
            house=row['house']
            students.append({"first":first, "last":last, "house":house})

except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")

try:
    fieldnames = ['first', 'last', 'house']
    with open(sys.argv[2], "w") as file:
        writer=csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
except FileNotFoundError:
    sys.exit("File does not exist")