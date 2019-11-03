from flask import Flask, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = '10.225.125.24'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cmpe281'
app.config['MYSQL_DB'] = 'sewa'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)
CORS(app, support_credentials=True)

def format(cur, rv):
    json_data=[]
    row_headers=[x[0] for x in cur.description]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json_data

@cross_origin(supports_credentials=True)
@app.route('/donate', methods = ['GET', 'POST'])
def donate():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        data = request.get_json()
        name = data['name']
        email = data['email']
        contact = data['contact']
        cur.execute("INSERT INTO donors(name, contact, email) VALUES(%s, %s, %s)", (name, contact, email))
        items = data['items']
        for item in items:
            cur.execute("INSERT INTO inventory(description, quantity, category) VALUES(%s, %s, %s)", (item['description'], item['quantity'], item['category']))
        mysql.connection.commit()
        rv = cur.fetchall()
        return str(rv)


@cross_origin(supports_credentials=True)
@app.route('/allcases', methods = ['GET'])
def handle_cases():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("select * from cases")
        mysql.connection.commit()
        rv = cur.fetchall()
        json_data = format(cur, rv)
        cur.close()
        return {"cases" : json_data}

@cross_origin(supports_credentials=True)
@app.route('/unassignedcases', methods = ['GET'])
def get_unassigned_cases():
    cur = mysql.connection.cursor()
    cur.execute("select * from cases where caseid not in (select caseid from assignments)")
    mysql.connection.commit()
    rv = cur.fetchall()
    json_data = format(cur, rv)
    cur.close()
    return {"cases" : json_data}

@cross_origin(supports_credentials=True)
@app.route('/volunteers', methods = ['GET'])
def get_volunteers():
    cur = mysql.connection.cursor()
    cur.execute("select * from users where role = 'volunteer'")
    mysql.connection.commit()
    rv = cur.fetchall()
    json_data = format(cur, rv)
    cur.close()
    return {"volunteers" : json_data}

@cross_origin(supports_credentials=True)
@app.route('/validatecases', methods = ['POST'])
def validate_cases():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        data = request.get_json()
        for key, val in data.items():
            cur.execute("UPDATE cases SET priority=%s WHERE caseid=%s", val, key)
            mysql.connection.commit()
            return
        
@cross_origin(supports_credentials=True)
@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    print(data['username'])
    cur = mysql.connection.cursor()
    cur.execute("select pwd from users where username like %s", [data['username']])
    mysql.connection.commit()
    rv = cur.fetchone()[0]
    if rv == data['password']:
        return "1"
    return "0"

@cross_origin(supports_credentials=True)
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        primary_contact = data['primary_contact']
        secondary_contact = data.get('secondary_contact', None)
        role = data['role']
        username = data['username']
        pwd = data['pwd']
        address = data['address']
        cur.execute("INSERT INTO users(firstname, lastname, email, primary_contact, secondary_contact, role, username, pwd, address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (firstname, lastname, email, primary_contact, secondary_contact, role, username, pwd, address))
        mysql.connection.commit()
        rv = cur.fetchall()
        return str(rv)

@cross_origin(supports_credentials=True)
@app.route('/show', methods = ['GET'])
def showtables():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    mysql.connection.commit()
    rv = cur.fetchall()
    cur.close()
    return str(rv)

@cross_origin(supports_credentials=True)
@app.route('/seekhelp', methods = ['POST'])
def seekhelp():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        data = request.get_json()
        cur.execute("INSERT INTO cases(problem_description, priority, assigned_priority, help_type, name, contact, address) VALUES(%s, %s, %s, %s, %s, %s, %s)", (data['problem_description'], data['priority'], data['assigned_priority'], data['help_type'], data['name'], data['contact'], data['address']))
        mysql.connection.commit()
        rv = cur.fetchall()
        cur.close()
        return str(rv)

@cross_origin(supports_credentials=True)
@app.route('/hello', methods = ['GET'])
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")
