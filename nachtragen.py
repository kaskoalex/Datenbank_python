import sqlite3
verbindung = sqlite3.connect("geburtstage.db")
zeiger = verbindung.cursor()


nachname   = "Schiller"
vorname    = "Johann Christoph Friedrich"

zeiger.execute("UPDATE personen SET vorname=? WHERE nachname=?", (vorname, nachname))
verbindung.commit()