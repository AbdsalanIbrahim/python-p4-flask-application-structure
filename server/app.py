from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome to the EpicTech Home Page!</h1>'


@app.route('/EpicTech')
def epic_tech():
    return '<h1>Welcome to EpicTech!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
