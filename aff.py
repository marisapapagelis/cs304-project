# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# aff.py file - helper functions for affiliate routes

import cs304dbi as dbi 


def get_affiliate(conn,username):
    '''Returns the username, class year, major(s), gpa, student orgs, and name of an affiliate given their username'''
    conn = dbi.connect()
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, welles_affiliates.gpa, 
    welles_affiliates.org1, welles_affiliates.org2,welles_affiliates.org3, user.name from  welles_affiliates inner join user 
    using (username) where username=%s''', [username])
    return curs.fetchone()

def get_affiliates(conn,name):
    '''Returns the username, class year, major(s), gpa, student orgs, and name of an affiliate given their name name'''
   #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, welles_affiliates.gpa, welles_affiliates.org1, 
                     welles_affiliates.org2,welles_affiliates.org3, user.name  from  welles_affiliates inner join user using (username) where user.name 
                     like %s''', ['%' + name + '%'])
    return curs.fetchall()

def get_experience(conn,username): 
    '''Returns the username and associated job id(s), company id(s), and company name(s) of an associate given its username'''
    conn = dbi.connect()
    #Create cursor to pull data from the user table.
    curs = dbi.dict_cursor(conn)
    curs.execute(''' select experience.username,experience.jid, experience.comp_id, company.comp_name from experience inner join company using 
    (comp_id) where username=%s''', [username])
    return curs.fetchall()








 
