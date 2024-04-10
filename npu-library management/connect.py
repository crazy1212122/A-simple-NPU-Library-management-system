import pymysql
def connect():
    conn = pymysql.connect(host='localhost', user='root',password='',database='npulib')#连接数据库library，用户和密码按需修改
    cursor = conn.cursor()
    return cursor, conn