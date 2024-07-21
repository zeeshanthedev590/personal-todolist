import sqlite3 as sql

# Connect to a database (or create one if it doesn't exist)
conn = sql.connect("./db/data.db")


cursor = conn.cursor()

# Create the 'todos' table
with open('./sql/todos.sql', 'r') as file:
    sql_script = file.read()

# Execute the SQL script
cursor.executescript(sql_script)
print('''TODO LIST
      
      1. Add a todo (type add)
      2. Delete a todo (type delete)''')
options = input("your option: ")
if options.lower() == "add":
    while True:
            title = input("Enter a todo (type 'exit' to end): ")
            
            if title.lower() == 'exit':
                break
            
            # Insert the todo item into the table using a parameterized query
            cursor.execute('''
            INSERT INTO todos (title) VALUES (?)
            ''', (title,))

elif options.lower() == "delete":
     pass
     

conn.commit()
conn.close()
