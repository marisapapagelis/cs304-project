
def insert_user():
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)