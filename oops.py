# class MyClass:
#     student = "Sujeet"
    
# class_obj = MyClass()
# print("Object name : ",class_obj)
# print("value of object in class : ",class_obj.student)

# class MyClass:
#     def __init__(self, name, marks):    # constructor
#         self.name = name
#         self.marks = marks
    
# class_obj = MyClass("Sujeet")       # object created
# print("Object name : ",class_obj.name)
# print("value of object in class : ",class_obj.name)





# class attributes and object attributes

# class Student:
#     college_name = "Lovely Professional University"
#     name = "anynomus" # this name" is class atteibute -> object attributes > class attributes
        
#     def __init__(self, name, roll_no):
#         self.name = name # object attributes > class attributes
#         self.roll_no = roll_no
#         print("Adding new studnet in data base")
        

# stu = Student("Rahul", 43)
# print(stu.name,stu.roll_no)

# print(stu.college_name)  # calling with the name of the object attributes
# print(Student.college_name) # calling with the name of class attribute




#------Methods qare function that belongs to object.

# class Cricket:
#     def __init__(self, name, team_name):
#         self.name = name
#         self.team_name = team_name
        
#     def batting(self):
#         return self.name
        
#     def bowling(self):
#         return self.name

# team_players = Cricket("Dhoni","CKS")
# print("Team players : ", team_players.name)
# print("Team name :", team_players.team_name)

# print("Captain of the team is : ", team_players.name)
# print("Best bowler of the team is : ", team_players.name)

# print(team_players.bowling())
# print(team_players.batting())



# -- Question -----
# WAP to create a class that takes name and marks of 3 subject as arguments  in constructor. Then create a method to print the avreage of the marks of the students


# class StudentMarks:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def average_marks(self):
#         sum = 0
#         for avg in self.marks:
#             sum = sum + avg
#             avg_marks = sum / len(self.marks)
#         return avg_marks
    

# stu_marks = StudentMarks("Sujeet", [87, 90, 78])
# print("Student Name : ", stu_marks.name)
# print("Studentmarks : ", stu_marks.average_marks())



# ---- Static Method --------------------------------

# methods that does not use the self parameter (work at class level)
# exampe can be used

# class statc_method:
#     @staticmethod  # this decorator is used to define a static method in python
#     def without_self_keyword():
#         return "This is method without self"


# s = statc_method()
# print(s.without_self_keyword())


# -------- access specifiers (private, protected, and public) --------------------------------
# Here’s a brief overview:

# Public: Public members (variables or methods) are accessible from anywhere, both inside and outside the class.
#Protected: Protected members are indicated by a single underscore (_) prefix. 
# These are not strictly enforced as protected but are treated as a convention to suggest they should not be accessed directly outside the class or its subclasses.
# Private: Private members are indicated by a double underscore (__) prefix. 
# These are "name-mangled" to prevent direct access from outside the class, though they can still be accessed indirectly.

class Sample:
    def __init__(self):
        self.public_var = "I am Public"  # Public variable
        self._protected_var = "I am Protected"  # Protected variable
        self.__private_var = "I am Private"  # Private variable

    def public_method(self):
        print("This is a Public method")

    def _protected_method(self):
        print("This is a Protected method")

    def __private_method(self):
        print("This is a Private method")

    def access_private_method(self):
        # Accessing private method from within the class
        self.__private_method()

# Create an object of the Sample class
obj = Sample()

# Accessing public members
print(obj.public_var)  # Output: I am Public
obj.public_method()    # Output: This is a Public method

# Accessing protected members (can be accessed, but not recommended)
print(obj._protected_var)  # Output: I am Protected
obj._protected_method()    # Output: This is a Protected method

# Accessing private members (will cause an AttributeError if accessed directly)
# print(obj.__private_var)  # This will raise an AttributeError

# Access private member through name mangling (though not recommended)
print(obj._Sample__private_var)  # Output: I am Private
obj._Sample__private_method()    # Output: This is a Private method

# Accessing private members through a public method
obj.access_private_method()  # Output: This is a Private method

# ------- ------ Key Points: --------------------------------
# Public members (like public_var) can be accessed from anywhere.
# Protected members (like _protected_var) can be accessed but are conventionally meant to be used only within the class or subclasses.
# Private members (like __private_var) cannot be directly accessed outside the class, but name mangling (_ClassName__varname) allows access indirectly. 
# This is mainly a way to prevent accidental access, not complete enforcement.




# ----- Inheritance in Python --------------------------------

