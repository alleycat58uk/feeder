import sql_mdb as mdb


cnx = mdb.open_connection()
cur = cnx.cursor()
cur.execute("SELECT * FROM organisations")

for result in cur:
	print(result)

mdb.close_connection(cnx)
