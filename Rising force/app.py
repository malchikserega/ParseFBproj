from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['UPLOAD_FOLDER'] = './tmp/'
ALLOWED_EXTENSIONS = ('txt',)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
db = SQLAlchemy(app)

import models