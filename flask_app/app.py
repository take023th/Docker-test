from flask import Flask


app = Flask(__name__)

@app.route("/hello") # FlaskのURLルーティングにおいてURLは/で始める。
def hello_world():
    return 'Hello Paiza'

if  __name__ == '__main__':
    app.run(host='0.0.0.0')
