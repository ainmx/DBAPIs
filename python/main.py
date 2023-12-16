import psycopg2, mysql.connector

# PostgreSQL
connection = psycopg2.connect(
                                database = "hstestdb",
                                host = "localhost",
                                user = "hsdb",
                                password = "hsdbpass",
                                port = 5432 )

cursor = connection.cursor()

cursor.execute("SELECT * FROM HTML")

print(cursor.fetchall())

# MySQL
connection = mysql.connector.connect(
                                database = "hstestdb",
                                host = "localhost",
                                user = "hsdb",
                                password = "hsdbpass",
                                port = 3306 )

cursor = connection.cursor()

cursor.execute("SELECT * FROM HTML")

print(cursor.fetchall())
