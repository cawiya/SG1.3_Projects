import sqlite3
import csv


#Create a databse connection
conn = sqlite3.connect('WAECscores.db')

#Check
print("WAEC Scores Database Created Successfully")

#Create a Cursor
cursor = conn.cursor()

#Check
print("Cursor Created Successfully")


# #Create Table called WAEC_scores that has ten columns Integer inputs
# create_table = """
# CREATE TABLE waec_scores(
#     WAEC_ID INTEGER,
#     Maths INTEGER,
#     English INTEGER,
#     Accounting INTEGER,
#     Commerce INTEGER,
#     Biology INTEGER,
#     Economics INTEGER,
#     Furthermaths INTEGER,
#     Yoruba INTEGER,
#     Literature INTEGER
# )
# """

# cursor.execute(create_table)

# #Check
# print("Table Created Successfully")

#load existing csv file
with open("WAECscores.csv", "r") as opened_file:
    read_file = csv.reader(opened_file)

    #skip the header
    next(read_file)

    cursor.executemany("""
    INSERT INTO waec_scores
    VALUES(?,?,?,?,?,?,?,?,?,?)
    """, read_file)



print("Data successfully loaded into the database table")

cursor.execute("""SELECT * FROM waec_scores""")

items = cursor.fetchall()
#print(items)

#Display output in a tabular form
print("WAEC ID", "\tMaths", "English", "Accounting", "Commerce", "Biology", "Economics", "Furthermaths", "Yoruba", "Literature" "\n" f"{'-' * 100}")

#loop through the items
for item in items:
    WAEC_ID,Maths,English,Accounting,Commerce,Biology,Economics,Furthermaths,Yoruba,Literature = item
    print(f"{WAEC_ID:5}    {Maths:5}{English:6}    {Accounting:5}       {Commerce:5} {Biology:10}   {Economics:5}   {Furthermaths:5}     { Yoruba:5}    {Literature:5}")

