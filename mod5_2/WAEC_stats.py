from functools import total_ordering
from pydoc import describe
import sqlite3
from unicodedata import name

#Connect to Database
conn = sqlite3.connect("WAECscores.db")

print("connected successfully")

#Create Cursor
cursor = conn.cursor()

print("Cursor connected successfully")


# #Query items From Scores Database
cursor.execute("""SELECT * FROM waec_scores""")

items = cursor.fetchall()
print(items)


# #Student with highest score in Maths
def max_maths():
    cursor.execute("SELECT WAEC_ID,MAX(Maths) FROM waec_scores")
    items = cursor.fetchall()
    for i in items:
        print("The Student with the highest score in Maths is",i[1],  " with the Score of",i[1], "\n"f"{'-'*100}")
max_maths()

#Which Student Scored Lowest in English
def min_english():
    cursor.execute("SELECT WAEC_ID,MIN(English) FROM waec_scores")
    items = cursor.fetchall()
    for i in items:
        print("The Student with the Least Score in English is "+i[0]+" with the Score of",i[1], "\n"f"{'.'*120}")
    
min_english()

#Average score of Students in Maths
def avg_math():
    cursor.execute("SELECT AVG(Maths) FROM waec_scores")
    items = cursor.fetchall()
    for i in items:
        print("Average Score of Students in Maths is ",i[0], "\n"f"{'.'*120}")
avg_math()

# Average Score of Student in English
def avg_english():
    cursor.execute("SELECT AVG(English) FROM waec_scores")
    items = cursor.fetchall()
    for i in items:
        print("Average Score of Students in English is ",i[0], "\n"f"{'.'*120}")
avg_english()

# Best Performing Student in across all nine subjects in terms of overall scores
def best_overall():
    cursor.execute("""
    SELECT name,
    SUM(Maths+English+Accounting+Commerce+Biology+Economics+Furthermaths+Yoruba+Literature)
    AS total
    FROM waec_scores
    GROUP BY WAEC_ID
    ORDER BY total DESC
    LIMIT 1
    """)
    items = cursor.fetchall()
    for i in items:
        print("Best Overall Performing Student "+i[0]+" with the Aggregate Score of",i[1], " in all nine Subjects welldone!" "\n"f"{'.'*120}")
best_overall()

#  Best Performing Student in across all nine subjects in terms of average scores
def best_avg():
    cursor.execute("""
    SELECT name,
    AVG(aths+English+Accounting+Commerce+Biology+Economics+Furthermaths+Yoruba+Literature)
    AS average
    FROM waec_scores
    GROUP BY name
    ORDER BY average DESC
    LIMIT 3 
    """)
    items = cursor.fetchall()
    for i in items:
        print("Best Overall Average Student "+i[0]+" with the Average Score of",i[1], " in all nine Subjects Keep Growing!" "\n"f"{'.'*120}")
    
best_avg()

# could use LIMIT 1 but it is most likely going to fall on the Top student, using LIMIT 3 gives us an idea of The Average Students in the Class

# # commit the changes
# conn.commit()

# # close the connection
# conn.close()