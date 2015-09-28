# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

import os
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand

from app import creat_app,db
from app.models import Post,Label


app = creat_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,Post=Post,Label=Label)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()
