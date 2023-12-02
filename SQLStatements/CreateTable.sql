CREATE TABLE IF NOT EXISTS bsdbneu (
        id INTEGER PRIMARY KEY,
        date DATE,
        station TEXT,
        count INTEGER,
        wind_speed FLOAT,
        precipitation DECIMAL(9,2),
        snowfall FLOAT,
        snow_depth FLOAT,
        mean_temperature INTEGER,
        max_temperature INTEGER,
        min_temperature INTEGER
);