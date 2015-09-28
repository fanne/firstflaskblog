#!/bin/sh

manage_dir=/data/script/python/flask_myblog_tranning/manage.py
echo $manage_dir
python manage.py runserver --host=0.0.0.0 --port=5004 -d -r
