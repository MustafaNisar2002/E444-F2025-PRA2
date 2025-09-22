# hello.py  (Example 2-1)
from flask import Flask
app = Flask(__name__)            # application instance

@app.route('/')                  # route + view function
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':       # dev server startup
    app.run(debug=True)
