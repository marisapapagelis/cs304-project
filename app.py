# Luiza, Nina, Marisa, Mehar 
# CS 304 Final Project
# App.py file 

from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename

app = Flask(__name__)

import cs304dbi as dbi
import comp 
import jo 
import aff 
import repre
import random
import ind
import ddl

app.secret_key = 'admin' # secret key

app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])


app.config['TRAP_BAD_REQUEST_ERRORS'] = True

# new for file upload
app.config['resumes'] = 'resumes'
app.config['MAX_CONTENT_LENGTH'] = 1*1024*1024 # 1 MB

# route to home page
@app.route('/',  methods = ['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('main.html',title='DoorToDoor')
    else: 
        return redirect(url_for('login'))

@app.route('/home/', methods = ['GET'])
def home(): 
        return render_template('home.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    conn = dbi.connect()
    if request.method == 'GET': # the get method is not working here! 
        return render_template('login.html')
    else:
        print(list(request.form.keys()))
        if request.form['submit'] == 'login':
            myusername = request.form['username']
            password=request.form['password']
            user_password = ddl.get_password(conn, myusername) ['passwd']

            if password == user_password: # check if password is correct
                is_rep = repre.is_rep(conn, myusername)
                session['username']=myusername #at this point, trustworthy value. 
                if is_rep: # check if rep
                    return redirect(url_for('rep',username=myusername))
                else:
                    return redirect(url_for('affiliate',username=myusername))
            else:
                flash('Username or Password is Incorrect. Please try again.')
                return redirect(url_for('login'))
        elif request.form['submit'] == 'signup':
            name=request.form['name']
            email=request.form['email']
            myusername=request.form['username']
            password=request.form['password']
            password2=request.form['password2']
            kind= request.form['kind']
            user_list = []
            for user in aff.get_all_affiliates(conn):
                user_list.append(user['username'])
                if myusername in user_list:
                    flash("Username already exists. Please choose another username.")
                    return redirect(url_for('login'))
                if password != password2: # check is password was re-entered correctly
                    flash('Passwords do not match. Please try again.')
                    return redirect(url_for('login'))
                else: 
                    ddl.insert_user(conn,myusername,name,password,email) # insert user
                    if kind == 'affiliate': # insert affiliate
                        ddl.insert_affiliate(conn,myusername,None,None,None,None,None,None)
                        flash('Taking you to your profile page. Please add additional information if necessary')
                        return redirect(url_for('affiliate_update', username = myusername))
                    else: 
                        ddl.insert_rep(conn,myusername,name,1) # insert rep
                        flash('Please enter your company details.')
                        return redirect(url_for('rep_update', username = myusername))

@app.route('/logout/')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   flash('You have been logged out')
   return redirect(url_for('index'))

# routes from search bar to appropriate pages
@app.route('/search/', methods = ['GET'])
def search():
    kind= request.args['kind']
    name=request.args['query']
    conn=dbi.connect()
    if kind =='company':
        # routes to company page, list, or lists no companies 
        companylist=comp.get_companies(conn,name)
        if len(companylist) == 1: 
            return redirect(url_for('company', comp_id=companylist[0]['comp_id']))
        elif len(companylist) > 1: 
            return render_template('company-list.html',companylist=companylist)
        else :
            flash('Sorry, no company with this name exists.')
            return redirect(url_for('all_companies'))
    elif kind == 'industry':
        # routes to industry page, list, or lists no industries
        industrylist=ind.get_industries(conn,name)
        if len(industrylist) == 1: 
            return redirect(url_for('industry', iid=industrylist[0]['iid']))
        elif len(industrylist) > 1: 
            return render_template('industry-list.html',industrylist=industrylist)
        else :
            flash('Sorry, no industry with this name exists.')
            return redirect(url_for('all_industries'))
    else: 
        # routes to person page, list, or lists no people
        personlist=aff.get_affiliates(conn,name)
        if len(personlist) == 1: 
            return redirect(url_for('affiliate',username=personlist[0]['username']))
        elif len(personlist) > 1: 
            return render_template('affiliate-list.html',personlist=personlist)
        else:
            flash('Sorry, no person with this name exists.')
            return redirect(url_for('all_affiliates'))

# routes to a specific industry page given an industry id
@app.route('/industry/<iid>/', methods=['GET', 'POST'])
def industry(iid):
    conn=dbi.connect()
    res = ind.get_industry(conn,iid)
    ind_name = res['ind_name']
    iid = res['iid']
    complist = ind.get_companies(conn,iid)
    return render_template('industry-page.html', iid = iid, ind_name=ind_name, complist = complist)
    
# routes to a specific company page given a company id
@app.route('/company/<comp_id>/', methods=['GET', 'POST'])
def company(comp_id):
    conn=dbi.connect()
    res= comp.get_company(conn,comp_id)
    comp_name = res['comp_name']
    iid = res['iid']
    comp_id=res['comp_id']
    location = res['locations']
    ind_name = res['ind_name']
    reps = repre.get_reps(conn,comp_id)
    if request.method == 'GET':
        return render_template('company-page.html', comp_id=comp_id, name=comp_name, iid=iid, location=location, ind_name=ind_name, reps=reps, is_rep=rep)
    else:
        return redirect(url_for('jobs', comp_id=comp_id))

# routes from a company page to a job page for that company 
@app.route('/company/<comp_id>/jobs/')
def jobs(comp_id):
    conn=dbi.connect()
    jobs=jo.get_jobs(conn,comp_id)
    comp_name=comp.get_company(conn,comp_id)['comp_name']
    return render_template('job-list.html', jobs=jobs, comp_name=comp_name) 

# routes from a companies job page to a specific job given the jobs unique ID
@app.route('/company/<comp_id>/job/<jid>/')
def job(comp_id, jid):
    conn=dbi.connect()
    com=comp.get_company(conn,comp_id)
    comp_id=com['comp_id']
    comp_name=com['comp_name']
    ind_name=com['ind_name']

    job=jo.get_job(conn,jid)
    jid=job['jid']
    title = job['title'] 
    status = job['job_status']
    q1 = job['qual1']
    q2 = job['qual2']
    q3 = job['qual3']
    app_link = job['app_link']
    
    compensation = jo.get_compensation(conn, jid)
    username = jo.get_rep(conn, jid)['username']
    myusername=session['username']
    #must implement a way to retrive myusername from sessions, if my usert true edit button visible
    if ddl.is_user(username,myusername) and repre.get_rep(conn,myusername)['comp_id']==comp_id:
        myuser = True
    else: 
        myuser = False
    # must implement a check to see if rep's username matches the session username
    # if no match, then myuser should be False, edit button doesn't appear

    return render_template('job-page.html', comp_name=comp_name, ind_name=ind_name,
                            jid=jid, status=status, q1=q1, q2=q2,comp_id=comp_id,
                            q3=q3, app_link=app_link, title=title, myuser= myuser, username=username, compensation=compensation)

# routes to an affiliates individual page given a unique username
@app.route('/affiliate/<username>/', methods=['GET', 'POST'])
def affiliate(username):
    conn=dbi.connect()
    affil=aff.get_affiliate(conn,username)
    myusername = session['username']
    #Assign variables.
    name = affil['name']
    username = affil['username']
    major = affil['major']
    gpa = affil['gpa']
    org1= affil['org1']
    org2= affil['org2']
    org3= affil['org3']
    year=affil['year']
    experiences=aff.get_experience(conn,username)
    myuser=ddl.is_user(username,myusername)
    if experiences:
        for e in experiences:
            job = jo.get_job(conn, e['jid']) #get each job based on the jid
            e['title']=job['title'] #add job title onto each experience 

    return render_template('affiliate-page.html',name = name,
        username=username,gpa=gpa,major=major,org1=org1,org2=org2,org3=org3,experiences=experiences,year=year,myuser=myuser)

# routes to company reps page given a unique username
@app.route('/rep/<username>/', methods=['GET', 'POST'])
def rep(username):
    conn=dbi.connect()
    print(session)
    myusername = session['username']
    rep = repre.get_rep(conn, username)
    name = rep['name']
    comp_id = rep['comp_id']
    comp_name = comp.get_company(conn,comp_id)['comp_name']
    myuser=ddl.is_user(username,myusername)
    return render_template('rep-page.html', username=username, name=name, comp_id=comp_id, comp_name=comp_name,myuser=myuser)

# routes to page that lists all companies included to date
@app.route('/all/companies/')
def all_companies():
    conn=dbi.connect()
    companylist = comp.get_all_companies(conn)
    return render_template('company-list.html', companylist=companylist)

# routes to page that lists all industries included to date
@app.route('/all/industries/')
def all_industries():
    conn=dbi.connect()
    industrylist = ind.get_all_industries(conn)
    return render_template('industry-list.html', industrylist=industrylist)

# routes to page that lists all affiliates included to date
@app.route('/all/affiliates/')
def all_affiliates():
    conn=dbi.connect()
    personlist = aff.get_all_affiliates(conn)
    return render_template('affiliate-list.html', personlist=personlist)

#For Alpha Implementation:

@app.route('/affiliate/<username>/update/', methods=['GET', 'POST'])
def affiliate_update(username):  
    conn = dbi.connect()
    affili= aff.get_affiliate(conn,username)
    user_password = ddl.get_password(conn, username) ['passwd']
    if request.method == 'GET':
        return render_template('update-affiliate.html', username = affili['username'], name = affili['name'], major =affili['major'],
                                gpa = affili['gpa'], org1=affili['org1'],year=affili['year'],org2=affili['org2'], org3=affili['org3'],password=user_password)      
    else: #using POST
    #requesting information inputted by user in form
        print(request.form)
        major = request.form['major']
        gpa=request.form['gpa']
        year=request.form['year']
        org1=request.form['org1']
        org2=request.form['org2']
        org3=request.form['org3']
        password=request.form['password']
        if request.form['submit'] == 'update': #if user wants to update 
            ddl.update_affiliate(conn,username,major,gpa,org1,org2,org3,year)
            ddl.user_update(conn,username,password)
            flash(" Affiliate Profile was updated succesfully!") #really think we should include affiliate name in table
            return redirect(url_for('affiliate',username=username))
        if request.form['submit'] == 'upload':
            f = request.files['myfile']
            user_filename = username
            ext = user_filename.split('.')[-1]
            filename = secure_filename('{}.{}'.format(username,ext))
            ddl.insert_resume(conn,username,f.filename)
            pathname = os.path.join(app.config['resumes'],filename)
            f.save(pathname)    
            flash('resume uploaded successfully')
            return render_template('update-affiliate.html', username = affili['username'], name = affili['name'], major = major,
                                gpa = gpa, org1=org1,year=year,org2=org2, org3=org3,password=password) 
        else:
            ddl.delete_allexperiences(conn,username) 
            ddl.delete_affiliate(conn, username) 
            ddl.delete_user(conn, username)
            flash("This Profile was deleted. We are sad to see you go. Good luck!")
            return redirect(url_for('index'))

@app.route('/affiliate/<username>/resume/')
def resume(username):
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    numrows = curs.execute(
        '''select filename from user_resumes where username = %s''',
        [username])
    if numrows == 0:
        flash('No resume for {}'.format(username))
        return redirect(url_for('affiliate_update', username = username))
    row = curs.fetchone()
    return send_from_directory(app.config['resumes'],row['filename'])

@app.route('/rep/<username>/update/', methods=['GET', 'POST'])
def rep_update(username):
    conn = dbi.connect()
    rep = repre.get_rep(conn, username)
    comps = comp.get_all_companies(conn)
    user_password=ddl.get_password(conn, username) ['passwd']
    if request.method == 'GET':
        return render_template('update-rep.html', name = rep['name'], username=username, comps=comps, password=user_password)
    else: #using POST
        #requesting information inputted by user in form
        name = request.form['name']
        comp_id = request.form['comp_id']
        password=request.form['password']
        if comp_id=='null':
            flash("Redirecting you to the company insert page.")
            return redirect(url_for('comp_insert', username=username))
        else:
            ddl.update_rep(conn,username, name, comp_id)
            ddl.user_update(conn,username,password)
            flash("Rep Profile for " + name + " was updated succesfully!")
            return redirect(url_for('rep', username=username))

@app.route('/rep/<username>/insert/company/', methods=['GET', 'POST'])
def comp_insert(username):
    conn = dbi.connect()
    inds = ind.get_all_industries(conn)
    if request.method == 'GET':
        return render_template('insert-company.html', inds = inds, username=username)
    else: #using POST
        print (request.form)
        comp_name = request.form['comp_name']
        iid = request.form['iid']
        locations = request.form['locations']
        ddl.insert_comp(conn, comp_name, iid, locations)
        flash("Company Profile (" + comp_name + ") was inserted successfully.")
        flash("Please update your company in your personal profile.")
        return redirect(url_for('rep_update', username=username))

@app.route('/rep/<username>/update/company/<comp_id>/', methods=['GET', 'POST'])
def comp_update(username, comp_id):
    conn = dbi.connect()
    c = comp.get_company(conn,comp_id)
    if request.method == 'GET':
        return render_template('update-company.html', username=username, comp_id = comp_id, comp_name = c['comp_name'], locations = c['locations'])         
    else: #using POST
        #requesting information inputted by user in form
        comp_name = request.form['comp_name']
        locations = request.form['locations']

        if request.form['submit'] == 'update': #if user wants to update 
            ddl.update_comp(conn,comp_id,comp_name,locations) 
            flash("Company Profile (" + comp_name + ") was updated succesfully!")
            return redirect(url_for('company', comp_id=comp_id))
                
        else: #if deleting job
            ddl.delete_comp(conn, comp_id) #deletes movie and checks if deleted
            flash("Company Profile (" + title + ") was deleted successfully.")
            flash('Job Posting for ' + title + ' was deleted successfully')
            return redirect(url_for('company', comp_id=comp_id))

@app.route('/rep/<username>/insert/job/', methods=['GET', 'POST'])
def job_insert(username):
    conn = dbi.connect()
    rep = repre.get_rep(conn, username)
    comp_id = rep['comp_id']
    company = comp.get_company(conn, comp_id)
    iid = company['iid']
    comp_name = company['comp_name']
    ind_name = company['ind_name']
    if request.method == 'GET': 
        # renders template for insert page
        return render_template('insert-job.html', title='Insert a Job', username=username, comp_id=comp_id, iid=iid, comp_name=comp_name,ind_name=ind_name)
    else: #if request method is POST
        # requests inputs from form 
        title = request.form['jobtitle']
        educ = request.form['educ']
        gpa = request.form['gpa']
        skills = request.form['skills']
        status = request.form['status']
        link = request.form['link']
        ddl.insert_job(conn,title,educ,gpa,skills,status,link,comp_id,iid,username)
        flash("Job (" + title + ") was inserted successfully.")
        return redirect(url_for('rep', username=username))

@app.route('/rep/<username>/update/job/<jid>/', methods=['GET', 'POST'])
def job_update(username, jid):
    conn = dbi.connect()
    job = jo.get_job(conn,jid)
    comp_id = job['comp_id']
    if request.method == 'GET':
        return render_template('update-job.html', username=username, jid=jid, title = job['title'],
                            educ= job['qual1'], gpa= job['qual2'], skills = job['qual3'], status = job['job_status'], link = job['app_link'])
        
    else: #using POST
        #requesting information inputted by user in form
        title = request.form['title']
        educ = request.form['education']
        gpa = request.form['gpa']
        skills = request.form['skills']
        status = request.form['status']
        link = request.form['link']

        if request.form['submit'] == 'update': #if user wants to update

            ddl.update_job(conn,title,educ,gpa,skills,status,link,jid)
            flash("Job Posting for " + title + " was updated succesfully!")
            return redirect(url_for('job', jid=jid, comp_id=comp_id))
        #else: if deleting job
        else: 
            ddl.delete_job(conn, jid) #deletes movie and checks if deleted
            flash('Job Posting for ' + title + ' was deleted successfully')
            return redirect(url_for('company',))
    

#For Beta Implementation:

@app.route('/affiliate/<username>/insert/experience/', methods=['GET', 'POST'])
def ex_insert(username):
    conn = dbi.connect()
    comps = comp.get_all_companies(conn)
    if request.method == 'GET': 
        return render_template('insert-ex.html', username=username, comps=comps, jobs=None)
    else:
        if request.form['submit'] == "Choose":
            comp_id = request.form['comp_id']
            jobs = jo.get_jobs(conn, comp_id)
            return render_template('insert-ex.html', username=username, comps=None, jobs=jobs)

        if request.form['submit'] == 'submit':  
            jid = request.form['jid']
            compensation = request.form['compensation']
            job = jo.get_job(conn, jid)
            comp_id = job['comp_id']
            iid = job['iid']
            ddl.insert_experience(conn,username,jid,comp_id,iid,compensation)
            flash("Experience was updated succesfully!") 
            return redirect(url_for('affiliate', username=username))

'''The extent of the update feature for experiences is the delete option.'''
@app.route('/affiliate/<username>/update/experience/', methods=['GET', 'POST'])
def ex_update(username):
    conn = dbi.connect()
    experiences = aff.get_experience(conn, username)
    if experiences: #get comp_name and job title to show up on form
        for e in experiences:
            job = jo.get_job(conn, e['jid']) #get job based on the jid
            e['title']=job['title'] #add job title onto each experience 
            c = comp.get_company(conn, e['comp_id']) #get company based on the jid
            e['comp_name'] = c['comp_name'] #add company name onto each experience 
    if request.method == 'GET': 
        return render_template('update-ex.html', username=username, experiences=experiences)
    else:
        jid = request.form['jid']
        ddl.delete_experience(conn,username,jid)
        flash("Experience was deleted succesfully.") 
        return redirect(url_for('affiliate', username=username))

@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # setting this variable to mehar's database since that is where we made the ddl
<<<<<<< HEAD
    db_to_use = 'lmiranda_db' # using Luiza's database
=======
    db_to_use = 'mpapagel_db' # using Luiza's database
>>>>>>> e48a8453bdebe28e8328d07ac55923cde60074a6
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
