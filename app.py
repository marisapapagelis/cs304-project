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

app.secret_key = 'welcome' # secret key

app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])


app.config['TRAP_BAD_REQUEST_ERRORS'] = True

# route to home page
@app.route('/')
def index():
    return render_template('main.html',title='DoorToDoor')

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
            return redirect(url_for('index'))
    elif kind == 'industry':
        # routes to industry page, list, or lists no industries
        industrylist=ind.get_industries(conn,name)
        if len(industrylist) == 1: 
            return redirect(url_for('industry', iid=industrylist[0]['iid']))
        elif len(industrylist) > 1: 
            return render_template('industry-list.html',industrylist=industrylist)
        else :
            flash('Sorry, no industry with this name exists.')
            return redirect(url_for('index'))
    else: 
        # routes to person page, list, or lists no people
        personlist=aff.get_affiliates(conn,name)
        if len(personlist) == 1: 
            return redirect(url_for('affiliate',username=personlist[0]['username']))
        elif len(personlist) > 1: 
            return render_template('affiliate-list.html',personlist=personlist)
        else:
            flash('Sorry, no person with this name exists.')
            return redirect(url_for('index'))

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
    reps=repre.get_reps(conn,comp_id)
    if request.method == 'GET':
        return render_template('company-page.html', comp_id=comp_id, name=comp_name, iid=iid, location=location, ind_name=ind_name, reps=reps)
    else:
        return redirect(url_for('jobs', comp_id=comp_id))

# routes from a company page to a job page for that company 
@app.route('/company/<comp_id>/jobs/')
def jobs(comp_id):
    conn=dbi.connect()
    jobs=jo.get_jobs(conn,comp_id)
    comp_name=comp.get_company(conn,comp_id)['comp_name']
    #get username using session - pull it out from the session after they login
    #get username using session - pull it out from the session after they login
    if repre.is_rep(conn,username): #get username using session - pull it out from the session after they login
        return render_template('rep_job-list.html', jobs=jobs,comp_name=comp_name)
        if request.form.get('submit') == 'edit':
            return redirect(url_for('job_update',jid = ))
    else:
        return render_template('job-list.html', jobs=jobs,comp_name=comp_name) 

# routes from a companies job page to a specific job given the jobs unique ID
@app.route('/company/<comp_id>/job/<jid>/')
def job(comp_id,jid):
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

    return render_template('job-page.html', comp_name=comp_name, ind_name=ind_name,
                            jid=jid, status=status, q1=q1, q2=q2,comp_id=comp_id,
                            q3=q3, app_link=app_link, title=title)

# routes to an affiliates individual page given a unique username
@app.route('/affiliate/<username>', methods=['GET', 'POST'])
def affiliate(username):
    conn=dbi.connect()
    affil=aff.get_affiliate(conn,username)
    #Assign variables.
    name = affil['name']
    username = affil['username']
    major = affil['major']
    gpa = affil['gpa']
    org1= affil['org1']
    org2= affil['org2']
    org3= affil['org3']
    experiences=aff.get_experience(conn,username)

    if experiences:
        for e in experiences:
            job = jo.get_job(conn, e['jid']) #get each job based on the jid
            e['title']=job['title'] #add job title onto each experience 

    return render_template('affiliate-page.html',name = name,
        username=username,gpa=gpa,major=major,org1=org1,org2=org2,org3=org3,experiences=experiences)

# routes to company reps page given a unique username
@app.route('/rep/<username>/', methods=['GET', 'POST'])
def rep(username):
    conn=dbi.connect()
    rep = repre.get_rep(conn, username)
    name = rep['name']
    comp_id = rep['comp_id']
    comp_name = comp.get_company(conn,comp_id)['comp_name']
    return render_template('rep-page.html', name=name, comp_id=comp_id, comp_name=comp_name)

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

#@app.route('/affiliate/<username>/update/', methods=['GET', 'POST'])
#def affiliate_update(username):


@app.route('/job/<jid>/update/', methods=['GET', 'POST'])
def job_update(jid):
    conn = dbi.connect()
    job = jo.get_job(conn,jid)
    # username = 
    if repre.is_rep(conn,username):
            if request.method == 'GET':
                return render_template('update_job.html', title = job['title'],
                                    educ= job['qual1'], gpa= job['qual2'], skills = job['qual3'], status = job['job_status'], link = job['app_link'])
                
            else: #using POST
                #requesting information inputted by user in form
                title = request.form['jobtitle']
                educ = request.form['education']
                gpa = request.form['gpa']
                skills = request.form['technical_skills']
                status = request.form['app_status']
                link = request.form['AppLink']
        
                if request.form.get('submit') == 'update': #if user wants to update 
                    if ddl.update_job(conn,jid,title,educ,gpa,skills,status,link) == 1: 
                        flash("Job Posting for " + title + " was updated succesfully!")
                        return render_template('update_job.html', title = job['title'],
                                    educ= job['qual1'], gpa= job['qual2'], skills = job['qual3'], status = job['job_status'], link = job['app_link'])

                else: #if deleting job
                    if ddl.delete_job(conn, jid) == 1: #deletes movie and checks if deleted
                            flash('Job Posting for ' + title + ' was deleted successfully')
                            return redirect(url_for('index'))


#@app.route('/company/<comp_id>/update/', methods=['GET', 'POST'])
#def comp_update(comp_id):

@app.route('/rep/<username>/update/', methods=['GET', 'POST'])
def rep_update(username):
    conn = dbi.connect()
    rep= repre.get_rep(conn,username)
    getcomp = comp.get_company(rep['comp_id'])
    comp = getcomp['comp_name']
    if request.method == 'GET':
        return render_template('update-rep.html', name = rep['name'],comp_id = rep['comp_id']), comp_name = comp)
        
    else: #using POST
        #requesting information inputted by user in form
        name = request.form['rep-name']
        cid = request.form['comp_id']
        comp = request.form['comp_name']
        if request.form.get('submit') == 'update': #if user wants to update 
            if ddl.update_rep(conn,name,cid,comp) == 1: 
                flash("Rep Profile for " + name + " was updated succesfully!")
                return render_template('update-rep.html', name = rep['name'],comp_id = rep['comp_id']), comp_name = comp)

        else: #if deleting rep from database
            if ddl.delete_rep(conn, username) == 1: #deletes movie and checks if deleted
                    flash("Rep Profile for " + name + " was deleted successfully.")
                    return redirect(url_for('index'))

'''routes to job insert form'''
@app.route('/job/<jid>/insert/', methods=['GET', 'POST'])
def job_insert(jid):
    conn = dbi.connect()
    if request.method == 'GET': 
        # renders template for insert page
        return render_template('insert_job.html', title='Insert a Job')
    else: #if request method is POST
        # requests inputs from form 
        title = request.form['jobtitle']
        educ = request.form['education']
        gpa = request.form['gpa']
        skills = request.form['technical_skills']
        status = request.form['app_status']
        link = request.form['AppLink']
        # using the search_movie function to check the database for movie
        
        if ddl.insert_jobs(conn,title,qual1,qual2,qual3,job_status,app_link,comp_id,iid) == 1:
            #notify user that movie is now inserted
            flash("Job Posting for " + title + " has been posted!") 
            return redirect(url_for('job_update',jid = jid)) 
        
        return render_template('insert_job.html', title='Insert a Job')
    
#@app.route('/company/<comp_id>/insert/', methods=['GET', 'POST'])
#def comp_insert(comp_id):

@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # setting this variable to mehar's database since that is where we made the ddl
    db_to_use = 'mbhatia_db' # using Luiza's database
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
