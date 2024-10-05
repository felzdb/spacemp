from flask import Blueprint, render_template, redirect

login_bp = Blueprint("Login_Menu", __name__, template_folder="templates")

@login_bp.route("/login")
def route_login():
    return render_template('login.html')