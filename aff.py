# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# aff.py file - helper functions for affiliate routes

import cs304dbi as dbi 


def get_affiliate(conn,username):
   #Set up connection.
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, welles_affiliates.gpa, welles_affiliates.org1, 
                     welles_affiliates.org2,welles_affiliates.org3, user.name from  welles_affiliates inner join user using (username) where username=%s''', [username])
    return curs.fetchone()

def get_affiliates(conn,name):
   #Set up connection.
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, welles_affiliates.gpa, welles_affiliates.org1, 
                     welles_affiliates.org2,welles_affiliates.org3, user.name  from  welles_affiliates inner join user using (username) where user.name like %s''', ['%' + name + '%'])
    return curs.fetchall()

def get_all_affiliates(conn):
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, user.name from welles_affiliates inner join user using (username) order by name asc''')
    return curs.fetchall()

def get_experience(conn,username): 
    #Create cursor to pull data from the user table.
    curs = dbi.dict_cursor(conn)
    curs.execute(''' select experience.username,experience.jid, experience.comp_id, company.comp_name from experience inner join company using (comp_id) where username=%s''', [username])
    return curs.fetchall()

def get_password(conn,username): 
    #Create cursor to pull data from the user table.
    curs = dbi.dict_cursor(conn)
    curs.execute(''' select passwd from user where username=%s''', [username])
    return curs.fetchone()