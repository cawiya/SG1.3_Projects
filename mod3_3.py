"""defining the parent class"""
class StuternStudents:

    def __init__(self, first, last):

        """define the class attributes"""
        self.first = first
        self.last = last
        self.email = first + last + "@stutern.com"

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_email(self):
        return self.email

    def set_first(self, first_name):
        self.first = first_name

    def set_last(self, last_name):
        self.last = last_name

    def set_email(self, email):
        self.email =email 

    def __str__(self):
        """print full name"""
        return str(self.first) + " " + str(self.last)

    """define the subclass"""
class Groupleader(StuternStudents):

    def __init__(self, first, last, student=[]):

        """defining the class attributes & methods"""

        super().__init__(first, last)
        self.student = student

        if student is []:
            self.student = []
            print(self.student)

    def add_students(self, new_student):
        self.student(self, new_student)
        print(self.student)

    def remove_students(self, old_student):
        self.student.remove(old_student)
        print(self.student)

    def __str__(self):
        return str(self.student)

# creating five instances of the parent class
student1 = StuternStudents("Tawakalitu","Awonaike")
student2 = StuternStudents("Christian","Uzondu")
student3 = StuternStudents("Bukola","Ajayi")
student4 = StuternStudents("Cynthia","Awiye")
student5 = StuternStudents("Tina","Uyanide")

# getting the first name, last name and email of student1 in the parent class
print(student1.get_first())
print(student1.get_email())

#creating two instances of a subclass
leader1 = Groupleader("Temitope","Bamidele")
leader2 = Groupleader("Adedoyin","Abass")

#adding two students to leader1
new_student1 = ("Abubakar", "Adisa")
new_student2 = ("Theresa", "Karamor")

# add 2 students to leader2
new_student3 = ("Sheriff", "Azeez")
new_student4 = ("Placidus", "Ali")

# calling the add_student method for the two instances of the subclass
leader1.add_students(new_student1)
leader1.add_students(new_student2)
leader2.add_students(new_student3)
leader2.add_students(new_student4)

# remove students from the two instances of the subclass
leader1.remove_students(new_student2)
leader2.remove_students(new_student4)

# print email of the instances of the subclass
print(leader1.get_email())
print(leader2.get_email())
