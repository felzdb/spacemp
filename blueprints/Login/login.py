from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import pandas as pd
import requests


login_bp = Blueprint("Login_Menu", __name__, template_folder="templates")

@login_bp.route("/login", methods=['GET', 'POST'])
def route_login():
    if request.method == 'POST':
        # Receber os dados do formulário
        username = request.form['username']
        password = request.form['password']
        
        print(f"Dados recebidos no formulário: Usuário={username}, Senha={password}")  # Debugging print
        
        if verificar_usuario(username, password):
            # Buscar a região associada ao usuário no Airtable ou banco de dados
            region = buscar_regiao_do_usuario(username)
            
            print(region)

            if region:
                # Armazenar a região na sessão do Flask
                session['region'] = region
                print(f"Região armazenada na sessão: {session['region']}")
            else:
                flash('Erro ao buscar a região do usuário.', 'error')
                return redirect(url_for('Login_Menu.route_login'))  # Voltar ao login em caso de falha
            

            return redirect(url_for('dash_temp_menu.route_HomePage'))  # Sucesso: Redirecionar para o dashboard
        else:
            flash('Nome de usuário ou senha incorretos', 'error')
            return redirect(url_for('Login_Menu.route_login'))  # Falha: Redirecionar de volta ao login

    # Caso seja um GET, renderizar a página de login
    return render_template('login.html')


# Função para verificar credenciais
def verificar_usuario(username, password):
    # Configurações do Airtable
    pat = 'patqTjSfqmO03jEDd.4330e2c445694f5b08b9223c4c869eb4b19c1c903dd58ff8b409aefd3dabe73a'
    base_id = 'appAjKZG2ceyIn0FU'
    table_name = 'tbluUrT38tFYLVEBQ'
    airtable_url = f'https://api.airtable.com/v0/{base_id}/{table_name}'
    headers = {
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    }

    records = []

    # Loop para lidar com a paginação
    while True:
        response = requests.get(airtable_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            records.extend(data['records'])

            # Verifique se existe um 'offset' na resposta, se sim, use-o para a próxima solicitação
            if 'offset' in data:
                # Atualize a URL com o novo offset
                airtable_url = f'https://api.airtable.com/v0/{base_id}/{table_name}?offset={data["offset"]}'
            else:
                # Se não houver 'offset', todos os registros foram recuperados
                break
        else:
            print(f'Erro ao buscar dados: {response.status_code}')
            return False  # Retorne falso em caso de erro

    # Converter os dados para um DataFrame
    rows = [record['fields'] for record in records]
    df_airtable = pd.DataFrame(rows)

    # Verificar se o usuário e a senha correspondem a algum registro
    user_row = df_airtable[(df_airtable['User_name'] == username) & (df_airtable['Password'] == password)]

    if not user_row.empty:
        return True  # Usuário e senha estão corretos
    else:
        return False  # Usuário ou senha estão incorretos
    
def buscar_regiao_do_usuario(username):
    pat = 'patqTjSfqmO03jEDd.4330e2c445694f5b08b9223c4c869eb4b19c1c903dd58ff8b409aefd3dabe73a'
    base_id = 'appAjKZG2ceyIn0FU'
    table_name = 'tbluUrT38tFYLVEBQ'
    airtable_url = f'https://api.airtable.com/v0/{base_id}/{table_name}'
    headers = {
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(airtable_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for record in data['records']:
            fields = record['fields']
            if fields.get('Name') == username:
                return fields.get('Region')  # Retorna a região associada ao usuário
    return None
    