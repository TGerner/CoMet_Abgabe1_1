import csv
import sqlite3

################ erstelle Tabellen nach Datenbankschema in der 2.NF

verbindung = sqlite3.connect("BSDB.db")
zeiger = verbindung.cursor()

sql_anweisung_erstelle_HauptTabelle="""
CREATE TABLE IF NOT EXISTS HauptTabelle (
'Id' INTEGER,
'Date' DATE,
'Station' TEXT,
'Count' INTEGER,
'StationFKID' INTEGER,
PRIMARY KEY (Id),
FOREIGN KEY (StationFKID) REFERENCES StationTabelle(StationID));
"""
# die HauptTabelle muss zuerst erstellt werden, und mit Id supplied werden, damit die abhängigkeiten aufhören
# in excel station austauschen durch 1 und dann später bei bedarf joinen an stationstabelle

sql_anweisung_erstelle_StationTabelle="""
CREATE TABLE IF NOT EXISTS StationTabelle (
'SID' INTEGER,
'Bezeichnung' TEXT,
PRIMARY KEY (SID));
"""
# 

sql_anweisung_erstelle_NiederschlagTabelle="""
CREATE TABLE IF NOT EXISTS NiederschlagTabelle (
'NId',
'Precipation' DECIMAL(9,2),
'Wind_speed' FLOAT,
'Snowfall' FLOAT,
'Snow_depth' FLOAT,
FOREIGN KEY (NId) REFERENCES HauptTabelle(Id)
);
"""
# 


sql_anweisung_erstelle_TemperaturTabelle="""
CREATE TABLE IF NOT EXISTS TemperaturTabelle (
'TId' INTEGER,
'Mean_temperature' INTEGER,
'Max_temperature' INTEGER,
'Min_temperature' INTEGER,
FOREIGN KEY (TId) REFERENCES HauptTabelle(Id)
);
"""
# 

zeiger.execute(sql_anweisung_erstelle_HauptTabelle)
zeiger.execute(sql_anweisung_erstelle_NiederschlagTabelle)
zeiger.execute(sql_anweisung_erstelle_StationTabelle)
zeiger.execute(sql_anweisung_erstelle_TemperaturTabelle)

################ Ende Tabellenerstellung

################ Anfang Tabellen befüllen

sql_anweisung_importiere_Daten_In_HauptTabelle="""
INSERT INTO HauptTabelle (
        Id,
        Date,
        Station,
        Count)
VALUES (
        :Id,
        :Date,
        :Station,
        :Count)
"""

sql_anweisung_importiere_Daten_In_StationTabelle="""
INSERT INTO StationTabelle (
        SID,
        Bezeichnung)
VALUES (
        :SID,
        :Bezeichnung)
"""

###############

### was passiert wenn 2x importiert werden soll, 
with open("StationTabelle.csv") as csv_HauptTabelle:
    csv_reader_object = csv.reader(csv_HauptTabelle, delimiter=',')

    with sqlite3.connect("BSDB.db") as verbindung:
        zeiger = verbindung.cursor()
        zeiger.executemany(sql_anweisung_importiere_Daten_In_HauptTabelle, csv_reader_object)


with open("StationTabelle.csv") as csv_StationTabelle:
    csv_reader_object = csv.reader(csv_StationTabelle, delimiter=',')

    with sqlite3.connect("BSDB.db") as verbindung:
        zeiger = verbindung.cursor()
        zeiger.executemany(sql_anweisung_importiere_Daten_In_StationTabelle, csv_reader_object)


######################### update funktion schreiben die alle Stationen die zahlen aus StationTabelle gibt
### das hier funktioniert ich die tabelle richtig importiert habe
sql_anweisung_Stationen_auf_Nummern_updaten="""
UPDATE HauptTabelle
SET StationFKID = 
     CASE 
        WHEN station = '10th & E St NW' THEN 1
        WHEN Bezeichnung = '10th & K St NW' THEN 2
        WHEN Bezeichnung = '10th St & Constitution Ave NW' THEN 3
        WHEN Bezeichnung = '11th & Girard St NW' THEN 4
        WHEN Bezeichnung = '11th & Kenyon St NW' THEN 5
        ELSE Bezeichnung
END;
"""


#Quellen SQL Fremdschlüsselbeziehungen 
#https://cloud.google.com/spanner/docs/foreign-keys/how-to?hl=de