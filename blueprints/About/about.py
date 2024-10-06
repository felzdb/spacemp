from flask import Blueprint, render_template

# Criação do blueprint
about_bp = Blueprint('about', __name__, template_folder='templates')

# Rota da página "About"
@about_bp.route("/about")
def route_about():
    return render_template('about.html')
