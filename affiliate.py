#very rough version of py file, because we need to change our tables :) 

import cs304dbi as dbi # is this what we import?
    
def get_person(conn,username):
    '''Returns the name, gpa, major, org1,org2,org3,industry for the user"
    '''

    curs = dbi.dict_cursor(conn)
    curs.execute('''select user.name, user.gpa , user.major, user.org1, user.org2,user.org3, user.industry from user where person.nm=%s''', [username]) 
    # the queries will change if we change our tables to only affiliates or do we include everything in user? We need to discuss this
    return curs.fetchone()

def get_experience(conn,jobid):
    '''Returns a dictionary with a list of jobs and job ids  of jobs a specific person has worked for " '''
    curs = dbi.dict_cursor(conn)
    #is the person including the title or the user id for their job, confused how we are going to do this. 
    curs.execute('''select job.title,job.jobid,  where jobid=%s''',[jobid])
    return curs.fetchall()


if __name__ == '__main__':
    dbi.cache_cnf()   # defaults to ~/.my.cnf
    dbi.use('ourdb') #what is our db called? 
    conn = dbi.connect()