from db_model.mongodb import conn_mongodb
from datetime import datetime

class BlogSession():
    blog_page = {'A':'blog_A.html', 'B':'blog_B.html'} # blog_id를 A, B로 만듬 blog_page[A]는 blog_A.html
    session_count = 0                  # 세션 카운트 변수 (A/B 페이지 번갈아 보여주기 위함)

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name): # 접속할때마다 접속기록을 mongodb에 저장
        now = datetime.now()  # save_session_info함수를 호출한 시간을 now에 저장함
        now_time = now.strftime("%Y-%Mm-%d %H:%M:%S") # 시간을 문자열로 변환

        mongo_db = conn_mongodb()
        mongo_db.insert_one({             # 세션 정보를 MongoDB에 저장
            'session_ip': session_ip,
            'user_email': user_email,
            'page': webpage_name,
            'access_time': now_time
        })

    @staticmethod
    def get_blog_page(blog_id=None):  # blog_id가 없으면 A/B페이지를 번갈아가며 반환
        if blog_id == None:
            if BlogSession.session_count == 0:   # 50:50으로 반환
                BlogSession.session_count = 1
                return 'blog_A.html'
            else:
                BlogSession.session_count = 0
                return 'blog_B.html'
        else:
            return BlogSession.blog_page[blog_id]  # blog_id가 있다면 A면 A페이지, B면 B페이지를 반환