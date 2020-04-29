# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = scoreboard.py
# __version__   = v_0.1

# Import Module
import os, sqlite3

# Falls keine Datenbankdatei vorhanden: erzeugen
if not os.path.exists("scoreboard.db"):
    con = sqlite3.connect("scoreboard.db")
    cursor = con.cursor()
    sql = "CREATE TABLE zahlenraten(name TEXT, versuche INTEGER , secret INTEGER)"
    cursor.execute(sql)
    con.close()

# Datensatz in DB schreiben
con = sqlite3.connect("scoreboard.db")
cursor = con.cursor()
sql = "INSERT INTO zahlenraten VALUES('" + name + "', " + i + ", " + secret + "')"

# print(sql)
cursor.execute(sql)
con.commit()
con.close()
