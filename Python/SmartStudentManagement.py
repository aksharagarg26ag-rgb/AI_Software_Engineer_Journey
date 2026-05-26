class Students:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.__marks = marks

    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.__marks)


students_list = []


while True:

    print("\nSMART STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if not choice.isdigit():

        print("Please enter number")
        continue

    choice = int(choice)

    # ADD STUDENT
    if(choice == 1):

        name = input("Enter student name : ")

        try:

            age = int(input("Enter age: "))
            marks = float(input("Enter marks: "))

            student = Students(name, age, marks)

            students_list.append(student)

            print("Student added!")

        except ValueError:

            print("Invalid input")

    # VIEW STUDENTS
    elif(choice == 2):

        if len(students_list) == 0:

            print("No student found")

        else:

            print("\nStudent List:")

            for student in students_list:

                student.display()

    # SEARCH STUDENT
    elif(choice == 3):

        search_name = input("Enter name to search: ")

        found = False

        for student in students_list:

            if student.name.lower() == search_name.lower():

                student.display()

                found = True

        if not found:

            print("Student not found!")

    # DELETE STUDENT
    elif(choice == 4):

        delete_student = input("Enter student to delete: ")

        found = False

        for student in students_list:

            if student.name.lower() == delete_student.lower():

                students_list.remove(student)

                print("Student Deleted!")

                found = True

                break

        if not found:

            print("Student not found")

    # EXIT
    elif(choice == 5):

        print("Exiting...")

        break

    else:

        print("Invalid choice")