# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# ind.py file - helper functions for industry routes

import cs304dbi as dbi 

def get_companies(conn,iid):
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select * from company where iid=%s''', [iid])
    return curs.fetchall()

def get_industry(conn,iid):
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select industry.ind_name, industry.iid from industry where iid=%s''', [iid])
    return curs.fetchone()

def get_industries(conn,ind_name):
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select industry.ind_name, industry.iid from industry where lower(industry.ind_name) like %s''',['%' + ind_name.lower() + '%'])
    return curs.fetchall()

def get_all_industries(conn):
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select iid, ind_name from industry where not iid=1 order by ind_name asc''')
    return curs.fetchall()
