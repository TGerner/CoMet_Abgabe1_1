SELECT *
FROM main_table
LEFT JOIN StationTabelle ON main_table.station = StationTabelle.SID;
