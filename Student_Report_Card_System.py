#Build a Student Report Card System with the following features:
#- Add student details
#- Add or update grades
#- Display the report card


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            print(f"⚠️ Grade for {subject} already exists.")
        else:
            self.grades[subject] = grade
            print(f"✅ Grade added for {subject}.")

    def update_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject] = grade
            print(f"🔄 Grade updated for {subject}.")
        else:
            print(f"⚠️ Subject {subject} not found.")

    def display_report_card(self):
        print("\n" + "=" * 40)
        print("🎓 STUDENT REPORT CARD 🎓".center(40))
        print("=" * 40)
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Student ID : {self.student_id}")
        print("-" * 40)

        if not self.grades:
            print("No grades recorded.")
        else:
            print("Subjects & Grades:")
            for subject, grade in self.grades.items():
                print(f"{subject:<20} : {grade}")

        print("=" * 40)


name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
student_id = input("Enter Student ID: ")

student = Student(name, age, student_id)

while True:
    print("\n===== STUDENT MANAGEMENT MENU =====")
    print("1. Add Grade")
    print("2. Update Grade")
    print("3. Display Report Card")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        subject = input("Enter Subject Name: ")
        grade = input("Enter Grade: ")
        student.add_grade(subject, grade)

    elif choice == "2":
        subject = input("Enter Subject Name: ")
        grade = input("Enter New Grade: ")
        student.update_grade(subject, grade)

    elif choice == "3":
        student.display_report_card()

    elif choice == "4":
        print("✅ Exiting Program...")
        break

    else:
        print("❌ Invalid Choice! Please try again.")
