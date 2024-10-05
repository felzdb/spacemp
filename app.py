from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd


from blueprints.Login.login import login_bp
from blueprints.Register.register import register_bp
from blueprints.Dash_temp.dash_temp import dash_temp_bp


app = Flask(__name__)
app.secret_key = 'sua_chave_secretaa'

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dash_temp_bp)

# Função para verificar credenciais
def verificar_usuario(username, password):
    df = pd.read_excel('users.xlsx')
    for index, row in df.iterrows():
        if row['username'] == username and row['password'] == password:
            return True
    return False

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if verificar_usuario(username, password):
        print(username, password)
        flash('Login bem-sucedido!', 'success')
        return redirect(url_for('home'))
    else:
        print(username, password)
        flash('Nome de usuário ou senha incorretos.', 'danger')
        return redirect(url_for('home'))

#//URL INVÁLIDA//#
app.errorhandler(404)

#//RODAR APLICAÇÃO//#
if __name__ == '__main__':
    app.run(debug=True)