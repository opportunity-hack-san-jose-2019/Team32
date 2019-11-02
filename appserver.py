from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '10.225.125.24'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'cmpe281'
app.config['MYSQL_DB'] = 'sewa'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)


@app.route('/result', methods = ['GET', 'POST'])
def donate():
    if request.method == 'GET':
        place = request.args.get('place', None)
        if place:
            return place
        return "No place information is given"

@app.route('/show', methods = ['GET'])
def showtables():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    mysql.connection.commit()
    rv = cur.fetchall()
    cur.close()
    return str(rv)
    


if __name__ == '__main__':
    app.run(debug = True, host="10.225.125.24", port=5000)
