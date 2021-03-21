# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# comp.py file - helper functions for company routes

import cs304dbi as dbi

def get_company(conn,comp_id):
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select company.comp_name,company.comp_id, company.locations, company.iid, industry.ind_name 
    from company inner join industry using(iid) where comp_id = %s''', [comp_id])
    return curs.fetchone()

def get_allcompanies(conn,comp_name):
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute('''select company.comp_name, company.locations,company.comp_id, company.iid, industry.ind_name 
    from company inner join industry using(iid) where lower(comp_name) like  %s''', ['%'+ comp_name.lower() + '%'])
    return curs.fetchall()

def get_rep(conn,comp_id):
    curs = dbi.dict_cursor(conn)
    curs.execute("select * from company_rep where comp_id=%s", [comp_id])
    return curs.fetchall()
