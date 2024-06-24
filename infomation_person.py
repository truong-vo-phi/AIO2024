class Student:
    def __init__(self, name, yob: int, grade: str):
        self._name = name
        self._yob = yob
        self._grade = grade
    
    def describe(self):
        print('Student - Name: {} - YoB: {} - Grade: {}'.format(self._name, self._yob, self._grade))


class Doctor:
    def __init__(self, name, yob: int, specialist: str):
        self._name = name
        self._yob = yob
        self._specialist = specialist
        
    def describe(self):
        print('Doctor - Name: {} - YoB: {} - Specialist: {}'.format(self._name, self._yob, self._specialist))


class Teacher:
    def __init__(self, name, yob: int, subject: str):
        self._name = name
        self._yob = yob
        self._subject = subject
        
    def describe(self):
        print('Teacher - Name: {} - YoB: {} - Subject: {}'.format(self._name, self._yob, self._subject))


class Ward:
    def __init__(self, name):
        self._name = name
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def describe(self):
        print('Ward Name:', self._name)
        for person in self._people:
            person.describe()


# Examples
# 2a
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologist")
doctor1.describe()
# 2b
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(doctor1)
ward1.describe()
