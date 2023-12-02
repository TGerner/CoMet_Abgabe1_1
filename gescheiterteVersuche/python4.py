import csv
import sqlite3


verbindung = sqlite3.connect("BSDB.db")
zeiger = verbindung.cursor()

# Tabelle erstmalig erstellen falls noch nicht existent

sql_anweisung = """
CREATE TABLE IF NOT EXISTS bsdb4 (
        'id' INTEGER PRIMARY KEY,
        'date' DATE,
        'station' TEXT,
        'count' INTEGER,
        'wind_speed' FLOAT,
        'precipitation' DECIMAL(9,2),
        'snowfall' FLOAT,
        'snow_depth' FLOAT,
        'mean_temperature' INTEGER,
        'max_temperature' INTEGER,
        'min_temperature' INTEGER
);"""


# um in python sql anweisungen durchzuführen
zeiger.execute(sql_anweisung)

# einzelne Zeilen aus csv datei anzeigen lassen
with open("BikeshareDatensatz.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei, delimiter=';')
    """for row in csv_reader_object:
        print(row)"""
        

    zeiger.execute(sql_anweisung)

### Aufgabe: jedes mal wenn kompiliert wird, werden die Daten neu eingefügt, das soll natürlich nicht so
# wie verhindere ich, dass dieselben Daten mehrfach eingelesen werden?

sql_anweisung4 ="""
SELECT *
COUNT
FROM bsdb4
"""

# unseren Datensatz, übrigens bereits in excel gefiltert nach unserer Straße, einfügen in unsere Datenbank in VSC

sql_anweisung2 = """
INSERT INTO bsdb4 (
    date,
    station,
    count,
    wind_speed,
    precipitation,
    snowfall,
    snow_depth,
    mean_temperature,
    max_temperature,
    min_temperature)
VALUES (
    :date,
    :station,
    :count,
    :wind_speed,
    :precipitation,
    :snowfall,
    :snow_depth,
    :mean_temperature,
    :max_temperature,
    :min_temperature)
"""

with open("BikeshareDatensatz.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei, delimiter=';')

    with sqlite3.connect("BSDB.db") as verbindung:
        zeiger = verbindung.cursor()
        zeiger.executemany(sql_anweisung2, csv_reader_object)

# gleiche Zeile löschen (sonst werden die Spaltennamen 2x angezeigt)
# habe ich als sql file auf die Db angewendet, war so leichter
"""sql_anweisung4 = 
DELETE
FROM bsdb3 
WHERE id='1';



zeiger.execute(sql_anweisung3)
"""

# alles einmal im Terminal anzeigen
"""
zeiger.execute("SELECT * FROM bsdb2")
inhalt = zeiger.fetchall()
print(inhalt)
"""

sql_anweisung5 = """
SELECT MAX(mean_temperature)
from bsdb;
"""
inhalt2 = zeiger.fetchone()
zeiger.execute(sql_anweisung5)
print(inhalt2)

verbindung.close()