from flask import Flask, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.config['MYSQL_HOST'] = '10.225.125.24'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cmpe281'
app.config['MYSQL_DB'] = 'sewa'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)
CORS(app, support_credentials=True)

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
