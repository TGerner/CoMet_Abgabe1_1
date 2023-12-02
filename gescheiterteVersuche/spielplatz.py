import sqlite3
import csv

DATABASE = "BSDB.db"
SOURCE = "data.csv"



### sicherstellen das sqlite3 die foreign keys aktiviert hat
sql_activate_foreign_keys = """
PRAGMA foreign_keys = ON;
"""

### Tabellen erstellen ###
    # HauptTabelle erstellen mit den für uns wichtigsten Infos: id neu dazu, date, station und count
sql_create_table_main_table = """
CREATE TABLE IF NOT EXISTS main_table (
    'id' INTEGER PRIMARY KEY,
    'date' TEXT,
    'station' TEXT,
    'count' INTEGER,
    FOREIGN KEY(station) REFERENCES station_table(SID)
);
"""
    # Niederschlag: name ist nicht perfekt, aber egal; ID#Foreign Key, precipation, wind_speed, snowfall, snow_depth7
    # weatherconditions

sql_create_table_weatherconditions_table ="""
CREATE TABLE IF NOT EXISTS weatherconditions_table (
    'pid' INTEGER PRIMARY KEY,
    'wind_speed' DOUBLE,
    'precipitation' DECIMAL(9,2),
    'snowfall' FLOAT,
    'snow_depth' FLOAT
    );
"""

# temperature table; tid, mean , max , min    
sql_create_table_temperature_table ="""
CREATE TABLE IF NOT EXISTS temperature_table (
    'tid' INTEGER PRIMARY KEY,
    'mean_temperature' INTEGER,
    'max_temperature' INTEGER,
    'min_temperature' INTEGER
);
"""
# station table
sql_create_table_station_table =""" 
CREATE TABLE IF NOT EXISTS station_table (
'SID' INTEGER PRIMARY KEY,
'Bezeichnung' TEXT
)
"""

##### Insertion SQLite Block

sql_insert_main_table = """
INSERT INTO main_table (date, station, count) VALUES (?, ?, ?);
"""

sql_insert_weatherconditions_table = """
INSERT INTO weatherconditions_table (wind_speed, precipitation, snowfall, snow_depth) VALUES (?,?,?,?);
"""

sql_insert_temperature_table ="""
INSERT INTO temperature_table (mean_temperature, max_temperature, min_temperature) VALUES (?,?,?);
"""

sql_insert_station_table = """
INSERT INTO station_table (SID, Bezeichnung) VALUES (?,?);
"""

