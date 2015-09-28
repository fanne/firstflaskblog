# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from ..models import Post
from flask.ext.wtf import Form
from wtforms import TextAreaField,SubmitField,StringField,ValidationError
from wtforms.validators import Required
from flask.ext.pagedown.fields import PageDownField
from ..models import Label


class PostForm(Form):
    title = TextAreaField('Post title',validators=[Required()])
    body = PageDownField('New Post.',validators=[Required()])
    submit = SubmitField('Submit')

class LabelForm(Form):
    name = StringField('Label',validators=[Required()])
    submit =SubmitField('Submit')

    def validate_name(self,field):
        if Label.query.filter_by(name=field.data).first():
            raise ValidationError('该标签已添加过.')

class DeletePostForm(Form):
    submit = SubmitField()