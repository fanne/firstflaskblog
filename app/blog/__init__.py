# /usr/bin/python
#coding:utf-8

__author__ = 'eyu Fanne'

from flask import Blueprint
blog = Blueprint('blog',__name__)
from .import views

