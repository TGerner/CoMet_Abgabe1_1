SELECT HauptTabelle.Id, StationID
FROM HauptTabelle
JOIN StationTabelle ON HauptTabelle.StationID = StationTabelle.StationID;