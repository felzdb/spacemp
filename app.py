from flask import Flask, render_template, blueprints
import psycopg2
from psycopg2 import sql


from blueprints.Login.login import login_bp
from blueprints.Register.register import register_bp
app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)

DATABASE = {
    'dbname': 'plsql-agroassets',
    'user': 'postgres',
    'password': '36\H30Ak9Ie4\-+O',
    'host': '34.151.212.149',  # ou o IP do seu servidor
    #'port': '5432'        # padrão do PostgreSQL
}

def get_db_connection():
    conn = psycopg2.connect(**DATABASE)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tbl_users;')
    results = cur.fetchall()
    cur.close()
    conn.close()
    return str(results)

#//URL INVÁLIDA//#
app.errorhandler(404)

#//RODAR APLICAÇÃO//#
if __name__ == '__main__':
    app.run(debug=True)