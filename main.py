#-*- coding:utf-8 -*-
from flask import Flask    # 不用多说
import musics,movies    #导入blueprints目录下musics.py与movies.py模块,
 
app=Flask(__name__)    #创建 Flask()对象： app
 
@app.route('/')  #使用了蓝图，app.route() 这种模式就仍可以使用，注意路由重复的问题
def hello_world():
    return 'home page !'
 
app.register_blueprint(musics.musics)     # 将musics模块里的蓝图对象musics注册到app
app.register_blueprint(movies.movies)     # 将movies模块里的蓝图对象movies注册到app
 
if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0')    #调试模式开 启动服务器 运行在默认的5000端口
