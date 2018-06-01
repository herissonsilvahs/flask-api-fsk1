import os
from flask import (
    Blueprint, request, current_app, send_from_directory, render_template
)

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route("/")
def index():
    return "teste"