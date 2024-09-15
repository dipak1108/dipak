
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

def get_data(code,c2):
   try:
      cursor = conn.cursor()
      statement = "SELECT latitude_deg,longitude_deg FROM airport WHERE ident=%s"
      data = [code]
      cursor.execute(statement, data)
      for crr1 in cursor:
         print("Successfully retrieve ident",crr1)
      cursor1 = conn.cursor()
      statement1 = "SELECT  latitude_deg,longitude_deg FROM airport WHERE ident=%s"
      data2 = [c2]
      cursor1.execute(statement1, data2)
      for c1 in cursor1:
        print("Successfully retrieve ident",c1)
   finally:
      print("finallyident" )
code= input("Enter icao code: ")
code2= input("Enter icao code: ")
get_data(code,code2)
conn.close()
