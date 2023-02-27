from flask import Flask
application = Flask(__name__)

from carbon_app.home.routes import home
from carbon_app.methodology.routes import methodology
from carbon_app.carbon_calculator.routes import carbon_calculator
from carbon_app.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_calculator)
application.register_blueprint(users)