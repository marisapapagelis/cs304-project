from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

# one or the other of these. Defaults to MySQL (PyMySQL)
# change comment characters to switch to SQLite

import cs304dbi as dbi

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
    res= company.get_company(conn,comp_id)
    comp_name = res['comp_name']
    iid = res['iid']
    location = res['locations']
    ind_name = res['ind_name']
    reps=company.get_rep()
    if request.method == 'GET':
        return render_template('company.html', comp_id=comp_id, name=comp_name, ind_name=ind_name,
                                iid=iid, location=location, ind_name=ind_name, reps=reps)
    else:
        return redirect(url_for('jobs', comp_id=comp_id))

@app.route('/company/<comp_id>/jobs/')
def jobs(comp_id):
    jobs=jobs.get_jobs(conn,comp_id)
    comp_name = jobs['comp_name']
    jid=jobs['jid']
    title = jobs['title']
    jid = jobs['jid']
    comp_id = jobs['comp_id']
    status = jobs['job_status']
    q1 = jobs['qual1']
    q2 = jobs['qual2']
    q3 = jobs['qual3']
    app = jobs['app_link']
    #Create table of Jobs.
    return render_template('jobs.html', comp_id=comp_id, jid= jid, status=status,comp_name=comp_name, q1=q1, q2=q2, q3=q3,app_link=app)

@app.route('/affiliate/<username>', methods=['GET', 'POST'])
def affiliate(username):
    aff=affiliate.get_affiliate(conn,username)
    #Assign variables.
    # name = aff['name']
    username = aff['username']
    major = aff['major']
    gpa = aff['gpa']
    Org1= aff['org1']
    Org2= aff['org2']
    Org3= aff['org3']
    comp = aff['comp_name'] 
    #Create cursor to pull data from the experience table.
    

    if request.method = 'GET':
        return render_template('affiliate-page.html',name = name,
            username=username,gpa=gpa,major=major,org1=org1,org2=org2,org3=org3,comp=comp)
    else: 
        return redirect(url_for('affiliate_update', username=username))

@app.route('/job/<jid>/')
def job(jid):
    job=jobs.get_jobs(conn,comp_id)
    comp_name = job['comp_name']
    comp_idd = job['comp_id']
    jid=job['jid']
    title = job['title'] 
    status = job['job_status']
    getindustry=company.get_company(conn,comp_idd)
    ind_name=getindustry['ind_name']
    q1 = jobs['qual1']
    q2 = jobs['qual2']
    q3 = jobs['qual3']
    app = jobs['app_link']

    #Somehow get the company and industry names.
    #something something something

    return render_template('job-page.html', company=comp_name, industry=ind_name,
                            jid=jid, status=status, qual1=q1, qual2=q2,
                            qual3=q3, link=app, title=title)
  
@app.route('/rep/<username>/', methods=['GET', 'POST'])
def rep(username):
    rep = rep.get_rep(conn, username)
    name = rep['name']
    comp_id = rep['comp_id']

    #Somehow get the company name (comp_name).
    #something something something

    return render_template('rep.html', name=name, comp_id=comp_id)

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
