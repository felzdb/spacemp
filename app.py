from flask import Flask, render_template, blueprints


from blueprints.Login.login import login_bp
app = Flask(__name__)

app.register_blueprint(login_bp)


#//URL INVÁLIDA//#
app.errorhandler(404)

#//RODAR APLICAÇÃO//#
if __name__ == '__main__':
    app.run(debug=True)