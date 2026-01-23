import math

grade_to_points = {
   "O": 10,
   "A+": 9,
   "A": 8,
   "B+": 7,
   "B": 6,
   "C+": 5,
   "C": 4,
   "D": 3,
   "F": 0
}

class student:

   def __init__(self):
      self.__id = None
      self.name = None
      self.age = None
      self.grade = None
      self.marks = []

   def set_details(self, id=1, name="Samarth", age=23, grade="A+"):
      self.__id = id
      self.name = name
      self.age = age
      self.grade = grade
      self.marks = self.get_marks()

      # # For user input, uncomment the lines below
      # self.name = input("Enter Name: ")
      # self.age = int(input("Enter Age: "))
      # self.grade = input("Enter Grade: ")

   def get_marks(self):
      return [int(x) for x in input("Enter marks separated by space: ").split(',')]

   def grade_calculator(self):
      total_marks = sum(int(mark) for mark in self.marks)
      percentage = (total_marks / (len(self.marks) * 100)) * 100
      return math.floor(percentage)

   def get_details(self):
      return f"ID: {self.__id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade} \nPercentage: {self.grade_calculator()}%"
   
   def __del__(self):
      print(f"Student object with ID: {self.__id} is being deleted.")

s1 = student()
s1.set_details()
print(s1.get_details())
# print(s1._student__id) # Calling the private variable