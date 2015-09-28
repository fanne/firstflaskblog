# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask import  render_template
from flask.ext.login import login_user,redirect,url_for,request,flash,current_user,login_required,logout_user

from .import auth
from form import LogInForm,RegistrationForm
from ..models import User
from ..import db

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me)
            return redirect(request.args.get('next') or url_for('blog.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html',form=form)

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user= User(email = form.email.data,
                   username = form.username.data,
                   password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册完成')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logged out now')
    return redirect(url_for('blog.index'))


