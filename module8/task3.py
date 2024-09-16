
import mariadb
import sys
from geopy.distance import geodesic


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


def get_coordinates(icao_code):
   """Fetch latitude and longitude for a given ICAO code."""
   try:
      cursor = conn.cursor()
      cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s", (icao_code,))
      result = cursor.fetchone()  # Fetch only one result
      return result  # Returns (latitude, longitude) or None
   except mariadb.Error as e:
      print(f"Error executing query: {e}")
      return None
   finally:
      cursor.close()


def calculate_distance(icao1, icao2):
   """Calculate and print distance between two ICAO codes."""
   coords1 = get_coordinates(icao1)
   coords2 = get_coordinates(icao2)

   if coords1 and coords2:
      distance = geodesic(coords1, coords2).kilometers
      print(f"Distance between {icao1} and {icao2} is {distance:.2f} km")
   else:
      print("Could not calculate distance due to missing data.")


# Main code
icao1 = input("Enter first ICAO code: ")
icao2 = input("Enter second ICAO code: ")
calculate_distance(icao1, icao2)

conn.close()
