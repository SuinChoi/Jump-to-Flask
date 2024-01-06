from flask import Blueprint
# __name__ is the main_views
# main is the alais, this will be used in url_for in the future
# url_prefix means what hello_pybo will call this time it will call localhost:5000/
# if it is url_prefix = '/main' the hello_pybo will call localhost:5000/main/
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo :)'

@bp.route('/')
def index():
    return 'Pybo index'

# 라우팅 함수가 추가되더라도 main_view에 추가하기때문에 create_app이 안 뚱뚱해짐
# Gonna add routing functions on main_views so create_app will not be fat