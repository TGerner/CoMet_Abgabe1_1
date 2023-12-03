import sqlite3

DATABASE = "BSDB.db"

##### alle Tabellen droppen, damit diese Datei immer wieder ausgeführt werden kann, und alles damit getan ist

sql_drop_main_table = """
DROP TABLE main_table
"""
sql_drop_station_table = """
DROP TABLE station_table
"""
sql_drop_weatherconditions_table = """
DROP TABLE weatherconditions_table
"""
with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_drop_station_table)
with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_drop_weatherconditions_table)
with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_drop_main_table)
conn.close()