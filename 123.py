from flask import Flask

app = Flask(__name__)

num = 111
@app.route('/')
def demo1():
    return 'demo1'

if __name__ == '__main__':
    app.run(debug=True)