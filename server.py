#! env/bin/python
import json
import flask

app = flask.Flask(__name__)
users_file = 'data/addressbook.json'
act_file = 'data/activities.json'
private_key=''

@app.route('/')
def home_page():
    return flask.render_template("index.html")

@app.route('/leden/')
def members_page():
    jdata = load_json_by(users_file)
    print('found users')
    return flask.render_template('user_list.html', users=jdata)

@app.route('/leden/<username>')
def get_member_by(username):
    juser = find_json_item_by(username, load_json_by(users_file))
    return flask.render_template('user_page.html', user=juser)

@app.route('/activiteiten/')
def activity_page():
    return flask.render_template('activities.html', activities=load_json_by(act_file))

@app.route('/activiteiten/<activity_id>')
def get_activity_by(activity_id):
    jactivity = find_json_item_by(activity_id, load_json_by(act_file))
    return flask.render_template('activity.html', activity=jactivity)

@app.route('/login/', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        juser = find_json_item_by(request.form.username, load_json_by(users_file))
        if verify_password(juser, request.form.password)
           return redirect('/') 
    return flask.render_template('login.html')

def verify_password(json_user, password):
    


def load_json_by(json_file_name):
    with open(json_file_name) as data_file:
        return json.loads(data_file.read())
    flask.abort(404)
        
def find_json_item_by(json_key, jdata):
    for jkey in jdata:
        if jkey == json_key:
            return jdata[jkey]
    flask.abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template(error.html)

if __name__=='__main__':
    app.run(debug=True)
