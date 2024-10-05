from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import Session
from db import engine
from models import Usuario

login_bp = Blueprint("Login_Menu", __name__, template_folder="templates")

@login_bp.route("/login", methods=['GET', 'POST'])
def route_login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']  # Considere usar hash para senhas

        session = Session()
        usuario = session.query(Usuario).filter_by(email=email).first()

        if usuario and usuario.senha == senha:  # Lembre-se de hashear senhas!
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('home'))  # Substitua pelo endpoint desejado
        else:
            flash('Email ou senha incorretos!', 'danger')
        
        session.close()
    
    return render_template('login.html')
