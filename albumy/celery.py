# -*- coding: utf-8 -*-
from flask import Flask
from celery import Celery

from albumy.settings import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
# Celery configuration
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'database'
# app.config['CELERY_RESULT_DBURI'] = 'sqlite:///temp.db'
# app.config['CELERY_TRACK_STARTED'] = True
# app.config['CELERY_SEND_EVENTS'] = True

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

@celery.task
def do_something(data):

    from celery import current_task
    import os
    import subprocess
    with app.app_context():
        pass
        #run some bash script with some params in my case

