import cs304dbi as dbi

def get_rep(conn,username):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute("select name, comp_id from company_rep where username = %s", [username])
    return curs.fetchall()