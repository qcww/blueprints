#-*- coding:utf-8 -*-
from flask import Blueprint    #不用多说
 
movies=Blueprint('movies',__name__)
@movies.route("/movie")
def movie():
    return '这里是一部好片~'