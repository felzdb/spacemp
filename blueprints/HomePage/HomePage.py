from flask import Blueprint, render_template, redirect

HomePage_bp = Blueprint("HomePage_Menu", __name__, template_folder="templates")

@HomePage_bp.route("/")
def route_HomePage():
    return render_template('HomePage.html')