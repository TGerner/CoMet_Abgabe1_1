-- SQLite
CREATE TABLE IF NOT EXISTS tab1 (
test INTEGER,
testid INTEGER,
FOREIGN KEY (testid) REFERENCES bsdb2(id)
);