# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'
from flask import Flask,render_template,request,current_app
from .import blog
from ..models import Post,Label


@blog.route('/',methods=['GET','POST'])
def index():
    #posts = Post.query.order_by(Post.timestamp.desc()).all()
    page = request.args.get('page',1,type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page,per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    labels = Label.query.all()
    return render_template('index.html',posts=posts,pagination=pagination,labels=labels)




@blog.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('blog/post.html',posts=[post])