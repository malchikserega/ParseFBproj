from app import db


class Target(db.Model):
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    url = db.Column(db.String(1024), unique=True)
    in_process = db.Column(db.Boolean, nullable=False)
    is_ready = db.Column(db.Boolean, nullable=False)

    __tablename__ = 'target'

    def __init__(self, url):
        self.url = url
        self.in_process = self.is_ready = False

    def __repr__(self):
        return '<Target %r>' % self.url


class Photo(db.Model):
    id = db.Column(db.Integer, autoincrement=True, unique=True, primary_key=True)
    target = db.Column(db.Integer, db.ForeignKey('target.id'))
    url = db.Column(db.String(1024))

    __tablename__ = 'photo'

    def __init__(self, target, url):
        self.target = target
        self.url = url

    def __repr__(self):
        return '<Photo %r>' % self.url


