# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# comp.py file - helper functions for company routes

import cs304dbi as dbi

def get_company(conn,comp_id):
    '''Returns the company name, company id, locations and associated industry id and industry name of a 
    company when given it's comany id'''
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select company.comp_name,company.comp_id, company.locations, company.iid, industry.ind_name 
    from company inner join industry using(iid) where comp_id = %s''', [comp_id])
    return curs.fetchone()

def get_companies(conn,comp_name):
    '''Returns all matching company names, locations, company id's, industry id's of those companies, and 
    associated industry names when given a string of a company name'''
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select company.comp_name, company.locations,company.comp_id, company.iid, industry.ind_name 
    from company inner join industry using(iid) where lower(comp_name) like  %s''', ['%'+ comp_name.lower() + '%'])
    return curs.fetchall()

def get_all_companies(conn):
    '''Returns all company names and id's from the database except for the 'None' company option'''
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select comp_id, comp_name from company where not comp_id=1 order by comp_name asc''')
    return curs.fetchall()