from flask import render_template
from app.extensions import celery, mail
from app.database import db
from celery.signals import task_postrun
from flask_mail import Message
from app.decorators import with_request_context
from app.utils import utils


# Sends registration e-mail
@with_request_context
@celery.task
def send_registration_email(user, email, token):
    msg = Message(
        'User Registration',
        sender='no-reply@recipes.com',
        recipients=[email]
    )
    URL = utils.hosturl(url_for('auth.verify', token=token, _external=True))
    msg.body = render_template(
        'mail/registration.mail',
        URL=URL
    )
    mail.send(msg)


@task_postrun.connect
def close_session(*args, **kwargs):
    # Flask SQLAlchemy will automatically create new sessions for you from
    # a scoped session factory, given that we are maintaining the same app
    # context, this ensures tasks have a fresh session (e.g. session errors
    # won't propagate across tasks)
    db.session.remove()
