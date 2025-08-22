// Main JavaScript for SANAS Presentation Website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initSmoothScrolling();
    initAnimations();
    initContactForm();
    initNavbarScroll();
    
    console.log('SANAS website loaded successfully!');
});

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Intersection Observer for animations
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    document.querySelectorAll('.card, .contact-item').forEach(el => {
        observer.observe(el);
    });
}

// Contact form enhancement
function initContactForm() {
    const contactForm = document.querySelector('form[method="POST"]');
    if (!contactForm) return;

    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.innerHTML;

    contactForm.addEventListener('submit', function(e) {
        // Show loading state
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="loading"></span> Sending...';
        
        // Reset after 3 seconds (in real app, this would be handled by server response)
        setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
        }, 3000);
    });

    // Real-time form validation
    const requiredFields = contactForm.querySelectorAll('input[required], textarea[required]');
    requiredFields.forEach(field => {
        field.addEventListener('blur', validateField);
        field.addEventListener('input', clearValidation);
    });
}

// Field validation
function validateField(e) {
    const field = e.target;
    const value = field.value.trim();
    
    // Remove existing validation classes
    field.classList.remove('is-valid', 'is-invalid');
    
    if (!value) {
        field.classList.add('is-invalid');
        showFieldError(field, 'This field is required.');
    } else if (field.type === 'email' && !isValidEmail(value)) {
        field.classList.add('is-invalid');
        showFieldError(field, 'Please enter a valid email address.');
    } else {
        field.classList.add('is-valid');
        clearFieldError(field);
    }
}

// Clear validation on input
function clearValidation(e) {
    const field = e.target;
    field.classList.remove('is-invalid');
    clearFieldError(field);
}

// Show field error
function showFieldError(field, message) {
    clearFieldError(field); // Clear any existing error
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
}

// Clear field error
function clearFieldError(field) {
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
}

// Email validation
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Navbar scroll effect
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    if (!navbar) return;

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
}

// Add CSS for navbar scroll effect
const style = document.createElement('style');
style.textContent = `
    .navbar-scrolled {
        background-color: rgba(33, 37, 41, 0.95) !important;
        backdrop-filter: blur(10px);
        transition: background-color 0.3s ease;
    }
`;
document.head.appendChild(style); 