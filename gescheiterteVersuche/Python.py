import _sqlite3 # Q1
import pandas as pd # Q1, Q2 

conn = _sqlite3.connect('test.db') # Q1
c = conn.cursor() # Q1

"""c.execute('''CREATE TABLE bikeShareDB2(
        date DATETIME,
        station TEXT,
        count INTEGER,
        wind_speed FLOAT,
        precipitation DECIMAL(9,2),
        snowfall FLOAT,
        snow_depth FLOAT,
        mean_temperature INTEGER,
        max_temperature INTEGER,
        min_temperature INTEGER
          )'''
          )"""
bikeShareDB3 = pd.read_csv('BikeshareDatensatz.csv') # load to DataFrame
bikeShareDB3.to_sql('bikeshareDB3', conn, if_exists='append', index = False) # write to sqlite table

# Spalten trennen


# Connection trennen
c.close()
conn.close()

# Quellenverzeichnis
# Q1 - https://mungingdata.com/sqlite/create-database-load-csv-python/ - wie gehe ich mit Daten in Python um, bzw wie lese ich ein
# Q2 - https://www.youtube.com/watch?v=BPLUAKHuAYw - Python interpreter
# Q3 - https://stackoverflow.com/questions/67946868/how-do-i-install-pandas-into-visual-studio-code - pandas installation