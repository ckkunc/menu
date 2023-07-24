import sqlite3

# Connect to the database
conn = sqlite3.connect('backend/django/db.sqlite3')
c = conn.cursor()

# Query the database
c.execute('SELECT * FROM phone_numbers_phonenumber')
data = c.fetchall()

# Loop through the data
for row in data:
    print(row[1])

# Close the database connection
conn.close()
