#-*- coding:utf-8 -*-
from flask import render_template
from flask import Blueprint

MBTI_BP = Blueprint('mbti', __name__)


@MBTI_BP.route('/')
@MBTI_BP.route('/welcome/')
def welcome():
    '''欢迎页面，纯属装逼'''
    return render_template('mbti/welcome.html')


@MBTI_BP.route('/home/')
def home():
    '''这才是真正的首页'''
    return render_template('mbti/home.html')


@MBTI_BP.route('/about/')
def about():
    '''关于页面'''
    return render_template('mbti/about.html')


@MBTI_BP.route('/personalities/')
def personalities():
    '''关于页面'''
    return render_template('mbti/personalities.html')


@MBTI_BP.route('/test/', methods=('GET, POST'))
def test():
    '''测试页面视图'''
    return render_template('mbti/test.html')
