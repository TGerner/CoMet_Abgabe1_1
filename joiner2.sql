SELECT MAX(temperature_table.mean_temperature) AS hoechste_mittlere_temperatur,
main_table.*, temperature_table.mean_temperature, temperature_table.tid, station_table.SID, station_table.Bezeichnung
FROM main_table
JOIN station_table ON main_table.station = station_table.SID
JOIN temperature_table ON main_table.station = temperature_table.tid
WHERE temperature_table.mean_temperature <> 'NA'
AND main_table.station = 35;