#### update block : main_table stationen durch zahlen ersetzen
sql_update_main_table="""
UPDATE main_table
SET station =
  CASE
    WHEN station = '10th & E St NW' THEN 1
    WHEN station = '10th & K St NW' THEN 2
    WHEN station = '10th St & Constitution Ave NW' THEN 3
    WHEN station = '11th & Girard St NW' THEN 4
    WHEN station = '11th & Kenyon St NW' THEN 5
    WHEN station = '11th & M St NW' THEN 6
    WHEN station = '11th & O St NW' THEN 7
    WHEN station = '11th & S St NW' THEN 8
    WHEN station = '12th & L St NW' THEN 9
    WHEN station = '13th & H St NE' THEN 10
    WHEN station = '13th & U St NW' THEN 11
    WHEN station = '14th & Belmont St NW' THEN 12
    WHEN station = '14th & Irving St NW' THEN 13
    WHEN station = '14th & L St NW' THEN 14
    WHEN station = '14th & Q St NW' THEN 15
    WHEN station = '14th & R St NW' THEN 16
    WHEN station = '14th & Rhode Island Ave NW' THEN 17
    WHEN station = '14th & V St NW' THEN 18
    WHEN station = '15th & M St NW' THEN 19
    WHEN station = '15th & P St NW' THEN 20
    WHEN station = '15th & W St NW' THEN 21
    WHEN station = '15th St & Constitution Ave NW' THEN 22
    WHEN station = '15th St & Pennsylvania Ave NW' THEN 23
    WHEN station = '16th & R St NW' THEN 24
    WHEN station = '17th & Corcoran St NW' THEN 25
    WHEN station = '17th & G St NW' THEN 26
    WHEN station = '17th & K St NW' THEN 27
    WHEN station = '17th & K St NW / Farragut Square' THEN 28
    WHEN station = '17th & P St NW' THEN 29
    WHEN station = '17th St & Independence Ave SW' THEN 30
    WHEN station = '17th St & Massachusetts Ave NW' THEN 31
    WHEN station = '18th & M St NW' THEN 32
    WHEN station = '18th & New Hampshire Ave NW' THEN 33
    WHEN station = '18th & R St NW' THEN 34
    WHEN station = '18th St & Wyoming Ave NW' THEN 35
    WHEN station = '1st & K St NE' THEN 36
    WHEN station = '1st & M St NE' THEN 37
    WHEN station = '1st & M St SE' THEN 38
    WHEN station = '1st & Rhode Island Ave NW' THEN 39
    WHEN station = '20th & O St NW / Dupont South' THEN 40
    WHEN station = '20th St & Florida Ave NW' THEN 41
    WHEN station = '21st & I St NW' THEN 42
    WHEN station = '21st St & G st NW' THEN 43
    WHEN station = '22nd & I St NW / Foggy Bottom' THEN 44
    WHEN station = '22nd & P ST NW' THEN 45
    WHEN station = '23rd & M St NW' THEN 46
    WHEN station = '25th St & Pennsylvania Ave NW' THEN 47
    WHEN station = '2nd St & Massachusetts Ave NE' THEN 48
    WHEN station = '37th & O St NW / Georgetown University' THEN 49
    WHEN station = '3rd & H St NE' THEN 50
    WHEN station = '3rd & M St NE' THEN 51
    WHEN station = '3rd St & Pennsylvania Ave SE' THEN 52
    WHEN station = '4th & C St SW' THEN 53
    WHEN station = '4th & Florida Ave NE' THEN 54
    WHEN station = '4th & M St SW' THEN 55
    WHEN station = '4th St & Madison Dr NW' THEN 56
    WHEN station = '5th & K St NW' THEN 57
    WHEN station = '5th St & Massachusetts Ave NW' THEN 58
    WHEN station = '6th & H St NE' THEN 59
    WHEN station = '7th & F St NW / National Portrait Gallery' THEN 60
    WHEN station = '7th & K St NW' THEN 61
    WHEN station = '7th & R St NW / Shaw Library' THEN 62
    WHEN station = '8th & H St NW' THEN 63
    WHEN station = '8th & O St NW' THEN 64
    WHEN station = 'Adams Mill & Columbia Rd NW' THEN 65
    WHEN station = 'California St & Florida Ave NW' THEN 66
    WHEN station = 'Columbia & Ontario Rd NW' THEN 67
    WHEN station = 'Columbus Circle / Union Station' THEN 68
    WHEN station = 'Connecticut Ave & R St NW' THEN 69
    WHEN station = 'Constitution Ave & 2nd St NW/DOL' THEN 70
    WHEN station = 'Convention Center / 7th & M St NW' THEN 71
    WHEN station = 'Eastern Market / 7th & North Carolina Ave SE' THEN 72
    WHEN station = 'Eastern Market Metro / Pennsylvania Ave & 8th St SE' THEN 73
    WHEN station = 'Eckington Pl & Q St NE' THEN 74
    WHEN station = 'Henry Bacon Dr & Lincoln Memorial Circle NW' THEN 75
    WHEN station = 'Jefferson Dr & 14th St SW' THEN 76
    WHEN station = 'Jefferson Memorial' THEN 77
    WHEN station = 'Lamont & Mt Pleasant NW' THEN 78
    WHEN station = 'Lincoln Memorial' THEN 79
    WHEN station = 'Lincoln Park / 13th & East Capitol St NE' THEN 80
    WHEN station = 'M St & Pennsylvania Ave NW' THEN 81
    WHEN station = 'Maine Ave & 7th St SW' THEN 82
    WHEN station = 'Maine Ave & 9th St SW' THEN 83
    WHEN station = 'Massachusetts Ave & Dupont Circle NW' THEN 84
    WHEN station = 'Metro Center / 12th & G St NW' THEN 85
    WHEN station = 'New Hampshire Ave & 24th St NW' THEN 86
    WHEN station = 'New Hampshire Ave & T St NW' THEN 87
    WHEN station = 'New Hampshire Ave & Ward Pl NW' THEN 88
    WHEN station = 'New Jersey Ave & F St NW' THEN 89
    WHEN station = 'New York Ave & 15th St NW' THEN 90
    WHEN station = 'Ohio Dr & West Basin Dr SW / MLK & FDR Memorials' THEN 91
    WHEN station = 'Park Rd & Holmead Pl NW' THEN 92
    WHEN station = 'Potomac & M St NW' THEN 93
    WHEN station = 'Rhode Island & Connecticut Ave NW' THEN 94
    WHEN station = 'Smithsonian-National Mall / Jefferson Dr & 12th St SW' THEN 95
    WHEN station = 'Thomas Circle' THEN 96
    WHEN station = 'Vermont Ave & I St NW' THEN 97
    WHEN station = 'Washington & Independence Ave SW/HHS' THEN 98
    WHEN station = 'Wisconsin Ave & O St NW' THEN 99
    WHEN station = '1st & I St SE' THEN 100
    ELSE station
END;
"""

