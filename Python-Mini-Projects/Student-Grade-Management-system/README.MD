# 🎓 Student Grade Management System

A simple command-line **Student Grade Management System** built with Python. This project allows users to add, update, delete, and view student grades using a dictionary.

## 📌 Features

* ➕ Add a new student and their grade
* ✏️ Update an existing student's grade
* 🗑️ Delete a student record
* 📋 Display all student records
* 🚪 Exit the program

## 🛠️ Technologies Used

* Python 3
* Dictionaries
* Functions
* Loops
* Conditional Statements

## 📂 Project Structure

```text
student_grade_management.py
README.md
```

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:

```bash
git clone https://github.com/your-username/student-grade-management-system.git
```

3. Navigate to the project folder:

```bash
cd student-grade-management-system
```

4. Run the program:

```bash
python student_grade_management.py
```

## 📖 Menu

```text
Student Grade Management System

1. Add Students
2. Update Student Marks
3. Delete Student
4. View Student
5. Exit
```

## 💻 Example Output

```text
Student Grade Management System

1. Add Students
2. Update Student Marks
3. Delete Student
4. View Student
5. Exit

Enter Your Choice = 1

Enter Student Name = Tanisha
Enter Student Grade = 95

Added Tanisha with a 95
```

## 📚 Functions

* `add_student(name, grade)` – Adds a new student.
* `update_grade(name, grade)` – Updates an existing student's grade.
* `delete_student(name)` – Deletes a student record.
* `display_all_student()` – Displays all student records.
* `main()` – Runs the menu-driven application.

## 📊 Data Structure

The program stores student records using a Python dictionary.

Example:

```python
Student_grade = {
    "Tanisha": 95,
    "Rahul": 88,
    "Aisha": 91
}
```

## 🚀 Future Improvements

* Save records to a file
* Load records automatically when the program starts
* Search for a student
* Sort students by name or grade
* Calculate average, highest, and lowest grades
* Add input validation and exception handling

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

