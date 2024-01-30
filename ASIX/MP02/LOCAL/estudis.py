import sqlite3
conexion = sqlite3.connect('escuela.db')

cursor = conexion.cursor()

SQL_estudis = 'CREATE TABLE IF NOT EXISTS estudis (id INTEGER PRIMARY KEY, estudi TEXT NOT NULL, persona_id INTEGER)'
cursor.execute(SQL_estudis) 

estudis_tipus = [
    ("Batxillerat_social", 1,),
    ("Batxillerat_cientific", 5,),
    ("GRAU", 4,),
    ("CFGM Informatica", 7,),
    ("CFGM Informatica", 8,),
    ("CFGM Farmacia", 3,),
    ("CFGM", 6,),
    ("CFGS", 2,)
]

for estudis in estudis_tipus:
    cursor.execute("INSERT INTO estudis(estudi, persona_id) VALUES(?,?)", estudis)


conexion.commit()