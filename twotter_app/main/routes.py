"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from twotter_app.models import Twot, Reply
from twotter_app.main.forms import TwotForm, ReplyForm

# Import app and db from events_app package so that we can run app
from twotter_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################


@main.route('/')
def homepage():
    all_twots = Twot.query.all()
    return render_template('homepage.html', twots=all_twots)

@main.route('/compose_twot', methods=['GET', 'POST'])
@login_required
def compose_twot():
    form = TwotForm()

    if form.validate_on_submit():
        twot = Twot(
            body=form.body.data,
            publish_date=date.today(),
            user=current_user
        )

        db.session.add(twot)
        db.session.commit()

        flash('Your Twot was successfully Twotted!')
        return redirect(url_for('main.homepage'))
    return render_template('compose_twot.html', form=form)


@main.route('/twot/<twot_id>')
@login_required
def twot_detail(twot_id):
    form = ReplyForm()
    twot =  Twot.query.get(twot_id)
    replies = Reply.query.filter_by(twot_id=twot_id)

    return render_template('twot.html', twot=twot, replies=replies, form=form)


@main.route('/reply/<twot_id>', methods=['POST'])
@login_required
def twot_reply(twot_id):
    form = ReplyForm()
    twot = Twot.query.get(twot_id)

    if form.validate_on_submit():
        reply = Reply(
            body=form.body.data,
            publish_date=date.today(),
            user=current_user,
            twot=twot
        )

        db.session.add(reply)
        db.session.commit()

        flash('Your reply was submitted successfully!')
        return redirect(url_for('main.twot_detail', twot_id=twot_id))
    
    return render_template('twot.html', form=form, twot=twot)