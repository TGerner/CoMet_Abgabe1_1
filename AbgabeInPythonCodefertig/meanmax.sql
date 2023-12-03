SELECT MAX(mean_temperature) AS hoechsteMittlereTemperatur, main_table.station, 
main_table.id,
weatherconditions_table.mean_temperature, 
weatherconditions_table.wid, 
station_table.SID, 
station_table.Bezeichnung
FROM main_table
JOIN station_table ON main_table.station = station_table.SID
JOIN weatherconditions_table ON main_table.id = weatherconditions_table.wid
WHERE mean_temperature <> 'NA'
AND main_table.station = 35;