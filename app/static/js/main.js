/**
 * Main JavaScript file for the FastAPI Boilerplate
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('FastAPI Boilerplate loaded');
    
    // Example of a simple toggle function for mobile navigation
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', function() {
            navLinks.classList.toggle('show');
        });
    }
    
    // Add active class to current navigation link
    const currentLocation = window.location.pathname;
    const navItems = document.querySelectorAll('.nav-links a');
    
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href === currentLocation) {
            item.classList.add('active');
        }
    });
    
    // Example of a simple form validation
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                event.preventDefault();
                
                // Show error message
                const errorMessage = document.createElement('div');
                errorMessage.className = 'alert alert-danger';
                errorMessage.textContent = 'Please fill in all required fields.';
                
                // Insert error message at the top of the form
                form.insertBefore(errorMessage, form.firstChild);
                
                // Remove error message after 5 seconds
                setTimeout(() => {
                    errorMessage.remove();
                }, 5000);
            }
        });
    });
    
    // Example of handling API calls
    const apiExample = async (endpoint, method = 'GET', data = null) => {
        try {
            const options = {
                method,
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            };
            
            if (data && (method === 'POST' || method === 'PUT')) {
                options.body = JSON.stringify(data);
            }
            
            const response = await fetch(endpoint, options);
            
            if (!response.ok) {
                throw new Error(`API request failed with status ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API request error:', error);
            throw error;
        }
    };
    
    // Export helper functions for reuse
    window.appHelpers = {
        apiExample,
        showAlert: (message, type = 'info') => {
            const alertElement = document.createElement('div');
            alertElement.className = `alert alert-${type}`;
            alertElement.textContent = message;
            
            document.querySelector('.container').prepend(alertElement);
            
            setTimeout(() => {
                alertElement.remove();
            }, 5000);
        }
    };
});
