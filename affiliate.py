#very rough version of py file, because we need to change our tables :) 

import cs304dbi as dbi 

import random

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
    return render_template('affiliate-page.html',  name=user_name, 
                                username=userid, org1=org1, org2=org2,org3=org3,
                                description=None, reps=reps_iterate)
 
