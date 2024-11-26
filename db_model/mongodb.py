import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))


def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')   # MongoDB 연결 상태 확인
        # 데이터베이스와 컬렉션 접근
        # blog_session_db: 데이터베이스 이름
        # blog_ab: 컬렉션 이름
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        # 연결 실패시 재연결 시도
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    
    # 컬렉션 객체 반환
    return blog_ab
