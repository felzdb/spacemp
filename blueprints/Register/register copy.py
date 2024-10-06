from flask import Blueprint, render_template, redirect, request, url_for


register_bp = Blueprint("register", __name__, template_folder="templates")

@register_bp.route("/register", methods=["POST", "GET"])
def route_register():
    if(request.method == "POST"):
        redirect("/login")
    else:
        return render_template('register.html')
    