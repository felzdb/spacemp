from flask import Blueprint, render_template, redirect

main_menu_bp = Blueprint("Main_Menu", __name__, template_folder="templates")

@main_menu_bp.route("/main_menu")
def route_login():
    return render_template('menu.html')