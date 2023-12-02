-- SQLite
CREATE TABLE bikeshareDatensatz(
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

-- not null ist noch nicht eingefügt
