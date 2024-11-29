from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog   # blog 모듈 사용하기             blog_view패키지안에 blog.py(모듈)사용하기
from blog_control.user_mgmt import User  # User 모듈 사용하기  blog_control.user_mgmt 패키지.user_mgmt(모듈)안에서 User클래스 사용하기
import os 

# https 만을 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')  # html가져올 경로
CORS(app)
app.secret_key = 'dave_server'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog') # blog_view.blog모듈에서 blog_abtest는 blog.py에서 blueprint 객체가 담긴 변수이다.

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)