from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import SessionLocal  # Importa a sessão configurada corretamente
from models import Usuario
from werkzeug.security import check_password_hash  # Para verificar o hash da senha

login_bp = Blueprint("Login_Menu", __name__, template_folder="templates")

@login_bp.route("/login", methods=['GET', 'POST'])
def route_login():
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário
        email = request.form['email']
        senha = request.form['senha']  # Senha digitada pelo usuário no login

        # Usa o SessionLocal para criar a sessão com o banco de dados
        session = SessionLocal()
        
        try:
            # Consulta o banco de dados pelo e-mail
            usuario = session.query(Usuario).filter_by(email=email).first()

            # Verifica se o usuário existe e se a senha está correta
            if usuario and check_password_hash(usuario.password, senha):
                flash('Login bem-sucedido!', 'success')
                return redirect(url_for('home'))  # Substitua pelo endpoint desejado
            else:
                flash('Email ou senha incorretos!', 'danger')
        finally:
            # Fecha a sessão com o banco de dados
            session.close()

    # Retorna a página de login no método GET
    return render_template('login.html')
