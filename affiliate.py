import cs304dbi as dbi 

def get_affiliate(conn,username):
   #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, welles_affiliates.gpa, welles_affiliates.org1, 
                     welles_affiliates.org2,welles_affiliates.org3 where username=%s''' [username])
    return curs.fetchone()

def get_affiliates(conn,name):
   #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, welles_affiliates.gpa, welles_affiliates.org1, 
                     welles_affiliates.org2,welles_affiliates.org3 where lower(name) like %s''' ['%' + name.lower() + '%'])
    return curs.fetchall()

def get_experience(conn,username): 
    conn = dbi.connect()
    #Create cursor to pull data from the user table.
    curs = dbi.dict_cursor(conn)
    curs.execute(''' select experience.username, experience.jid, experience.comp_id, company.comp_name from experience left outer join company where username=%s''' [username]



 
