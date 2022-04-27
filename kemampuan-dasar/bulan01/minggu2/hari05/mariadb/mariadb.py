# Module Imports
from colorama import Cursor
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
    user="db_user",
    password="db_user_passwd",
    host="192.0.2.1",
    port=3306,
    database="employees"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# cur.execute(
#     "SELECT first_name,last_name FROM employees WHERE first_name=?", 
#     (first_name,))


# Print Result-set
for (first_name, last_name) in cur:
    print(f"First Name: {first_name}, Last Name: {last_name}")


Cursor.execute(
    "INSERT INTO employees (first_name,last_name) VALUES (?, ?)", 
    (first_name, last_name))


# Disable Auto-Commit
conn.autocommit = False


try:
    Cursor.execute("some MariaDB query")
except mariadb.Error as e:
    print(f"Error: {e}")


#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="db_user",
    password="db_user_passwd",
    host="localhost",
    database="employees")
cur = conn.cursor() 

#retrieving information 
some_name = "Georgi" 
cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,)) 

for first_name, last_name in cur: 
    print(f"First name: {first_name}, Last name: {last_name}")
    
#insert information 
try: 
    cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()



