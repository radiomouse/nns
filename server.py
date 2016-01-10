import json
from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
users_file = 'data/addressbook.json'
act_file = 'data/activities.json'

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/leden/')
def members_page():
    jdata = load_json_by(users_file)
    print('found users')
    return render_template('user_list.html', users=jdata)

@app.route('/leden/<username>')
def get_member_by(username):
    error = None
    juser = find_json_item_by(username, load_json_by(users_file))
    if juser is None:
        error = 'Gebruiker kon niet gevonden worden'
    return render_template('user_page.html', user=juser, error=error)

@app.route('/activiteiten/')
def activity_page():
    return render_template('activities.html', activities=load_json_by(act_file))

@app.route('/activiteiten/<activity_id>')
def get_activity_by(activity_id):
    error = None
    jactivity = find_json_item_by(activity_id, load_json_by(act_file))
    if jactivity is None:
        error = 'Activiteit kon niet gevonden worden'
    return render_template('activity.html', activity=jactivity, error=error)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        juser = find_json_item_by(request.form.username, load_json_by(users_file))
        if match_pashword(juser, request.form.pashword):
            return redirect('/')
        error = 'invalid credentials'
    return render_template('login.html', error)
        
def match_pashword(juser, pashword):
    return juser['pashword'] == pashword
    
def load_json_by(json_file_name):
    with open(json_file_name) as data_file:
        return json.loads(data_file.read())
    return None
        
def find_json_item_by(json_key, jdata):
    for jkey in jdata:
        if jkey == json_key:
            return jdata[jkey]
    return None

if __name__=='__main__':
    app.run()
