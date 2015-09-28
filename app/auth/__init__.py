# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask import Blueprint
auth = Blueprint('auth',__name__)
from .import view