# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# aff.py file - helper functions for affiliate routes

import cs304dbi as dbi 


def get_affiliate(conn,username):
    '''Returns the username, year, major, gpa, orgs, and name of a Wellesley affiliate
    when given their username'''
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, 
    welles_affiliates.gpa, welles_affiliates.org1, welles_affiliates.org2,welles_affiliates.org3, 
    user.name from  welles_affiliates inner join user using (username) where username=%s''', [username])
    return curs.fetchone()

def get_all_affiliates(conn, username): 
    '''Returns all affiliates and all of their information from the database'''
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select * from user''')
    return curs.fetchall()

def get_affiliates(conn,name):
    '''Returns the username, year, major, gpa, orgs, and name of all Wellesley affiliates
    containing the entered string within their name.'''
    #Create cursor to pull data from the user table
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, welles_affiliates.year, welles_affiliates.major, 
    welles_affiliates.gpa, welles_affiliates.org1, welles_affiliates.org2,welles_affiliates.org3, 
    user.name  from  welles_affiliates inner join user using (username) where user.name like %s''', ['%' + name + '%'])
    return curs.fetchall()

def get_all_affiliates(conn):
    '''Returns the username and name of all Wellesley Affiliates in the database, ascending order'''
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select welles_affiliates.username, user.name from welles_affiliates inner join user 
    using (username) order by name asc''')
    return curs.fetchall()

def get_experience(conn,username):
    '''Returns the username and all associated job id's, company id's, and company names when given
    the username of a Wellesley affiliate''' 
    #Create cursor to pull data from the user table.
    curs = dbi.dict_cursor(conn)
    curs.execute(''' select experience.username,experience.jid, experience.comp_id, company.comp_name from 
    experience inner join company using (comp_id) where username=%s''', [username])
    return curs.fetchall()

