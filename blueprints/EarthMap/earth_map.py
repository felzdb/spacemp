from flask import Blueprint, render_template

earth_map_bp = Blueprint('earth_map', __name__, template_folder='Templates')

@earth_map_bp.route('/earth_map')
def earth_map():
    return render_template('map.html')
