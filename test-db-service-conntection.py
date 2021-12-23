import os
import sys
import psycopg2
from psycopg2 import OperationalError
from faker import Faker


# get the database connection details from the environment
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASS = os.getenv('DATABASE_PASS')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')

try:
    # connect to the database
    conn = psycopg2.connect(
            database=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASS,
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            )
except OperationalError as error:
    print(f"Unable to connect to the database {DATABASE_NAME} on port {DATABASE_PORT}")
    sys.exit(error)

# create a cursor object and get the database version information
cursor = conn.cursor()
cursor.execute("select version()")

# fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

# drop the employee table
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# create the employee table
sql = '''
    CREATE TABLE EMPLOYEE(
        id SERIAL,
        FIRST_NAME CHAR(60) NOT NULL,
        LAST_NAME CHAR(60) NOT NULL
    )
'''

cursor.execute(sql)

print("Table created successfully........")
conn.commit()

# close the connection to the database
conn.close()

fake = Faker()
