import sqlite3

conn= sqlite3.connect("escuela.db")
cursor=conn.cursor()

SQL="CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, fecha TEXT)"
cursor.execute(SQL)

personas=[ 
          ("Pol", "Casta", "06-08-2004"), 
          ("Carlos", "Carbonell", "17-06-1982"),
          ("Angela", "Rodriguez", "11-10-2004"),
          ("Gerard", "Cardus", "20-04-1987"),
          ("Daniel", "Viedma", "03-05-2005"),
          ("Aleix", "Truzman", "07-12-2003"),
          ("Oriol","Mirabet", "18-10-2005"),
          ("Ramon", "Zanuy", "05-08-2000")
            ]

for p in personas:
  cursor.execute("INSERT INTO personas (nombre, apellido, fecha) VALUES (?, ?, ?)", p)

conn.commit()
conn.close()