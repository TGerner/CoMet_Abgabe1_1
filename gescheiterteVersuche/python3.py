import csv
import pandas as pd
import sqlite3
from io import StringIO


#csv_data = pd.read_csv('BikeshareDatensatz.csv')
#db_file = 

def create_sqlite_database_from_csv_string(csv_data = 'BikeshareDatensatz.csv', db_file = 'test.db', table_name = 'BSDB4'):
    # Create a StringIO object to simulate a file-like object from the CSV data
    csv_file = StringIO(csv_data)

    # Read the CSV data
    reader = csv.DictReader(csv_data)

    # Connect to SQLite database
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Check if the table already exists
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Create a table in the database
        create_table_query = f"CREATE TABLE {table_name} (ID INTEGER PRIMARY KEY, date TEXT, location TEXT, count INTEGER, wind_speed REAL, precipitation REAL, snowfall INTEGER, snow_depth INTEGER, mean_temperature REAL, max_temperature REAL, min_temperature REAL);"
        cursor.execute(create_table_query)

        print(f"Table '{table_name}' created.")

    """ Check if records with the same date already exist
    existing_dates = [row[0] for row in cursor.execute(f"SELECT date FROM {table_name};").fetchall()]
    new_records = [(row['date'], row['location'], int(row['count']), float(row['wind_speed']), float(row['precipitation']), int(row['snowfall']), int(row['snow_depth']), float(row['mean_temperature']), float(row['max_temperature']), float(row['min_temperature'])) for row in reader if row['date'] not in existing_dates]

    if new_records:
        # Insert new records into the table
        insert_query = f"INSERT INTO {table_name} (date, location, count, wind_speed, precipitation, snowfall, snow_depth, mean_temperature, max_temperature, min_temperature) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.executemany(insert_query, new_records)
        print(f"{len(new_records)} new records inserted.")
    else:
        print("No new records to insert.") """

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    # Example CSV data as a string variable
    csv_data = pd.read_csv('BikeshareDatensatz.csv')
    
    """date;location;count;wind_speed;precipitation;snowfall;snow_depth;mean_temperature;max_temperature;min_temperature
    2022-01-01;18th St & Wyoming Ave NW;28;4.7;0.44;0;0;57;66;53
    """

    # Specify the SQLite database file, table name
    db_file_path = 'output_database_with_id.db'  # Change this to your desired SQLite database file path
    table_name = 'BSDB.db'

    # Call the function to create an SQLite database with the formatted data and ID column
    #create_sqlite_database_from_csv_string(csv_data, db_file_path, table_name)
