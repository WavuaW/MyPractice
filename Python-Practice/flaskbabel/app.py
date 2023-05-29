from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

def get_locale():
    return 'en'
    # return request.accept_languages.best_match(['en', 'es'])
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():

    chris = gettext('Anthony')
    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    de_num = numbers.format_decimal(12345, locale='de_DE')

    d = date(2007, 3, 1)

    us_date = dates.format_date(d, locale='en_US') 
    de_date = dates.format_date(d, locale='de_DE') 

    results = {'us_num': us_num, 'se_num': se_num, 'de_num': de_num, 'us_date' : us_date, 'de_date' : de_date}
    return render_template('index.html', results=results, chris=chris)

if __name__ == '__main__':
    app.run(debug=True)
    