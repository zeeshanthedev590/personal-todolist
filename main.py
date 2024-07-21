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
      
      1. Add a todo
      2. Delete a todo
      3. Show the todos
      4. Exit''')
while True:
    options = input("your option: ")
    if options == "4":
         break
    if options == "1":
        while True:
                title = input("Enter a todo (type 'exit' to end): ")
                
                if title.lower() == 'exit':
                    break
                
                # Insert the todo item into the table using a parameterized query
                cursor.execute('''
                INSERT INTO todos (title) VALUES (?)
                ''', (title,))

    elif options == "2":
        # id = input('enter the number of the todo to be removed :')
        # cursor.execute('''
        #         DELETE FROM todos where id = (?)
        #         ''', (id,))
        try:
            id = int(input('Enter the ID of the todo to be removed: '))
            cursor.execute('''
            DELETE FROM todos WHERE id = ?
            ''', (id,))
            if cursor.rowcount == 0:
                print("No todo found with that ID.")
            else:
                print("Todo removed.")
        except ValueError:
            print("Please enter a valid number.")
    elif options == "3":
        cursor.execute('SELECT * FROM todos')
        todos = cursor.fetchall()
        print(todos)  

        

conn.commit()
conn.close()
