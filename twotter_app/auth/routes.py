"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from twotter_app.models import Twot, Reply, User
from twotter_app.auth.forms import SignUpForm, LoginForm
from twotter_app import bcrypt

# Import app and db from events_app package so that we can run app
from twotter_app import app, db

auth = Blueprint("auth", __name__)

##########################################
#           Routes                       #
##########################################


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(
            username=form.username.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()
        flash('Account Created')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)
    pass