
# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# ddl.py file - helper functions for ddl

import cs304dbi as dbi
import bcrypt

# insert, delete, update COMPANIES

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

# insert, update, delete AFFILIATES

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

# insert, update, delete USERS

def user_update(conn,username,hashed2_str): 
    '''Updates user password when given the associated username and new password'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''update user set hashed= %s where username=%s''',
                        [hashed2_str, username])
    conn.commit()

def delete_user(conn,username): # works for both affiliate and rep
    '''Deletes user information from the user table when given the associated username''' 
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from user where username=%s''', [username]) 
    conn.commit() 

def insert_hashed(conn, myusername, name, hashed_str, email):
    '''Inserts username, name, hashed password, and email of a user into the user table'''
    curs = dbi.cursor(conn)
    curs.execute('''INSERT INTO user(username, name, hashed, email)
                            VALUES(%s,%s,%s,%s)''',[myusername, name, hashed_str, email])
    conn.commit()

# insert, update, delete COMPANY REPRESENTATIVES

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

def delete_rep(conn,username): 
    '''Deletes all company rep information of a company rep from the company rep table when
    given the associated username'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''delete from company_rep where username=%s''', [username]) 
    conn.commit()

# insert, update, delete JOBS

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

# insert, delete EXPERIENCE (cannot update - just delete and make a new one)

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

# Additional USER functions
  
def user_exists(conn, username):
    '''Returns the username of a user when given their username (used to check if a 
    user exists in the database)'''
    curs = dbi.dict_cursor(conn)    
    curs.execute('''select username from user where username=%s''', [username])  
    curs.fetchone()

def check_user(conn, myusername):
    '''Returns a boolean whether the user exists in the database given their username'''
    curs = dbi.dict_cursor(conn)
    user = curs.execute("select username from user where username =%s", [myusername])
    return (user == 1) # true if user exists, false otherwise

def is_user(username,myusername): 
    '''checks if username variable equals myusername variable'''
    return username==myusername

def select_hashed(conn, username):
    '''selects username and hashed password from user table given a username'''
    curs = dbi.dict_cursor(conn)
    curs.execute('''SELECT username,hashed
                      FROM user
                      WHERE username = %s''', [username])
    row = curs.fetchone()
    return row 

# RESUME functions

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

# Insert test data functions

def insert_data(conn, myusername, name, password, email):
    '''Inserts test data with hashed password into the user table'''
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_str = hashed.decode('utf-8')
    curs = dbi.cursor(conn)
    curs.execute('''INSERT INTO user(username, name, hashed, email)
                             VALUES(%s,%s,%s,%s)''',[myusername, name, hashed_str, email])
    conn.commit()


    

