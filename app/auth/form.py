# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField,BooleanField,ValidationError
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from ..models import User


class LogInForm(Form):
    email = StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log in')

class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    username = StringField('Username',validators=[Required(),Length(1,64),Regexp('^[A-Za-z0-9_.]*$',0,
                                                                                 'Username must have only letters,'
                                                                                 'numbers,dots or underscores')])
    password = PasswordField('Password',validators=[Required(),EqualTo('password2',message='Passwords must macth.')])
    password2 = PasswordField('Confirm password',validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username in use')
