class student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = 0.0

    def input_data(self):
        self.name = input("Enter Name: ")
        self.roll_no = int(input("Enter Roll.No: "))
        self.marks = int(input("Enter Marks: "))

    def display_data(self):
        print("STUDENT DETAILS")
        print("Name of the Student: ", self.name)
        print("Roll.No of the Student: ", self.roll_no)
        print("Marks of the Student: ", self.marks)

s1 = student()
s1.input_data()
s2 = student()
s2.input_data()
s1.display_data()
s2.display_data()