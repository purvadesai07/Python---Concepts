file = open("students.txt", "w")
file.close()
while True:
    print("1. ADD RECORDS")
    print("2. DISPLAY RECORDS")
    print("3. SEARCH RECORDS")
    print("4. EXIT")
    choice = input("Enter your choice: ")
    if choice == '1':
        try:
            r = input("Enter Roll.no: ")
            n = input("Enter Name: ")
            m = float(input("Enter Marks: "))
            f = open("students.txt", "a")
            f.write(r + ","+ n + "," + str(m) + "\n")
            f.close()
            print("RECORDS ADDED.")
        except:
            print("INVALID RECORD.")
    elif choice == '2':
        try:
            f = open("students.txt", "r")
            print("RECORDS: ")
            for line in f:
                data = line.strip().split(",")
                print("Roll.no : ",data[0],"Name: ",data[1],"Marks: ",data[2])
            f.close()
        except:
            print("FILE NOT FOUND!!")
    elif choice == '3':
        try:
            s = input("Enter Roll.no to Search: ")
            f = open("students.txt", "r")
            found = False
            for line in f:
                data = line.strip().split(",")
                if data[0] == s:
                    print("Found: ",data)
                    found = True
                    break
            if not found:
                print("RECORD NOT FOUND!!")
            f.close()
        except:
            print("FILE NOT FOUND!!")
    elif choice == '4':
        break
    else:
        print("INVALID CHOICE!!")