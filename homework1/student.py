"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {}

    def student_details(self):
        return print(f"Student name is {self.name}, age is {self.age}, ID is {self.id}.")

    def add_subject(self, subject, grade):
        self.subjects.update({subject: grade})
        return self.subjects

    def remove_subjects(self, subject):
        self.subjects.pop(subject)
        return self.subjects

    def view_subjects(self):
        print(f"The student {self.name} is studying {self.subjects}.")
        return self.subjects

    def calculate_marks(self):
        total_marks = sum(self.subjects.values())
        total_subjects = len(self.subjects)
        average_marks = total_marks / total_subjects
        print(f"The average mark of {self.name} is {average_marks}.")
        return average_marks


class CFGStudent(Student):
    def __init__(self, name, age, id, specialisation):
        super().__init__(name, age, id)
        self.specialisation = specialisation



cfg_student = Student('Aysha', 25, 1402)

cfg_student.student_details()
cfg_student.add_subject('Software', 99)
cfg_student.add_subject('Data', 88)
cfg_student.view_subjects()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)
