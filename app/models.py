# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from .import db
import time,datetime
from datetime import *
from markdown import markdown
import bleach
from  flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from .import login_manager


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)

    @staticmethod
    def on_changed_body(target,value,oldvalue,initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value,output_format='html'),
            tags=allowed_tags,strip=True
        ))
db.event.listen(Post.body,'set',Post.on_changed_body)

class Label(db.Model):
    __tablename__ = 'labels'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Label %r>' %self.name

class User(UserMixin,db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




