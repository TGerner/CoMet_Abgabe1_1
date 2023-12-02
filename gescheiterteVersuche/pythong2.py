import csv
import sqlite3

def create_sqlite_database(input_file, db_file, table_name, columns_order):
    # Read the CSV file
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        data = [row for row in reader]

    # Connect to SQLite database
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Create a table in the database
    create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns_order)});"
    cursor.execute(create_table_query)

    # Insert data into the table
    insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?']*len(columns_order))});"
    cursor.executemany(insert_query, [(row[column] for column in columns_order) for row in data])

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    # Specify the input CSV file, SQLite database file, table name, and column order
    input_file_path = 'BikeshareDatensatz.csv'  # Change this to your input CSV file
    db_file_path = 'test.db'  # Change this to your desired SQLite database file path
    table_name = 'formatted_table'
    columns_order = ['date DATETIME',
        'station TEXT',
        'count INTEGER',
        'wind_speed FLOAT',
        'precipitation DECIMAL(9,2)',
        'snowfall FLOAT',
        'snow_depth FLOAT',
        'mean_temperature INTEGER',
        'max_temperature INTEGER',
        'min_temperature INTEGER']  # Change these to your column names in the desired order

    # Call the function to create an SQLite database with the formatted data
    create_sqlite_database(input_file_path, db_file_path, table_name, columns_order)

    print(f"SQLite database created and saved to {db_file_path}, table name: {table_name}")
