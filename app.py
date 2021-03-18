from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

# one or the other of these. Defaults to MySQL (PyMySQL)
# change comment characters to switch to SQLite

import cs304dbi as dbi
# import cs304dbi_sqlite3 as dbi

import random

app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

# This gets us better error messages for certain common request errors
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

#Set this to a dummy comp_id for testing.
#comp_id of 1 corresponds to JPMorgan Chase.
comp_id=1
username_recruit='lu1'
username_welles='mars'

@app.route('/company/<comp_id>', methods=['GET', 'POST'])
def company(comp_id):
    #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs = dbi.dict_cursor(conn)
    curs.execute("select * from company where comp_id = %s", [comp_id])
    res = curs.fetchone()
    #Assign variables.
    comp_name = res['comp_name']
    iid = res['iid']
    location = res['locations']
    #Create second cursor to find industry name.
    curs1 = dbi.dict_cursor(conn)
    curs1.execute("select ind_name from industry where iid = %s", [iid])
    res1 = curs1.fetchone()
    #Assign variables.
    ind_name = res1['ind_name']

    #Create table of Company Representatives.
    curs3 = dbi.dict_cursor(conn)
    curs3.execute("select username, name from company_rep where comp_id=%s", [comp_id])
    reps_iterate = curs3.fetchall()

    if request.method == 'GET':
        return render_template('company.html', comp_id=comp_id, name=comp_name, 
                                iid=iid, location=location, ind_name=ind_name,
                                description=None, reps=reps_iterate)
    else:
        return redirect(url_for('jobs', comp_id=comp_id))

@app.route('/company/<comp_id>/jobs/')
def jobs(comp_id):
    #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the company table.
    curs4 = dbi.dict_cursor(conn)
    curs4.execute("select comp_name from company where comp_id = %s", [comp_id])
    res4 = curs4.fetchone()
    #Assign variables.
    comp_name = res4['comp_name']
    #Create table of Jobs.
    curs5 = dbi.dict_cursor(conn) 
    curs5.execute("select jid, title, qual1, qual2, qual3, app_link from jobs where comp_id=%s", [comp_id])
    jobs_iterate = curs5.fetchall()

    return render_template('jobs.html', comp_id=comp_id, name=comp_name, jobs=jobs_iterate)

@app.route('/affiliate/<username>', methods=['GET', 'POST'])
def affiliate(username):
    #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the user table.
    curs = dbi.dict_cursor(conn)
    curs.execute("select * from user where username = %s", [username])
    usernow = curs.fetchone()
    #Assign variables.
    user_name = usernow['name']
    userid = usernow['username']
    major = usernow['major']
    gpa = usernow['GPA']
    Org1= usernow['org1']
    Org2= usernow['org1']
    Org3= usernow['org1']
    #Create cursor to pull data from the experience table.
    curs1 = dbi.dict_cursor(conn)
    curs1.execute("select jid, comp_id, hire_date, end_date from experience where username = %s", [username])
    jobs = curs.fetchall()

    #Somehow get the job titles.
    #something something something

    if request.method = 'GET':
        return render_template('affiliate-page.html',  name=user_name, 
                                username=userid, org1=org1, org2=org2,org3=org3,
                                jobs=jobs, major=major, gpa=gpa)
    else: 
        return redirect(url_for('affiliate_update', username=username))

@app.route('/job/<jid>/')
def job(jid):
    #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the jobs table.
    curs = dbi.dict_cursor(conn)
    curs.execute("select * from jobs where jid = %s", [jid])
    job = curs.fetchone()
    #Assign variables.
    title = job['title']
    jid = job['jid']
    comp_id = job['comp_id']
    iid = job['iid']
    status = job['job_status']
    q1 = job['qual1']
    q2 = job['qual2']
    q3 = job['qual3']
    app = job['app_link']

    #Somehow get the company and industry names.
    #something something something

    return render_template('job-page.html', company=comp_id, industry=iid,
                            jid=jid, status=status, qual1=q1, qual2=q2,
                            qual3=q3, link=app, title=title)
  
@app.route('/rep/<username>/', methods=['GET', 'POST'])
def rep(username):
    #Set up connection.
    conn = dbi.connect()
    #Create cursor to pull data from the jobs table.
    curs = dbi.dict_cursor(conn)
    curs.execute("select * from company_rep where username = %s", [username])
    recruiter = curs.fetchone()
    #Assign variables.
    name = recruiter['name']
    comp_id = recruiter['comp_id']

    #Somehow get the company name (comp_name).
    #something something something

    return render_template('recruiter.html', name=name, comp_name=comp_id)

#For Alpha Implementation: 
#@app.route('/affiliate/<username>/update', methods=['GET', 'POST'])
#def affiliate_update(username):
    
    
@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # setting this variable to mehar's database since that is where we made the ddl
    db_to_use = 'ngoodman_db' 
    dbi.use(db_to_use)
    print('will connect to {}'.format(db_to_use))

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)
