from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' # //// - is an absolute path while /// - is relatuve

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8080, debug=True)

