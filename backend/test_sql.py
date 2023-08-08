import psycopg2

# Get the database URL from the environment variable
DATABASE_URL = 'postgres://vpnupkvyteevaf:3dc52a6b3a59cdb655dee04110025fcc5bfac30d8f578ec183f2c328b0dddbef@ec2-34-236-199-229.compute-1.amazonaws.com:5432/dedqpuil6p7p8t'

# Connect to the database
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Create a cursor object
cur = conn.cursor()

# Execute a query to get all phone numbers from the database
cur.execute("SELECT Number FROM phone_numbers_phonenumber")

# Fetch all rows from the query result
rows = cur.fetchall()

# Loop over the rows and print each phone number
for row in rows:
    phone_number = row[0]
    print(phone_number)

# Close the cursor and connection
cur.close()
conn.close()
