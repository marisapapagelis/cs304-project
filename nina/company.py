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

comp_id=1

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