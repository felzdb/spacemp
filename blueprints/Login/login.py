from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import Session

login_bp = Blueprint("Login_Menu", __name__, template_folder="templates")

@login_bp.route("/login", methods=['GET', 'POST'])
def route_login():
    return render_template('login.html')
