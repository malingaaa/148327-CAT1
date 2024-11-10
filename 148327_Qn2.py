# question 2

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # assignment names and grades

    def add_assignment(self, assignment_name, grade):
        """Adds an assignment and grade to the student's record."""
        self.assignments[assignment_name] = grade

    def display_grades(self):
        """Displays all assignments and grades for the student."""
        print(f"Grades for {self.name} (ID: {self.student_id}):")
        for assignment, grade in self.assignments.items():
            print(f"  {assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # students list

    def add_student(self, student):
        """Adds a student to the instructor's course."""
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) added to the course.")

    def assign_grade(self, student_id, assignment_name, grade):
        """Assigns a grade to a student for a specific assignment."""
        student = self.find_student(student_id)
        if student:
            student.add_assignment(assignment_name, grade)
            print(f"Grade {grade} added for {student.name} on {assignment_name}.")
        else:
            print("Student not found.")

    def find_student(self, student_id):
        """Finds a student by their ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_all_students_grades(self):
        """Displays all students and their grades."""
        print(f"Course: {self.course_name}")
        for student in self.students:
            student.display_grades()

def main():    
    instructor = Instructor(name="Dr. Smith", course_name="Intro to Programming")

    while True:
        print("\nOptions:")
        print("a. Add a student")
        print("b. Assign Student Id")
        print("c. Assign a grade")
        print("d. Display all students and their grades")
        print("e. Quit")

        choice = input("Choose an option (a-e): ")

        if choice == "a":
            # Add a new student
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "b":
        # Add a new student id
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "c":
            # Assign a grade to a student
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == "d":            
            instructor.display_all_students_grades()

        elif choice == "e":        
            print("Exit program.")
            break

        else:
            print("Invalid choice, try again.")

main()