##### funktionsblock

def safe_int(value): # hier werden NAs rausgefiltert
    try:
        return int(value)
    except ValueError:
        return None
def executerOne(sqlStatement):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(sqlStatement)

def insertion(sqlStatementCreateTable, sqlStatementInsert, col):
    with open(SOURCE) as csv_file: # csv datei muss im gleichen verzeichnis liegen
        next(csv_file) # so wird die erste Zeile mit den Spaltennamen nicht mit genommen
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(sqlStatementCreateTable)

        if col == "dsc": # date, station, count : Main Tabelle
            for line in csv_file:
                try:
                    row = line.replace('"', '').strip().split(',')
                    count = safe_int(row[2])
                    cursor.execute(sqlStatementInsert, (row[0], row[1], count))
                except Exception as e:
                    print("Something wrong with:", line, "Error:", e)
        if col == "mmm": # mean_temp, max_temp, min_temp : temperatur Tabelle
            for line in csv_file:
                try:
                    row = line.replace('"', '').strip().split(',')
                    cursor.execute(sqlStatementInsert, (row[7], row[8], row[9]))
                except Exception as e:
                    print("Something wrong with:", line, "Error:", e)
        if col == "wpss": # windspeed, precipitation, snowfall, snowdepth : weathercond Tabelle
            for line in csv_file:
                try:
                    row = line.replace('"', '').strip().split(',')
                    cursor.execute(sqlStatementInsert, (row[3], row[4], row[5], row[6]))
                except Exception as e:
                    print("Something wrong with:", line, "Error:", e)
        else:
            return 0
        conn.commit()

def executerStation(sql_statement):
    with open("StationTabelle.csv") as csv_file:
            next(csv_file)
            csv_reader_object = csv.reader(csv_file, delimiter=';')
            with sqlite3.connect(DATABASE) as conn: 
                cursor = conn.cursor()
                cursor.executemany(sql_statement, csv_reader_object)

##### Abgabe abarbeiten
executerOne(sql_activate_foreign_keys) # foreignkeys aktivieren
   
##### Insertion Python Block

insertion(sql_create_table_main_table, sql_insert_main_table, "dsc") # create und insert main table
insertion(sql_create_table_weatherconditions_table, sql_insert_weatherconditions_table, "wpss") # create und insert weathercond table
insertion(sql_create_table_temperature_table, sql_insert_temperature_table, "mmm") # create und insert temp table

### dieser Block befüllt station_table

executerOne(sql_create_table_station_table)

executerStation(sql_insert_station_table)

executerOne(sql_update_main_table)

### Aufgabe 4 : für temperatur tabelle höchste mittlere temp ausgeben funktion schreiben

sql_info_max_mean_temp ="""
SELECT MAX(mean_temperature) AS hoechsteMittlereTemperatur,main_table.*, temperature_table.mean_temperature, temperature_table.tid, station_table.SID, station_table.Bezeichnung
FROM main_table
JOIN station_table ON main_table.station = station_table.SID
JOIN temperature_table ON main_table.id = temperature_table.tid
WHERE mean_temperature <> 'NA'
AND main_table.station = 35;
"""

executerOne(sql_info_max_mean_temp)


maximale_mean_temp = cursor.fetchone()

if maximale_mean_temp:
    max_temp = maximale_mean_temp[0]
    umgerechnet = (5/9) * (max_temp-32)
    print("Die höchste mittlere Temperatur beträgt:", umgerechnet)
else:
    print("Das hat leider nicht funktioniert.")
        
conn.close()

# to do Liste Code: 
# Dokumentation
# Quellen
# woher kamen die Daten
# woher kam die db

# ganz wichtig: Chloé Goupe, die das template für die LaTeX Datei geliefert hat 1.50 30.11
#https://www.overleaf.com/latex/templates/thesis-layout-upariscite/qvmbkpnxvtdn

# 29.11.23 14.38 Code ist vollständig fertig