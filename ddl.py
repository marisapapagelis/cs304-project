
# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# ddl.py file - helper functions for ddl

import cs304dbi as dbi


# COMPANY Helper functions (insert,delete,update)
def insert_comp(conn, comp_name,iid,locations): 
    '''Inserts companay name, associated industry id, and locations to the company table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO company(comp_name,iid,locations)  
                    VALUES (%s, %s, %s);''',[comp_name,iid,locations]) 
    conn.commit()

def delete_comp(conn,comp_id):
    '''Deletes all company information of a company from the company table when given 
    the associated company id'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from company where comp_id=%s''', [comp_id]) 
    conn.commit()

def update_comp(conn,comp_id,comp_name,locations): 
    '''Updates company id, company name, and locations of a company in the company table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''update company set comp_name = %s,locations = %s where comp_id=%s''', 
                        [comp_name,locations,comp_id])
    conn.commit()    


#AFFILIATE helper functions (insert,delete,update)
def delete_affiliate(conn,username):
    '''Deletes all affiliate information of a user from the welles_affiliates table 
    when given the associated username'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from welles_affiliates where username=%s''', [username])   
    conn.commit()

def insert_affiliate(conn,username,year,major,gpa,org1,org2,org3):
    '''Inserts username, year, major, gpa, and orgs of a user to the welles_affiliates
    table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO welles_affiliates (username,year,major,gpa,org1,org2,org3)
    VALUES (%s, %s, %s, %s,%s,%s,%s);''',[username,year,major,gpa,org1,org2,org3])
    conn.commit()

def update_affiliate(conn,username,major,gpa,org1,org2,org3,year):
    '''Updates the username, major, gpa, orgs, and year of an affiliate in the welles_affiliates
    table''' 
    curs = dbi.dict_cursor(conn)
    curs.execute('''update welles_affiliates set major = %s,gpa = %s,org1 = %s,org2=%s, org3=%s, 
    year=%s where username=%s''', [major,gpa,org1,org2,org3,year,username])
    conn.commit()     


# Company representitive helper functions
def delete_rep(conn,username): 
    '''Deletes all company rep information of a company rep from the company rep table when
    given the associated username'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from company_rep where username=%s''', [username]) 
    conn.commit()

def insert_rep(conn,username,name,comp_id):
    '''Inserts username, name, and company id of a company representative into the 
    company representative table''' 
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO company_rep (username,name,comp_id)
    VALUES (%s, %s, %s)''',[username,name,comp_id])
    conn.commit()

def update_rep(conn, username, name, comp_id):
    '''Updates company rep username, name, and company id in the company rep table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''update company_rep set name = %s, comp_id = %s where username=%s''',
                        [name, comp_id, username])
    conn.commit()

#USER HELPER FUNCTIONS for (INSERT ,update and  DELETE)

def user_update(conn,username,password): 
    '''Updates user password when given the associated username and new password'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''update user set passwd= %s where username=%s''',
                        [password, username])
    conn.commit()


def delete_user(conn,username): # works for both affiliate and rep
    '''Deletes user information from the user table when given the associated username''' 
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from user where username=%s''', [username]) 
    conn.commit()

def insert_user(conn,username,name,password,email): 
    '''Inserts username, name, password, and email of a user into the user table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO user(username,name,passwd,email)
                    VALUES (%s, %s, %s, %s);''',[username,name,password,email]) 
    conn.commit()

#JOB helper functions (insert,update,delete)
def insert_job(conn,title,qual1,qual2,qual3,job_status,app_link,comp_id,iid,username): 
    '''Inserts the job title, associated qualities, status, application link, company id, industry id
    and username of a job into the jobs table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO jobs(title,qual1,qual2,qual3,job_status,app_link,comp_id,iid,username)
                    VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s);''',[title,qual1,qual2,qual3,job_status,
                    app_link,comp_id,iid,username]) 
    conn.commit()

def update_job(conn,title,qual1,qual2,qual3,job_status,app_link,jid):
    '''Updates job title, qualites, status, application link, and jid of a job in the jobs table''' 
    curs = dbi.dict_cursor(conn)
    curs.execute('''update jobs set title = %s,qual1 = %s,qual2 = %s, qual3 = %s, job_status = %s, 
    app_link = %s where jid=%s''', [title,qual1,qual2,qual3,job_status,app_link,jid])
    conn.commit() 
 
def delete_job(conn,jid):
    '''Deletes a job and associated information from the job table given the job id'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from jobs where jid=%s''', [jid]) 
    conn.commit()

# Experiences  helper functions (insert,update,delete)

def insert_experience(conn,username,jid,comp_id,iid,compensation):
    '''Inserts a username, job id, company id, industry id, and compensation of a job into the 
    experience table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO experience(username,jid,comp_id,iid,compensation)
                    VALUES (%s, %s, %s, %s,%s);''',[username,jid,comp_id,iid,compensation]) 
    conn.commit()

def delete_experience(conn,username,jid):
    '''Deletes all information of an experience from the experience table when given the 
    associated username and job id'''
    curs = dbi.dict_cursor(conn)    
    curs.execute('''delete from experience where username=%s and jid=%s''', [username,jid]) 
    conn.commit()


#Helper functions for login information
  
def user_exists(conn, username):
    '''Returns the username of a user when given their username (used to check if a 
    user exists in the database)'''
    curs = dbi.dict_cursor(conn)    
    curs.execute('''select username from user where username=%s''', [username])  
    curs.fetchone()

def get_password(conn,username): 
    '''Returns the password of a user given its username'''
    curs = dbi.dict_cursor(conn)
    curs.execute(''' select passwd from user where username=%s''', [username])
    return curs.fetchone()

def is_user(username,myusername): 
    '''checks if username variable equals myusername variable'''
    return username==myusername
    

# RESUMES

def select_resume(conn,username):
    '''Returns resume information when given the associated username'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''select filename from user_resumes where username = %s''', [username])
    row = curs.fetchone()
    return row

def num_resumes(conn,username):
    '''Returns the filename of a resume when given the associated username'''
    curs = dbi.dict_cursor(conn)
    rows = curs.execute('''select filename from user_resumes where username = %s''', [username])
    return rows

def insert_resume(conn,username,filename):
    '''Inserts userrname and filename into the user_resumes table'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''INSERT INTO user_resumes (username,filename) VALUES (%s, %s) 
    on duplicate key update filename = %s;''', [username,filename,filename])
    conn.commit()

