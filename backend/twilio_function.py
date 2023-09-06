import psycopg2
from twilio.rest import Client


def main():
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

    # Read the contents of Chase.txt and Lenoir.txt
    with open('menus\Chase.txt', 'r') as file:
        chase_contents = file.read()
    with open('menus\Lenoir.txt', 'r') as file:
        lenoir_contents = file.read()

    # Your Account SID and Auth Token from twilio.com/console
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    # Loop over the rows and print each phone number
    for row in rows:
        phone_number = row[0]
        print(phone_number)
        message_body = f"{chase_contents}{lenoir_contents}"
        # Split the message body into chunks of 1600 characters each
        message_parts = [message_body[i:i+1600] for i in range(0, len(message_body), 1600)]
        # Send each part as a separate message
        for part in message_parts:
            message = client.messages.create(
                body=part,
                from_='+18667541467',
                to=phone_number
            )

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()