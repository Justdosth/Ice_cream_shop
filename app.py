from flask import Flask, render_template, request, url_for
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Babel
app.config['LANGUAGES'] = ['en', 'fa']  # English and Persian
app.config['BABEL_DEFAULT_LOCALE'] = 'fa'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

# Function to get the current locale
def get_locale():
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Initialize Babel
babel.init_app(app, locale_selector=get_locale)

# Function to determine text direction
def get_direction(lang):
    return 'rtl' if lang == 'fa' else 'ltr'

@app.route('/')
def home():
    lang = get_locale()  # Get the current language
    direction = get_direction(lang)  # Determine the text direction
    return render_template('index.html', lang=lang, direction=direction)

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('static', filename='en'))  # Should output "/?lang=en"
    app.run(debug=True)
