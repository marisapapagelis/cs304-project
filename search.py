
@app.route('/search/')
def search():
    kind = request.args['kind']
    industry = request.args['industry']

    conn = dbi.connect()
    curs = dbi.cursor(conn)

    if kind == ''






