#Similar to Midterm Final Class Diagram Question

#Parent Class
class School:
    def __init__(self, name):
        self.name = name
        self.students = []  # List to store student names
        self.courses = []   # List to store course names

    def search_by_name(self, name):
        """Search for a student by name."""
        if name in self.students:
            return name
        return None

    def add_student(self, name):
        """Add a student to the school."""
        if name not in self.students:
            self.students.append(name)
            print(f"Student '{name}' added to {self.name}.")
        else:
            print(f"Student '{name}' already exists in {self.name}.")

    def add_course(self, course_name):
        """Add a course to the school."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"Course '{course_name}' added to {self.name}.")
        else:
            print(f"Course '{course_name}' already exists in {self.name}.")

#Inherits School attributes
class Course(School):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school  # Connect the course to a specific school

    def register_student(self, student_name):
        """Register a student for this course."""
        if student_name in self.school.students:
            if student_name not in self.students:
                self.students.append(student_name)
                print(f"Student '{student_name}' registered for course '{self.name}'.")
            else:
                print(f"Student '{student_name}' is already registered for course '{self.name}'.")
        else:
            print(f"Student '{student_name}' does not exist in {self.school.name}.")

#Connected to a school, but uses composition 
#e.g. a student belongs in a school and enrolls in courses
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school  # Connect the student to a specific school
        self.courses = []     # List to store courses the student is enrolled in

    def enroll_in_course(self, course):
        """Enroll the student in a course."""
        if course.name in self.school.courses:
            if course.name not in self.courses:
                self.courses.append(course.name)
                course.register_student(self.name)
            else:
                print(f"Student '{self.name}' is already enrolled in course '{course.name}'.")
        else:
            print(f"Course '{course.name}' does not exist in {self.school.name}.")