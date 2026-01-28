import math
import dotenv
import psycopg2
import logging
from psycopg2 import sql

class my_database:
   database_name = "StudentDetails"

   def __init__(self):
      dotenv.load_dotenv()
      self.db_user = dotenv.get_key(".env", "DATABASEUSER")
      self.db_password = dotenv.get_key(".env", "DATABASEPASSWORD")
      self.host = "localhost"
      self.port = "5432" 
        
      self.create_db_if_not_exists()
      self.connection = psycopg2.connect(
         database = self.database_name,
         user = self.db_user,
         password = self.db_password,
         host = self.host,
         port = self.port
      )
      self.create_table()
        
      # Sync the student class ID counter with the DB
      student.latest_id = self.fetch_latest_id_count() + 1

   def create_db_if_not_exists(self):
      temp_conn = psycopg2.connect(
         database = "postgres", 
         user = self.db_user, 
         password = self.db_password, 
         host = self.host
      )
      temp_conn.autocommit = True
      cur = temp_conn.cursor()
      cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (self.database_name,))
      if not cur.fetchone():
         cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(self.database_name)))
         print(f"Database {self.database_name} created.")
      cur.close()
      temp_conn.close()

   def create_table(self):
      try:
         with self.connection.cursor() as cursor:
            cursor.execute("""
               CREATE TABLE IF NOT EXISTS students (
               sid INTEGER PRIMARY KEY,
               name VARCHAR(100),
               age INTEGER,
               grade VARCHAR(10),
               marks INTEGER[]
               )
            """)
            self.connection.commit()
      except Exception as e:
         logging.error(f"Error: {e}")

   def post_data(self, student_obj):
      cursor = self.connection.cursor()
      insert_query = """ INSERT INTO students (sid, name, age, grade, marks) VALUES (%s, %s, %s, %s, %s)"""
      record_to_insert = (student_obj.student_id, student_obj.name, student_obj.age, student_obj.grade, student_obj.marks)
      cursor.execute(insert_query, record_to_insert)
      self.connection.commit()
      cursor.close()
      print(f"Data for {student_obj.name} posted successfully.")

   def fetch_latest_id_count(self):
      cursor = self.connection.cursor()
      # Changed 'id' to 'sid' to match your table schema
      select_query = "SELECT COALESCE(MAX(sid), 0) FROM students"
      cursor.execute(select_query)
      result = cursor.fetchone()
      cursor.close()
      return result[0] if result else 0

class student:
   latest_id = 1 

   def __init__(self):
      self.student_id = student.latest_id
      
      # For User Input
      print(f"\n--- Entry for ID {self.student_id} ---") # So that the user knows the ID for the student
      self.name = input("Enter Student Name: ")
      self.age = int(input("Enter Student's Age: "))
      self.marks = [int(x.strip()) for x in input(f"Enter marks for {self.name} (separated by commas): ").split(',')]
      self.grade = self.grade_percentage_calculator()

      # Increment class counter so next student gets next ID
      student.latest_id += 1

   def grade_percentage_calculator(self, want_grade=True):
      if not self.marks: return 0
      total_marks = sum(self.marks)
      percentage = (total_marks / (len(self.marks) * 100)) * 100
      if want_grade:
         points = math.floor(percentage/10)
         match points:
            case 10:
                return "O"
            case 9:
                return "A+"
            case 8:
                return "A"
            case 7:
                return "B+"
            case 6:
                return "B"
            case 5:
                return "C+"
            case 4:
                return "C"
            case 3:
                return "D"
            case _:           # Covers the grade for case of 0% to 29% in marks
                return "F"
      return percentage

   def get_details(self):
      return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


if __name__ == "__main__":
   myDB = my_database()

   s1 = student()
   myDB.post_data(s1)

   s2 = student()
   myDB.post_data(s2)