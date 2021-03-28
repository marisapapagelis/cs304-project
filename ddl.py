

def insert_comp(conn, comp_name,iid,locations): 
 '''Inserts company into db after using the insert feature
    args: attributes of company to be displayed
    '''
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO company(comp_name,iid,locations)  
                    VALUES (%s, %s, %s);''',[comp_name,iid,locations])  #autoincrement no need for comp_id
    conn.commit()

def delete_comp(conn,comp_id)
    conn=dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from company where comp_id=%s''', [comp_id]) 
    conn.commit()

def delete_affiliate(conn,username):
    conn=dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from welles_affiliates where username=%s''', [username])   
    conn.commit()

def insert_affiliate(conn,username,year,major,gpa,org1,org2,org3):
    conn=dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO welles_affiliates (username,year,major,gpa,org1,org2,org3)
    VALUES (%s, %s, %s, %s,%s,%s,%s);''',[username,year,major,gpa,org1,org2,org3])

def delete_rep(conn,username): 
    conn=dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from company_rep where username=%s''', [username]) 
    conn.commit()

def insert_rep(conn,username,name,comp_id): 
    conn=dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO company_rep (username,name,comp_id)
    VALUES (%s, %s, %s);''',[username,name,comp_id])



def delete_user(conn,username): # works for both affiliate and rep 
    conn=dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from user where username=%s''', [username]) 
    conn.commit()

def update_comp(conn,comp_id,comp_name,iid,location): 
    curs = dbi.dict_cursor(conn)
    curs.execute('''update company set comp_name = %s,iid = %s,location = %s, where comp_id=%s''', # should they be able to update industry?
                        [comp_name,iid,locations,comp_id])
    conn.commit() #committing updated changes to database

 def insert_jobs(conn,title,qual1,qual2,qual3,job_status,app_link,comp_id,iid) 
 conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO jobs(title,qual1,qual2,qual3,job_status,app_link,comp_id,iid)
                    VALUES (%s, %s, %s, %s,%s,%s,%s,%s);''',[title,qual1,qual2,qual3,job_status,app_link,comp_id,iid]) 
    conn.commit()

def insert_user(conn,username,name,password,email): 
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO user(username,name,passwd,email)
                    VALUES (%s, %s, %s, %s);''',[username,name,password,email]) 
    conn.commit()

def update_jobs(conn,title,qual1,qual2,qual3,job_status,app_link): 
    curs = dbi.dict_cursor(conn)
    curs.execute('''update jobs set title = %s,qual1 = %s,qual2 = %s, qual3 = %s, job_status = %s, app_link = %s where jid=%s''',
                        [title,qual1,qual2,qual3,job_status,app_link])
    conn.commit() #committing updated changes to database
 

#deletes the job from database given its jid
def delete_jobs(conn,jid):
    curs = dbi.dict_cursor(conn)
    #deleting job from job table where jid is the jid of the job we want to delete
    curs.execute('''delete from jobs where jid=%s''', [jid]) 
    conn.commit()

def update_affiliate(conn,major,gpa,org1,org2,org3 ): 
    curs = dbi.dict_cursor(conn, )
    curs.execute('''update welles_affiliates set major = %s,gpa = %s,org1 = %s,org2=%s, org3=%s where username=%s''', 
                        [year,major,gpa,org1,org2,org3])
    conn.commit() #committing updated changes to database

def insert_experience(conn,username,jid,comp_id,iid,compensation):
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO experience(username,jid,comp_id,iid,compensation)
                    VALUES (%s, %s, %s, %s,%s);''',[username,jid,comp_id,iid,compensation]) 
    conn.commit()

def delete_experience(conn,username,jid)
    curs = dbi.dict_cursor(conn)    
    curs.execute('''delete from experience where username=%s and jid=%s''', [username,jid]) 
    conn.commit()
  








