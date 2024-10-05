from flask import Flask, render_template, blueprints
from db import engine
from models import Base

from blueprints.HomePage.HomePage import HomePage_bp
from blueprints.Login.login import login_bp
from blueprints.Register.register import register_bp
from blueprints.Dash_temp.dash_temp import dash_temp_bp
app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(HomePage_bp)
app.register_blueprint(dash_temp_bp)

#//URL INVÁLIDA//#
app.errorhandler(404)

#//RODAR APLICAÇÃO//#
if __name__ == '__main__':
    app.run(debug=True)