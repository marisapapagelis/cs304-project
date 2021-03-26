



def update_job(conn,jid,title,educ,gpa,skills,status,link): 
    curs = dbi.dict_cursor(conn)
    j = curs.execute('''update jobs set title = %s,educ = %s,gpa = %s, skills = %s, status = %s, link = %s where jid=%s''',
                        [title,qual1,qual2,qual3,job_status,app_link])
    conn.commit() #committing updated changes to database
    return j #returns number of rows affected by update query


#deletes the job from database given its jid
def delete_job(conn,jid):
    curs = dbi.dict_cursor(conn)
    #deleting job from job table where jid is the jid of the job we want to delete
    j = curs.execute('''delete from jobs where jid=%s''', [jid]) 
    conn.commit()
    return j #returns number of rows affected by delete query above