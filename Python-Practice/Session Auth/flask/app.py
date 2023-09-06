from flask import Flask, session, request, redirect, url_for

# Access cookies using the cookies attribute.
# To set cookies use the set_cookie methodof response objects.
# if you want to use sessions, do not use the cookies directy but use the Sessions in flask to add some security on top of the cookies for you.

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session}["username]'
    return 'You are not logged in'

@app.route('/ligin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
            <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
            </form>
        '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))