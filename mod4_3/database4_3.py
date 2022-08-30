#import SQLite3
import sqlite3

#Check that package is imported successfully
print('Successfully Imported module')

#create or connect to a database
conn = sqlite3.connect('students.db')

#check that database has been connected succesfully
print("Database created successfully!") ; print(type(conn))

#create a cursor object that allows the execution of SQL Statements
cursor = conn.cursor()

#check that cursor is created successfully
print("Cursor created sucessfully \n", type(cursor))


#create a table called students with four columns that accept text inputs
# cursor.execute("""
#                  CREATE TABLE students (
#                         first_name text,
#                         last_name text,
#                         email text
#                 )
# """)
                
#check that it is executed successfully
#print(" Students Table created successfully")

#insert multiple records 
student_data =[
    ("Will", "Johnson", "willjohnson@stutern.com"),
    ("John", "Smith", "johnsmith@stutern.com"),
    ("Katy", "Brown", "katybrown@stutern.com")
               
]

# cursor.executemany( 
# """
# INSERT INTO students
# VALUES(?, ?, ?)
# """,

# student_data

# )



# cursor.execute(
#     """
#     SELECT * FROM students
#     """
# )

#Rename the table
#cursor.execute("""
#               ALTER TABLE students
#              RENAME TO students_information;
#""")
#print("Renamed Table to students_information")

cursor.executemany( 
"""
INSERT INTO students_information
VALUES(?, ?, ?)
""",

student_data

)
# Check
print("Inserted multiple records at once!")

# Add a new column
cursor.execute("""
                ALTER TABLE students_information
                ADD COLUMN course text;
                """)
print("Column Added succesfully")

#Use the UPDATE statement to add values to the new column
cursor.execute("""
                UPDATE students_information
                SET course = "Data Science"
""")
print("Updated Values into students_information")

cursor.execute(
    """
    SELECT * FROM students_information
    """
)

items = cursor.fetchall()

#print(items)

#Format outputs to display in a tabular form
print("first_name"+ "\t Surname"+ "\t E-mail" "\t\t\t\t Course" )
print(".........."+ "\t.........."+ "\t.........."+ "\t\t\t...........")

#Loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email}\t\t{course}")

#commit to database
conn.commit()

#close your connection
conn.close()