
from flask import Blueprint, request, jsonify
import logging
import time

auth_bp = Blueprint('auth_bp', __name__)

# Static credentials for validation
STATIC_USERNAME = "galagar"
STATIC_PASSWORD = "12345"

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Handles user login, validates credentials, and logs the attempt.
    This route will be used for future JWT token generation.
    """
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Update Logging for Login Activity
    # Log the attempt before processing
    log_message = f"Login attempt for user: '{username}'"
    
    # Simulate a slight processing delay to ensure logs are processed correctly
    time.sleep(0.01)

    # Validate credentials (using static values for now)
    if username == STATIC_USERNAME and password == STATIC_PASSWORD:
        # Generate the token and return it.
        
        logging.info(f"{log_message} - Result: SUCCESS")
        return jsonify(
            {'message': 'Login successful', 
             'user': username,
             # Placeholder for future JWT token
             #'token_status': 
            }
        ), 200
    else:
        logging.warning(f"{log_message} - Result: FAILED")
        return jsonify({'message': 'Invalid credentials'}), 401