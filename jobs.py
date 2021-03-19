import cs304dbi as dbi

def get_jobs(conn,comp_id):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    curs.execute('''select company.comp_name, company.comp_id , jobs.jid, jobs.title,jobs.qual1, 
    jobs.qual2, jobs.qual3, jobs.app_link from company inner join jobs using (comp_id) where comp_id = %s''', [comp_id])

    return curs.fetchall()
  
