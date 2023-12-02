-- SQLite
CREATE TABLE test9(
    station TEXT,
    date DATE,
    Stockwerk INT);

INSERT INTO 
    test9 (station, date, Stockwerk)
VALUES 
    ("Bielefeld HBF", 2023-07-06, 1)
UPDATE test9 
    SET date = 2012-06-08