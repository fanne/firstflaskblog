# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'
import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.pagedown import PageDown
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootsrtap = Bootstrap()
db = SQLAlchemy()
pagedown = PageDown()


def creat_app(config_name):
    app = Flask(__name__)
    bootsrtap.init_app(app)
    db.init_app(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)


    from blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    from admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix='/admin')

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app
