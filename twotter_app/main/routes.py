"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime

# Import app and db from events_app package so that we can run app
from twotter_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################


@main.route('/')
def homepage():
    return render_template('homepage.html')