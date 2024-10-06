from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
import requests
import json

register_bp = Blueprint("Register_Menu", __name__, template_folder="templates")

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Capturando os dados do formulário
        nome_completo = request.form['nome_completo']
        nome_usuario = request.form['nome_usuario']
        email = request.form['user_email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        region = request.form['region']

        # Exibindo os dados recebidos no terminal para fins de debug
        print(f"Registrando novo usuário: {nome_completo}, {nome_usuario}, {email}, {telefone}")

        # Dados que serão enviados para o Airtable
        data = {
            "records": [
                {
                    "fields": {
                        "Name": nome_completo,
                        "User_name": nome_usuario,
                        "Email": email,
                        "Phone": telefone,
                        "Password": senha,
                        "Region": region
                    }
                }
            ]
        }

        # Configurações do Airtable
        pat = 'patqTjSfqmO03jEDd.4330e2c445694f5b08b9223c4c869eb4b19c1c903dd58ff8b409aefd3dabe73a'
        base_id = 'appAjKZG2ceyIn0FU'
        table_name = 'tbluUrT38tFYLVEBQ'
        airtable_url = f'https://api.airtable.com/v0/{base_id}/{table_name}'
        headers = {
            'Authorization': f'Bearer {pat}',
            'Content-Type': 'application/json'
        }

        # Enviando os dados para o Airtable
        response = requests.post(airtable_url, headers=headers, data=json.dumps(data))

        # Verificando a resposta da API do Airtable
        if response.status_code == 200:
            flash('Usuário registrado com sucesso!', 'success')
            return redirect(url_for('Login_Menu.route_login'))
        else:
            flash('Erro ao registrar usuário. Tente novamente.', 'error')
            return redirect(url_for('Register_Menu.route_register'))

    # Renderizando o template do formulário de registro quando a página for acessada via GET
    return render_template('register.html')