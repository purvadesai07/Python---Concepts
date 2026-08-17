import csv
f = open("data1.csv", "w", newline='')
writer = csv.writer(f)
writer.writerow(["ID", "NAME", "AGE"])
writer.writerow([1, "Aanya", 17])
writer.writerow([2, "Aarav", 19])
writer.writerow([3, "Rahul", 15])
writer.writerow([4, "Eva", 16])
f.close()
f = open("data1.csv", "r")
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()
search = int(input("Enter ID: "))
found = False
f = open("data1.csv", "r")
reader = csv.reader(f)
next(reader)
for row in reader:
    if int(row[0]) == search:
        print(row)
        print("RECORD FOUND!!")
        found = True
        break
if not found:
    print("RECORD NOT FOUND!!")
f.close() 