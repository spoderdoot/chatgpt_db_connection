import sqlite3

# Define the name of the SQLite database file
db_filename = 'gpt_organization.db'

# Establish a connection to the database (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_filename)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Read and execute the SQL script from the file
with open('create_db_structure.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database '{db_filename}' has been created and initialized.")