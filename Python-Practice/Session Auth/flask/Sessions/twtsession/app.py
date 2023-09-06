from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World <h1>TRASH CAN</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route('/admin')
def admin():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
