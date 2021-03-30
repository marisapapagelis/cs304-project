# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# jo.py file - helper functions for job routes

import cs304dbi as dbi

def get_jobs(conn,comp_id):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''select company.comp_name, company.comp_id as comp_id, jobs.jid, jobs.title,jobs.qual1, 
    jobs.qual2, jobs.qual3, jobs.job_status,jobs.app_link from company inner join jobs using (comp_id) where comp_id = %s''', [comp_id])
    return curs.fetchall()

def get_job(conn,jid):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''select * from jobs where jid=%s''',[jid])
    return curs.fetchone()

def get_rep(conn, jid):
    curs = dbi.dict_cursor(conn)
    curs.execute("select username from jobs where jid = %s", [jid])
    return curs.fetchone()
    
def get_compensation(conn, jid):
    curs = dbi.dict_cursor(conn)
    curs.execute("select compensation from jobs inner join experience using (jid) where jid = %s", [jid])
    return curs.fetchall()

