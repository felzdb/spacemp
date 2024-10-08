from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
#import requests

from blueprints.Login.login import login_bp
from blueprints.HomePage.HomePage import HomePage_bp
from blueprints.Register.register import register_bp
from blueprints.Dash_temp.dash_temp import dash_temp_bp
from blueprints.GPTBot.GPTBot import chatbot_bp
from blueprints.About.about import about_bp


app = Flask(__name__)
app.secret_key = 'sua_chave_secretaa'

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dash_temp_bp)
app.register_blueprint(HomePage_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(about_bp)

@app.route("/")
def route_HomePage():
    return render_template('HomePage.html')

#//URL INVÁLIDA//#
app.errorhandler(404)

#//RODAR APLICAÇÃO//#
if __name__ == '__main__':
    app.run(debug=True)