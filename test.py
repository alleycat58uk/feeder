import sql_mdb as mdb


# test read only connection
# cnx = mdb.open_ro_connection()
#
# cur = cnx[1]
# con = cnx[0]
#
# cur.execute("SELECT * FROM organisations")
#
# for result in cur:
# 	print(result)
#
# mdb.close_connection(con)

# test read write connection
cnx = mdb.open_rw_connection()

cur = cnx[1]
con = cnx[0]

cur.execute("INSERT INTO locations (place, type) VALUES ('United Kingdom', 'Country')")
cur.execute("INSERT INTO organisations (short_name, name, state_funded, location_id) \
			VALUES ('BBC', 'British Broadcasting Corporation', 'Y', 1)")

con.commit()

mdb.close_connection(con, cur)
