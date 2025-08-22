from flask import Flask, render_template, request, flash, redirect, url_for
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

# Routes
@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/services')
def services():
    """Services page route"""
    return render_template('services.html')

@app.route('/equipment')
def equipment():
    """Equipment page route"""
    return render_template('equipment.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic form validation
        if name and email and message:
            # Here you would typically send an email or save to database
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('errors/500.html'), 500

# Run application
if __name__ == '__main__':
    # Debug mode - only for development
    app.run(debug=True, host='0.0.0.0', port=5000) 