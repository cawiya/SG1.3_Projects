#import sqlite3
import sqlite3 

#check that the package is imported successfully
print("Successfully imported module")

#create and/or connect to a database
conn = sqlite3.connect("SGA1_3_learners.db")

#check that the database created/connected successfully
print("Database created successfully") ; print(type(conn))

#create a cursor object that allows the execution of SQL statements
cursor = conn.cursor()

#check that the cursor is created successfully
print("Cursor created successfully \n", type(cursor))


#create a table called students with four columns that accept text inputs
# cursor.execute("""
#     CREATE TABLE students(
#         first_name text,
#         last_name text,
#         email text,
#         course text
#     ) 
#  """)

#check that it is executed successfully
#print("Students table created successfully")


#insert multiple records
student_list = [
    ("Abubakar", "Adisa", "adisaabubakar@gmail.com", "Data Science"),
    ("Adebisi", "Afolabi",	"wasola.afolabi@yahoo.com", "Data Science"),
    ("Adedoyin", "Abass",	"doyinabass0@gmail.com", "Data Science"),
    ("Awonaike", "Tawakalitu",	"purpleduralumin@gmail.com", "Data Science"),  
    ("Babajide", "Adesugba",	"jide_ade@hotmail.com", "Data Science"),
    ("Bukola", "Ajayi",	"bukolam.ajayi@gmail.com", "Data Science"), 
    ("Binta", "Umar",	"ubinta63@yahoo.com", "Data Science"),
    ("Christian","Uzondu",	"uzonduchristian2@gmail.com","Data Science"),
    ("Cynthia", "Awiya",	"awiyac@yahoo.com","Data Science"),
    ("Deborah", "Olorunnishola", 	"deboraholuwatobi247@gmail.com","Data Science"),
    ("Eke", "Ihuoma",	"ihuomaeke28@gmail.com","Data Science"),
    ("Esther", "Akpanowo",	"estherakpanowo@gmail.com","Data Science"),
    ("Eniola", "Osadare", 	"dorcasosadare@gmail.com","Data Science"),
    ("Etariemi", "Louis",	"etariemilouis@gmail.com","Data Science"),
    ("Faith", "Amure",	"amuretalodabif@gmail.com","Data Science"),
    ("Ganiyat", "Shittu",	"ganiyatas@gmail.com","Data Science"),
    ("Gideon", "Uko",	"ukogideon13@gmail.com","Data Science"),
    ("Idowu", "Adesanya", 	"idsworld22@yahoo.com","Data Science"),
    ("Joyce", "Ezeonwu",	"joyceokore@gmail.com","Data Science"),
    ("Kehinde", "Orolade",	"kehindeorolade@gmail.com","Data Science"),
    ("Kafayat",  "Ibrahim", 	"kafayatadenike10@gmail.com","Data Science"),
    ("Lawrence", "Aneshimokha",	"anelawrence1@gmail.com","Data Science"), 
    ("Mariam", "Adeoti",	"adetutuadebola28@gmail.","Data Science"), 
    ("Ogechi", "Njemanze",	"ogenjemz@gmail.com","Data Science"),
    ("Omowunmi", "Awonirana",	"mowunmi11@gmail.com","Data Science"),
    ("Placidus", "Ali",	"Placidusali@gmail.com","Data Science"),
    ("Praise", "Emmanuel", 	"praiseemmanuel9ic@gmail.com","Data Science"),
    ("Prince", "Ekeocha",	"prince.ekeocha@gmail.com","Data Science"),
    ("Rasheedat", "Sikiru",	"rasheedatsikiru@gmail.com","Data Science"),
    ("Ramotallah", "Jubril",	"jubrilramotallah03@gmail.com","Data Science"),
    ("Sheriiff", "Azeez",	"SheriffOlaitan71@gmail.com","Data Science"),
    ("Stephen", "Ogungbile",	"stephenfunso@gmail.com","Data Science"),
    ("Temitope", "Bamidele",	"bamideletemitope42@gmail.com","Data Science"),
    ("Theresa", "Karamor",	"teriekarie@gmail.com","Data Science"),
    ("Tina", "Uyateide",	"tinauyats@gmail.com","Data Science"),
    ("Victoria", "Chukwuno",	"chukwunovictoria@gmail.com","Data Science"),

]


cursor.executemany(
"""
INSERT INTO students
VALUES(?, ?, ?, ?)
""",

student_list

)

#check that multiple records has been inserted
#print("Inserted multiple records at once!")

cursor.execute(
    """
    SELECT * FROM students
    """
)

items = cursor.fetchall

#print(items)

#format output to display in a tabular form
print("first_name"+ "\t Surname"+ "\t E-mail" "\t\t\t\t   Course \n"  f"{'.' * 100}")

#loop through the items
for item in items():
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email}\t\t{course}")

#commit to database
conn.commit()

#close your connection
conn.close()
