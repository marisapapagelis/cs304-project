
@app.route('/search/', methods = ['GET'])
def query():
    industry = request.args['industry']
    kind= request.args['kind']
    conn=dbi.connect()
    if kind =='company':
        companylist=company.get_company(conn,comp_id)
        if len(companylist) == 1: 
            return redirect(url_for('company', comp_id=companylist[0]['comp_id']))
        elif len(companylist) > 1: 
            return render_template('company-list.html',companylist=companylist,kind=kind)
        else :
            flash('Sorry, no company with this name exists.')
            return redirect(url_for('index'))
    elif kind == 'industry':
        industrylist=industry.get_industry(conn,comp_id)
        if len(industrylist) == 1: 
            return redirect(url_for('industry', iid=industrylist[0]['iid']))
        elif len(industrylist) > 1: 
            return render_template('industry-list.html',industrylist=industrylist,kind=kind)
        else :
            flash('Sorry, no industry with this name exists.')
            return redirect(url_for('index'))
    else: 
        personlist=affiliate.get_affiliate(conn,username)
        if len(personlist) == 1: 
            return redirect(url_for('affiliate',username=personlist[0]['username']))
        elif len(personlist) > 1: 
            return render_template('affiliate-list.html',personlist=personlist,kind=kind)
        else:
            flash('Sorry, no company with this name exists.')
            return redirect(url_for('index'))






