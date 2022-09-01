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

#Create an inventory Table that has 10 items with their cost price,quantity in stock. Give each item an ID
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


#Amount The Business OWner invested in the procurement of the items
def invested_amount():
    query ="""
    SELECT SUM(cost_price)
    FROM stationeries;
    """
    print('The total amount(in naira) invested in the procurement of items is')
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
invested_amount()

#The Average quantity of items in stock
def avg_quantity():
    query ="""
    SELECT AVG(quantity_in_stock)
    FROM stationeries;
    """
    print('The average quantity of items in stock is')
    cursor.execute(query)
    items = cursor.fetchmany(10)
    print(items)
avg_quantity()

#The item with the least Quantity in stock
def min_quantity():
    query ="""
    SELECT name
    FROM stationeries
    WHERE quantity_in_stock = (SELECT MIN(quantity_in_stock)
    FROM stationeries)
    """
    print('The item with the least quantity in stock is')
    cursor.execute(query)
    items = cursor.fetchmany(10)
    print(items)
min_quantity()

#The item with the most Quantity in stock
def max_quantity():
    query ="""
    SELECT name
    FROM stationeries
    WHERE quantity_in_stock = (SELECT MAX(quantity_in_stock)
    FROM stationeries)
    """
    print('The item with the most quantity in stock is')
    cursor.execute(query)
    items = cursor.fetchmany(10)
    print(items)
max_quantity()




# commit to database
# conn.commit()

# close your connection
# conn.close()