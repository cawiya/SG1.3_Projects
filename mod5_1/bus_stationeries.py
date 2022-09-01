#import SQLite3
import sqlite3

#Check that package is imported successfully
print('Successfully Imported module')

#create or connect to a database
conn = sqlite3.connect('Bus_stationeries.db')

#check that database has been connected succesfully
print("Bus Stationeries Database created successfully!") ; print(type(conn))

#create a cursor object that allows the execution of SQL Statements
cursor = conn.cursor()

#check that cursor is created successfully
print("Cursor created sucessfully \n", type(cursor))

# #Create an inventory Table that has 10 items with their cost price,quantity in stock. Give each item an ID
# cursor.execute("""
#                  CREATE TABLE stationeries (
#                         ID_no integer,
#                         name text,
#                         cost_price integer,
#                         quantity_in_stock integer
#                 )
# """)

# #check that it is executed successfully
# print("Stationeries table created successfully")

#insert multiple records into stationeries table

stationeries_list = [
    ("1001", "Stapler", "1000", "1200"),
    ("1002", "Punching Machine", "4500","150" ),
    ("1003", "Sticky tapes", "250", "100"),
    ("1004", "Glue", "100", "200"),
    ("1005", "Calculator", "3000", "600"),
    ("1006", "Envelope", "100", "1000"),
    ("1007", "Marker", "300", "1500"),
    ("1008", "Notepad", "500", "4000"),
    ("1009", "Note holders", "2500", "500"),
    ("1010", "Scissor", "1500", "700")
]

cursor.executemany(
    """
    INSERT INTO stationeries
    VALUES(?, ?, ?, ?)    
    """,

stationeries_list

)

#check that list has inserted successfully
print("Inserted stationeries list into bus stationeries database successfully")

cursor.execute(
    """
    SELECT * FROM stationeries
    """
)

items = cursor.fetchall()
#print(items)

#Display output in a tabular form
print("ID no" + "\t\tName" + "\t\tCost_price(NGN)" "\t\tQuantity in stock" "\n" f"{'.' * 70}")

#loop through the items
for item in items:
    ID_no, name, cost_price, quantity_in_stock = item
    print(f"{ID_no:5}         {name:16}{cost_price:15}{quantity_in_stock:15}")


#Items to restock
def restock_items():
    query = """
    SELECT name,
    CASE
    WHEN quantity_in_stock > 50 THEN 'Adequate quantity in stock'
    WHEN quantity_in_stock < 50 THEN 'Reorder level'
    ELSE 'Restock products'
    END
    FROM stationeries;
    """
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
restock_items()

# sufficient items/products from highest to lowest cost price
def sufficient_items_using_cost_price():
     query ="""
     SELECT * FROM stationeries
     WHERE quantity_in_stock > 50
     ORDER BY cost_price DESC;
     """
     cursor.execute(query)
     items = cursor.fetchall()
     print(items)
sufficient_items_using_cost_price()

#commit to database
#conn.commit()

#close your connection
#conn.close()