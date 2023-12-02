INSERT INTO main_table (date, station, count) 
VALUES (?, ?, ?);

INSERT INTO weatherconditions_table (wind_speed, precipitation, snowfall, snow_depth) 
VALUES (?,?,?,?);

INSERT INTO temperature_table (mean_temperature, max_temperature, min_temperature) 
VALUES (?,?,?);

INSERT INTO station_table (SID, Bezeichnung) 
VALUES (?,?);