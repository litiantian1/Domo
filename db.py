# encoding=utf-8
import pymysql

'''数据库操作'''

import pymysql

# 1. 建立连接
conn = pymysql.connect(host='10.41.120.153',
                       port=3306,
                       user='qa_query',
                       passwd='quetest$78Kkhd',  # password也可以
                       db='jxt',
                       charset='utf8')  # 如果查询有中文需要指定数据库编码

# 2. 从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

# 3. 查询数据库（读）
cur.execute("select * from user where name='张三'")

# 4. 获取查询结果
result = cur.fetchall()
print(result)

# 3. 更改数据库（写）
cur.execute("delete from user where name='李四'")

# 4. 提交更改
conn.commit()  # 注意是用的conn不是cur

# 5. 关闭游标及连接
cur.close()
conn.close()

'''封装数据库操作'''

#获取连接方式
def get_db_conn():
    conn=pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='test',
        pssswd='123456',
        db='api_test',
        charset='utf8'
    )
    return conn

#封装数据库查询操作
def query_db(sql):
    conn=get_db_conn()#获取连接
    cur=conn.cursor()#建立游标
    cur.execute(sql)#执行sql
    result=cur.fetchall()#获取所有查询结果
    cur.close()#关闭游标
    conn.close()#关闭连接
    return result #返回结果


#封装更改数据库操作
def change_db(sql):
    conn=get_db_conn() #获取连接
    cur=conn.cursor() # 建立游标
    try:
        cur.execute(sql) #执行sql
        conn.commit() #提交更改
    except Exception as e:
        conn.rollback() #异常回滚
    finally:
        cur.close() #关闭游标
        conn.close() # 关闭连接

#封装常用数据库操作
def chck_user(name):
    #注意sql中''号的嵌套问题
    sql="select * from user where name ='{}'".format(name)
    result=query_db(sql)
    return True if result else  False

def add_user(name,password):
    sql="insert into user (name,passwd) values ('{}','{}') ".format(name,password)
    change_db(sql)

def del_user(name):
    sql="delete from user where name='{}'".format(name)
    change_db(sql)

if __name__=='__main__':
    if chck_user('张三'):
        del_user('张三')

