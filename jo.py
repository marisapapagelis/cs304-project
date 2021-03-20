import cs304dbi as dbi

def get_jobs(conn,comp_id):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''select company.comp_name, company.comp_id as comp_id, jobs.jid, jobs.title,jobs.qual1, 
    jobs.qual2, jobs.qual3, jobs.job_status,jobs.app_link from company inner join jobs using (comp_id) where comp_id = %s''', [comp_id])
    return curs.fetchall()

def get_job(jid):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''select title,jid from jobs where jid=%s''',[jid])
    return curs.fetchone()
  
