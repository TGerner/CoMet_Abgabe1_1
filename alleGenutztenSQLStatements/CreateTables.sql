CREATE TABLE IF NOT EXISTS main_table (
    'id' INTEGER PRIMARY KEY,
    'date' TEXT NOT NULL,
    'station' TEXT NOT NULL,
    'count' INTEGER,
    FOREIGN KEY(station) REFERENCES station_table(SID)
);

CREATE TABLE IF NOT EXISTS weatherconditions_table (
    'pid' INTEGER PRIMARY KEY,
    'wind_speed' DOUBLE,
    'precipitation' DECIMAL(9,2),
    'snowfall' FLOAT,
    'snow_depth' FLOAT
);

CREATE TABLE IF NOT EXISTS temperature_table (
    'tid' INTEGER PRIMARY KEY,
    'mean_temperature' INTEGER,
    'max_temperature' INTEGER,
    'min_temperature' INTEGER
);

CREATE TABLE IF NOT EXISTS station_table (
'SID' INTEGER PRIMARY KEY,
'Bezeichnung' TEXT
);