Student_grade = { }
#Add a new students
def add_student(name,grade):
    Student_grade[name] = grade
    print(f"Added {name} with a {grade}")

def update_grade(name):
    if name in Student_grade:
        Student_grade[name] = grade
        print(f"{name} with mark are updated {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in Student_grade:
        del Student_grade[name]
        print(f"{name} has been successfully deleted!")
    else:
        print(f"{name} is not found!")

def display_all_student():
    if Student_grade:
        for name,grade in Student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No Students Found!")

def main():
    while True:
        print('\n Student Grade Management System')
        print("1. Add Students")
        print("2. Update Student Marks")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter Your choice = "))
        if choice == 1:
            name = input("Enter Student Name = ")
            grade = int(input("Enter Student Grade = "))
            add_student(name,grade)

        elif choice == 2:
            name = input("Enter Student Name = ")
            grade = int(input("Enter Student grade = "))
            update_grade(name, grade)
        
        elif choice == 3:
            name = input("Enter Studen Name = ")
            delete_student(name)
        
        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print("Closing The Program")
            break
        else:
            print("Invalid Choice")
main()
