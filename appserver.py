from flask import Flask, request

app = Flask(__name__)

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        place = request.args.get('place', None)
        if place:
            return place
        return "No place information is given"

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug = True, host="10.225.125.24", port=5000)
