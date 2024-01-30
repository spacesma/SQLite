import sqlite3
import datetime

conn=sqlite3.connect("escuela.db")
cursor=conn.cursor()

#SQL='SELECT id FROM personas;'
SQL = 'SELECT personas.nombre, personas.fecha, estudis.estudi FROM personas LEFT JOIN estudis ON personas.id = estudis.persona_id;'
cursor.execute(SQL)

res = cursor.fetchall()

for r in res:
    print("El meu nom és:", r[0] )
    print("Vaig neixer el: ", r [1])
    print("Vaig estudiar ", r [2])
    #convertir string de temps en objecte de temps
    x=datetime.datetime.strptime(r[1], "%d-%m-%Y")
    #demana la data actual com a objecte de temps
    thisyear=datetime.datetime.now()
    #restar els anys d'avui els anys de la data de n.
    anys=thisyear.year-x.year
    print(anys)
    
conn.close()