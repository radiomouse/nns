import json
from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
users_file = 'addressbook.json'
act_file = 'activities.json'

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/leden/')
def members_page():
    jdata = load_json_by(users_file)
    return render_template('user_list.html', users=jdata)

@app.route('/leden/<username>')
def get_member_by(username):
    jdata = load_json_by(users_file)
    print('retrieved jdata')
    juser = find_json_item_by(username, jdata)
    print('found juser, off to render template')
    if juser is None:
        return render_template('user_not_found.html')
    print('juser not none')
    return render_template('user_page.html', user=juser)

@app.route('/activiteiten/')
def activity_page():
    print('entering activity page')
    jactivities = load_json_by(act_file)
    print('jactivity found')
    return render_template('activities.html', activities=jactivities)

@app.route('/activiteiten/<activity_id>')
def get_activity_by(activity_id):
    jactivities = load_json_by(act_file)
    jactivity = find_json_item_by(activity_id, jactivities)
    print('jactivity found')
    if jactivity is None:
        return render_template('activity_not_found.html')
    return render_template('activity.html', activity=jactivity)

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