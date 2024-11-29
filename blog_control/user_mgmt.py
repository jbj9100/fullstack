from flask_login import UserMixin
from db_model.mysql import conn_mysqldb  # mysql.py에 보면 db객체정보 리턴하는 함수이다.

class User(UserMixin):  # UserMixin 클래스를 상속받음

    def __init__ (self, user_id, user_email, blog_id):  # User 객체 초기화: 사용자ID, 이메일, 블로그ID를 받아서 저장
        self.id = user_id  # 정수
        self.user_email = user_email
        self.blog_id = blog_id

    def get_id(self):
        return str(self.id)   # Flask-Login은 세션에 사용자 ID를 저장할 때 반드시 문자열 형태로 필요로 함
    

    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()        # MySQL 연결
        db_cursor = mysql_db.cursor()    # SQL 실행을 위한 커서 생성 
        sql = "SELECT * FROM user_info WHERE USER_ID ='" + str(user_id) + "'" # ex) "SELECT * FROM user_info WHERE USER_ID ='123'" 문자열
        #print(sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()    # 결과 한 줄 가져오기
        if not user:                   # 사용자가 없으면 없다고 None 리턴
            return None
        
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2]) # sql 테이블 구조를 보면 USER_ID, USER_EMAIL, BLOG_ID 순이다.
        #print(user)
        return user
    
    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL ='" + str(user_email) + "'"
        #print(sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2]) # sql 테이블 구조를 보면 USER_ID, USER_EMAIL, BLOG_ID 순이다.
        #print(user)
        return user
    

    @staticmethod
    def create(user_email, blog_id):    # email찾았을때 없으면 추가하는 메서드
        user = User.find(user_email) 
        if user == None:                # email이 없으면 DB에 추가
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSTER INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id)) # user_id는 auto_increment라서 추가 안함
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user                 # email이 있으면 user 리턴

