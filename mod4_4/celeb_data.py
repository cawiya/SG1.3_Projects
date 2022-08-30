import sqlite3

print("Successfully imported module")

conn = sqlite3.connect("celebs.db")

print("celebrity database created successfully") ; print(type(conn))

cursor = conn.cursor()

print("cursor created successfully \n", type(cursor))

# creating a table called celebs with six columns

cursor.execute("""
        CREATE TABLE celebs(
            name text,
            genre text,
            num_albums integer,
            age integer,
            awards integer,
            years_in_industry integer
        )

""")

print("celeb database created successfully")

celebs_data = [
    ("Wizkid", "Afrobeats", "4", "32", "65", "22"),
    ("2baba", "R&B", "2", "46","51", "13"),
    ("Beyonce", "R&B", "20", "40", "542", "25"),
    ("Tems", "Alte", "4", "27", "6","5"), 
    ("Davido", "Afrobeats", "8", "31","23","12"), 
    ("Jucee Froot", "Rap", "0", "28","1","10"),
    ("Moore DH", "Afrobeats","1","22","0","3"), 
    ("Monita", "Hip-hop","1", "20", "0", "1"),
    ("Nicki Minaj","Rap","7", "39", "316", "18"),
    ("Niniola", "Afrobeats","4", "35", "6", "8"),
    ("Tiwa savage", "Afropop","5", "42", "20", "26"),
    ("Qveen Herby", "R&B","5", "36", "1", "12"),
    ("Saint jhn", "Hip-hop","3", "35", "0", "12"),
    ("Saweetie", "Hip-hop","3", "29", "4", "6"),
    ("Shygirl", "Rap","4", "29", "1", "6"),
    ("Summer Walker", "Soul","2", "26", "5", "5"),
    ("SZA", "R&B","1", "32", "11", "11"),
    ("Olamide", "Hiphop","12", "33", "22", "12") ,
    ("Tierra Whack", "Rap","4", "26", "2", "11"),
    ("Dave", "Rap","2", "24", "2", "8")
]

cursor.executemany(
"""
INSERT INTO celebs
VALUES(?,?,?,?,?,?)
""",

celebs_data

)

#print("Inserted celebs_data into celebs database!")

cursor.execute(
    """
    SELECT * FROM celebs
    """
)

items = cursor.fetchall()

#print(items)

#Display in a tabular form

print("Name"+ "\t\tGenre"+ "\t\tnum_albums" "\tAge"+ "\tAwards" +"\t\tyears_in_industry \n"  f"{'.' * 100}") 

#loop through the items
for item in items:
    name, genre, num_albums, age, awards, years_in_industry = item
    print(f"{name:16}{genre:14}{num_albums:5}{age:15}{awards:10}{years_in_industry:15}")


#Most Decorated Celebrity
def most_decorated_celebrity():
        query= """
        SELECT name
        FROM celebs
        WHERE awards = (SELECT MAX(awards)
                   FROM celebs)
        """
        print(f"This is The most decorated Celebrity") 
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)
        
most_decorated_celebrity()

#Oldest Celebrity
def oldest_celebrity():
        query= """
        SELECT name
        FROM celebs
        WHERE age = (SELECT MAX(age)
                   FROM celebs)
        """
        print(f"This is the oldest Celebrity")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)
        
oldest_celebrity()

#Celebrity with the longest years in the industry
def longest_years_in_industry():
        query= """
        SELECT name
        FROM celebs
        WHERE years_in_industry = (SELECT MAX(years_in_industry)
                   FROM celebs)
        """
        print(f"This Celebrity has been in the Industry for the longest")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)

longest_years_in_industry()
        
#Celebrity with the least number of albums
def least_num_albums():
        query= """
        SELECT name
        FROM celebs
        WHERE num_albums = (SELECT MIN(num_albums)
                   FROM celebs)
        """
        print(f"This is the artist with the least albums!")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)

least_num_albums()

#Most Popular genre of music amongst all celebrities in the dataset
def most_popular_genre():
        query= """
        SELECT genre,
         COUNT(genre) AS `value_occurrence` 
         FROM celebs
         GROUP BY genre
         ORDER BY `value_occurrence` DESC
         LIMIT  1;
        """
        print(f"This is the most popular genre")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)

most_popular_genre()

#commit to database
conn.commit()

#close your connection
conn.close()