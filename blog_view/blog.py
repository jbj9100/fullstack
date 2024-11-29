from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for

blog_abtest = Blueprint('blog', __name__)   # 첫번째 인자: blueprint이름, 두번째 인자: 현재파일의 모듈명

@blog_abtest.route('/set_email', methods=['GET'])
def set_email():
    print('set_email', request.args.get('user_email'))
    return redirect(url_for('blog.test_blog'))  # url_for모듈과 쓸경우 url_for(blueprint의이름.함수명) 
    # return redirect('/blog/test_blog')        # redirect만 쓸경우 전체 경로 
                                                # 둘중 어떤 방법을 사용해도 상관 없다.

@blog_abtest.route('/set_email', methods=['GET', 'POST']) # 라우트에서 둘다 지원하게끔 POST 추가
def set_email():
    if redirect.method == 'GET':             
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.test_blog')) 
    else:
        #print('set_email', request.headers)  
        print('set_email', request.form)      
        #print('set_email', request.get_json())  
        return redirect(url_for('blog.test_blog')) 

# POST 방식으로 요청하고 데이터를 가져올 때 request.get_json()을 사용하면 bad request에러가 발생한다.
# 이유는 헤더에 context-Type이 application.x-www-form-urlencoded로 되어있다
# POST에서 context-Type: application/json일 경우에 request.get_json()으로 가져올 수 있고
# POST에서 context-Type: application.x-www-form-urlencode이면 requests.form으로 가져와야 한다.


@blog_abtest.route('/test_blog')
def test_blog():
    return render_template('blog_A.html')