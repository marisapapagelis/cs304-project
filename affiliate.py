import cs304dbi as dbi 

def get_affiliate(conn,username):
   #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the user table.
    curs = dbi.dict_cursor(conn)
    curs.execute("select welles_affiliates.username as 'username', welles_affiliates.year as 'year', welles_affiliates.major as 'major', welles_affiliates.gpa as 'gpa', welles_affiliates.org1 as 'org1', 
                     welles_affiliates.org2 as 'org2',welles_affiliates.org3 as 'org3', worked_for.comp_id as 'comp_id', company.comp_name as 'comp_name'
                     from welles_affiliates inner join worked_for using(username)
                     inner join company using (comp_id)")
    return curs.fetchone()


 
