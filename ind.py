# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# ind.py file - helper functions for industry routes

import cs304dbi as dbi 

def get_industries(conn,ind_name):
    '''Returns the industry name and id of an industry given its name.'''
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select industry.ind_name, industry.iid from industry where 
    lower(industry.ind_name) like %s''',['%' + ind_name.lower() + '%'])
    return curs.fetchall()

def get_industry(conn,iid):
    '''Returns the industry name and id of an industry given its industry id.'''
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select industry.ind_name, industry.iid from industry where iid=%s''', [iid])
    return curs.fetchone()


def get_companies(conn,iid):
    '''Returns all company information for an industry given its industry id.'''
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select * from company where iid=%s''', [iid])
    return curs.fetchall()
