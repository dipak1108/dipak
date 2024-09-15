
# Module Import
import mariadb
import sys

# Instantiate Connection
try:
   conn = mariadb.connect(
      host="127.0.0.1",
      port=3306,
      user="root",
      password="",
      database='duckburg',
   )
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")
   sys.exit(1)

def get_data(ident):
   try:
      cursor = conn.cursor()
      statement = "SELECT name,municipality,iso_country,continent FROM airport WHERE ident=%s"
      data = [ident]
      cursor.execute(statement, data)
      for x in cursor:
         print("Successfully retrieve ident",x)
   finally:
      print("finallyident" )
code= input("Enter icao code: ")
get_data(code)
conn.close()
