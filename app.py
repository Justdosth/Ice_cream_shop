from flask import Flask, render_template, request, url_for
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Babel
app.config['LANGUAGES'] = ['en', 'fa']  # English and Persian
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

# Function to get the current locale
def get_locale():
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Function to determine text direction
def get_direction(lang):
    return 'rtl' if lang == 'fa' else 'ltr'

# Initialize Babel
babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def home():
    products = [
        {"name": "Vanilla Ice Cream", "price": 99, "image": "product-1.jpg"},
        {"name": "Chocolate Ice Cream", "price": 89, "image": "product-2.jpg"},
        {"name": "Strawberry Ice Cream", "price": 95, "image": "product-3.jpg"},
        {"name": "Mango Ice Cream", "price": 110, "image": "product-4.jpg"},
        {"name": "Pistachio Ice Cream", "price": 120, "image": "product-5.jpg"},
    ]

    testimonials = [
        {"feedback": "Dolor eirmod diam stet kasd sed. Aliqu rebum est eos.", "client_name": "Client 1", "profession": "Designer", "image": "testimonial-1.jpg"},
        {"feedback": "Rebum elitr dolore et eos labore, stet justo sed est sed.", "client_name": "Client 2", "profession": "Developer", "image": "testimonial-2.jpg"},
        {"feedback": "Diam sed sed dolor stet amet eirmod eos labore diam.", "client_name": "Client 3", "profession": "Manager", "image": "testimonial-3.jpg"},
    ]
    lang = get_locale()  # Get the current language
    direction = get_direction(lang)  # Determine the text direction
    return render_template('index.html', lang=lang, direction=direction, products=products, testimonials=testimonials)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/service')
def service():
    return render_template('service.html')

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('static', filename='en'))  # Should output "/?lang=en"
    app.run(debug=True)

