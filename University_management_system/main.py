class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


class Student(Person):
    def __init__(self, name, age, id, department):
        super().__init__(name, age, id)
        self.department = department
        self.courses = []

    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def show_details(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")
        print(f"Department: {self.department}")
        print("Courses Enrolled:", self.courses)


class Teacher(Person):
    def __init__(self, name, age, id, subject):
        super().__init__(name, age, id)
        self.subject = subject

    def show_details(self):
        print("\n--- Teacher Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")
        print(f"Subject: {self.subject}")


class Course:
    def __init__(self, course_code, course_name, faculty):
        self.course_code = course_code
        self.course_name = course_name
        self.faculty = faculty

    def show_course(self):
        print("\n--- Course Details ---")
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Faculty: {self.faculty}")


# Lists to store data
students_list = []
teachers_list = []
courses_list = []


def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    id = input("Enter Student ID: ")
    dept = input("Enter Department: ")

    s = Student(name, age, id, dept)
    students_list.append(s)
    print("Student added successfully!\n")


def add_teacher():
    name = input("Enter Teacher Name: ")
    age = int(input("Enter Age: "))
    id = input("Enter Teacher ID: ")
    subject = input("Enter Subject: ")

    t = Teacher(name, age, id, subject)
    teachers_list.append(t)
    print("Teacher added successfully!\n")


def add_course():
    code = input("Enter Course Code: ")
    name = input("Enter Course Name: ")
    faculty = input("Enter Faculty Name: ")

    c = Course(code, name, faculty)
    courses_list.append(c)
    print("Course added successfully!\n")


def show_all_students():
    if not students_list:
        print("No students found.\n")
        return
    for s in students_list:
        s.show_details()


def show_all_teachers():
    if not teachers_list:
        print("No teachers found.\n")
        return
    for t in teachers_list:
        t.show_details()


def show_all_courses():
    if not courses_list:
        print("No courses found.\n")
        return
    for c in courses_list:
        c.show_course()


# MAIN MENU
print("----- UNIVERSITY MANAGEMENT SYSTEM -----")

while True:
    print("""
1. Add Student
2. Add Teacher
3. Add Course
4. Show All Students
5. Show All Teachers
6. Show All Courses
7. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        add_teacher()
    elif choice == 3:
        add_course()
    elif choice == 4:
        show_all_students()
    elif choice == 5:
        show_all_teachers()
    elif choice == 6:
        show_all_courses()
    elif choice == 7:
        print("Exiting System...")
        break
    else:
        print("Invalid choice! Please select again.\n")

        
