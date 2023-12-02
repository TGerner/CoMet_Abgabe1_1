-- SQLite

-- Tabelle erstellen
CREATE TABLE bikeshareDB(
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
)

-- was passiert wenn ich die Tabelle bereits habe und ich trotzdem meinen ganzen code gleichzeitg ausführen will

-- Daten einlesen
LOAD DATA INFILE 'BikeshareDatensatz.csv' 
INTO TABLE TRANSFER
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

