from app import db, r
from models import *

def update_target_urls(text):
    try:
        print(text)
        new = Target(text)
        db.session.add(new)
        db.session.commit()
        r.set(new.id, text)
        return True
    except:
        db.session.rollback()
        return False


def show_targets():
    return [[row.url, row.is_ready] for row in Target.query.all()]

def show_photos(target):
    return [[row.id, row.url] for row in Photo.query.join(Target, Photo.target == Target.id).filter(Target.url == target).all()]