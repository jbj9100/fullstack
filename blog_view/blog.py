from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from blog_control.user_mgmt import User
from flask_login import login_user, current_user

blog_abtest = Blueprint('blog', __name__)   # 첫번째 인자: blueprint이름, 두번째 인자: 현재파일의 모듈명

@blog_abtest.route('/set_email', methods=['GET', 'POST']) # 라우트에서 둘다 지원하게끔 POST 추가
def set_email():
    if request.method == 'GET':             
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog')) 
    else:
        #print('set_email', request.headers)  
        #print('set_email', request.get_json())  
        print('set_email', request.form['user_email'])      # set_email 사용자가 입력한 email 이 출려된다.
        user = User.create(request.form['user_email'],'A')  # email과 blog_id를 넣어준다, User.create() 인자없이 보내면 DB에 추가한다.
        login_user(user) # 여기서 이미 생선된 세션에 login_user에 user라는 객체를 넣어서 만들고
                         # get_id 메서드로 고유식별자 값을 추출해서 세션ID에 추출된 _user_id를 저장. 
                         # 클라이언트에게 응답할때 set-cookie에 세션을 넣어서 보내야한다.
                         # 그 다음 클라이언트가 다시 요청을 보낼때 request header에 세션정보가 같이 들어온다. 
                         # 서버는 세션 id를 디코딩한다.
        return redirect(url_for('blog.test_blog'))  # url_for모듈과 쓸경우 url_for(blueprint의이름.함수명) 
        # return redirect('/blog/test_blog')        # redirect만 쓸경우 전체 경로 
                                                    # 둘중 어떤 방법을 사용해도 상관 없다.

# POST 방식으로 요청하고 데이터를 가져올 때 request.get_json()을 사용하면 bad request에러가 발생한다.
# 이유는 헤더에 context-Type이 application.x-www-form-urlencoded로 되어있다
# POST에서 context-Type: application/json일 경우에 request.get_json()으로 가져올 수 있고
# POST에서 context-Type: application.x-www-form-urlencode이면 requests.form으로 가져와야 한다.


@blog_abtest.route('/test_blog')
def test_blog():
    if current_user.is_authenticated:
        return render_template('blog_A.html', user_email=) # jinja2 템플릿에서 읽을 user_email 전달