import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host = MYSQL_HOST,
    port = 3306,
    user = 'dave',
    passwd ='funcoding',
    db = 'blog_db',
    charset = 'utf8'    
)

def conn_mysqldb():
    if not MYSQL_CONN.open:  # false면 true여서 재연결
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN