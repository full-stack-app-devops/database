import psycopg2

# Connect to the default database
connection = psycopg2.connect(
    dbname="mydefaultdb",
    user="myuser",
    # password="mypassword",
    host="localhost",
    port="5432"
)

# Create a cursor object
cursor = connection.cursor()

cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the list of tables
print("List of tables:")
for row in rows:
    print(row[0])

# Close the cursor and connection when you're done
cursor.close()
connection.close()
