# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>HELLO THERE</h1>
            <p>Welcome to the app</p>
            <a href='/hello'>Go to home page</a>
        </body>
    </html>
    """
    return html

@app.route('/add')
def show_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = add(a, b)
    return str(answer)

@app.route('/sub')
def show_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = sub(a, b)
    return str(answer)
    
@app.route('/mult')
def show_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = mult(a, b)
    return str(answer)
    
@app.route('/div')
def show_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = div(a, b)
    return str(answer)
    
    
    
