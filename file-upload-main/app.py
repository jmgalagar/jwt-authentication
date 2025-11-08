
import os
import logging
from flask import Flask
from config import Config
from extensions import db, jwt # NOTE: Added 'jwt' import
from controllers.file_controller import file_bp 
from controllers.auth_controller import auth_bp 

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app) #Initialize JWT extension

#Setup logging
os.makedirs(app.config['LOG_FOLDER'], exist_ok=True)
logging.basicConfig(
    filename=f"{app.config['LOG_FOLDER']}/app.log",
    #Maintain Logging Consistency
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

app.register_blueprint(file_bp)
app.register_blueprint(auth_bp, url_prefix='/auth') # Registered with a prefix

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)