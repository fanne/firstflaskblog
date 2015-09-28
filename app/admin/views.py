# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

from flask import render_template,redirect,url_for,current_app,request,flash
from form import PostForm,LabelForm,DeletePostForm
from .import admin
from ..models import Post,Label
from ..import db
from flask.ext.login import  login_required



@admin.route('/',methods=['GET','POST'])
@login_required
def adminer():
    postform = PostForm()
    if postform.validate_on_submit():
        post = Post(title=postform.title.data,
                    body=postform.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.adminer'))
    labelform = LabelForm()
    if labelform.validate_on_submit():
        label = Label(name=labelform.name.data)
        print label
        db.session.add(label)
        db.session.commit()
        return redirect(url_for('.adminer'))


    posts = Post.query.all()
    page = request.args.get('page',1,type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page,per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('admin/admin.html',postform=postform,labelform=labelform,posts=posts)

@admin.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('delete post %s' %id)
    return redirect(url_for('.adminer'))


# @admin.route('/postadd',methods=['GET','POST'])
# def postadd():
#     postform = PostForm()
#     if postform.validate_on_submit():
#         post = Post(title=postform.title.data,
#                     body=postform.body.data)
#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for('.adminer'))
#     return render_template('admin/admin.html',postform=postform)
#
#
#
# @admin.route('postlist',methods=['GET','POST'])
# def postlist():
#     posts = Post.query.all()
#     return render_template('admin/admin',posts=posts)
#
#
#
# @admin.route('/labeladd',methods=['GET','POST'])
# def labeladd():
#     labelform = LabelForm()
#     if labelform.validate_on_submit():
#         label = Label(name=labelform.name.data)
#         print label
#         db.session.add(label)
#         db.session.commit()
#         return redirect(url_for('.adminer'))
#     render_template('admin/admin.html',labelform=labelform)




#
# @admin.route('/label',methods=['GET','POST'])
# def label():
#     form = LabelForm()
#     if form.validate_on_submit():
#         label = Label(name=form.name.data)
#         db.session.add(label)
#         db.session.commit()
#         return redirect(url_for('.label'))
#     return render_template('admin/admin.html',form=form)