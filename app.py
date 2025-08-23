from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

# Configure email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

# Routes
@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@app.route('/equipment')
def equipment():
    """Equipment page route"""
    return render_template('equipment.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        company = request.form.get('company')
        service = request.form.get('service')
        
        if name and email and message:
            try:
                # Send email
                msg = Message(
                    subject=f'New Contact Form - {name}',
                    sender=os.environ.get('EMAIL_USER'),
                    recipients=['skb.group@mail.ru'],
                    body=f"""
                    New message from website:
                    
                    Name: {name}
                    Email: {email}
                    Company: {company or 'Not specified'}
                    Service: {service or 'Not specified'}
                    
                    Message:
                    {message}
                    """
                )
                mail.send(msg)
                flash('Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.', 'success')
            except Exception as e:
                # Log error and show user-friendly message
                print(f"Email error: {e}")
                flash('Произошла ошибка при отправке сообщения. Пожалуйста, свяжитесь с нами напрямую.', 'error')
            
            return redirect(url_for('contact'))
        else:
            flash('Пожалуйста, заполните все обязательные поля.', 'error')
    
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
    # Production-ready configuration
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=port) 