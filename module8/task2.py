
import mariadb
import sys

# Instantiate Connection
try:
    conn = mariadb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",  # Consider using environment variables for sensitive data
        database='duckburg',
    )
except mariadb.Error as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)

def get_airport_counts(code):
    try:
        cursor = conn.cursor()
        query = """
            SELECT airport.type, COUNT(*) AS count
            FROM airport
            WHERE airport.iso_country = %s
            GROUP BY airport.type
        """
        cursor.execute(query, (code,))
        results = cursor.fetchall()

        if results:
            for airport_type, count in results:
                print(f"Type: {airport_type}, Count: {count}")
        else:
            print("No results found.")
    except mariadb.Error as e:
        print(f"Error executing query: {e}")
    finally:
        cursor.close()

code = input("Enter ICAO code: ")
get_airport_counts(code)
conn.close()

