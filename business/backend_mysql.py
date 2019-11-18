import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='10.0.97.24',
                             user='runworksit',
                             password='runworksit',
                             db='runwork_badge',
                             charset='utf8mb4',
                             )
cursor = connection.cursor()
# print(cursor)
# select badge from rwork_app_user_badge where user_id="lianhy";
# update rwork_app_user_badge set badge = 6 where user_id = 'lianhy';
# sql="select * from rwork_app_user_badge where user_id='lianhy';"
# sql="select * from rwork_app_user_badge where user_id='lianhy';"
# sql="update rwork_app_user_badge set badge = 8 where user_id = 'lianhy';"
# sql="update rwork_app_user_badge set badge = 10 where user_id = 'lianhy' and app_key='d005c7be806367ca8a0beeee43ba8df1';"
# sql="update rwork_app_user_badge set badge = 11 where user_id = 'lianhy' and app_key='3179614bfac948fb9f14411970b8df4f';"
sql="select * from rwork_app_user_badge where user_id='lianhy';"
d=cursor.execute(sql)
q=cursor.fetchall()
for i in q:
    print(i)
sql="update rwork_app_user_badge set badge = 19 where user_id = 'lianhy';"
d=cursor.execute(sql)
z=cursor.execute("commit")
sql="select * from rwork_app_user_badge where user_id='lianhy';"
d=cursor.execute(sql)
d=cursor.fetchall()
for i in d:
    print(i)


# sql="update rwork_app_user_badge set badge = 4 where user_id = '%s' and app_key = '%s';"
# useid="lianhy"
# appkey="d005c7be806367ca8a0beeee43ba8df1"
# # cursor.execute(sql,(useid,appkey))
# try:
#     #批量执行多条插入SQL语句
#     cursor.execute(sql, (useid, appkey))
#     #提交事务
#     result = cursor.fetchone()
#     print("ggggggggggggggggggggg")
#     print(result)
#     connection.commit()
# except Exception as e:
#     #有异常，回滚事务
#     print("zzzzzzzzzzzzzzzzzz")
#     connection.rollback()
# cursor.close()
# connection.close()
# # try:
# #     with connection.cursor() as cursor:
# #         # Create a new record
# #         sql = "'update rwork_app_user_badge set badge = 4 where user_id = 'lianhy' and app_key = 'd005c7be806367ca8a0beeee43ba8df1';'"
# #         cursor.execute(sql)
# #
# #     # connection is not autocommit by default. So you must commit to save
# #     # your changes.
# #     connection.commit()
# #
# #     with connection.cursor() as cursor:
# #         # Read a single record
# #         sql = "'update rwork_app_user_badge set badge = 4 where user_id = 'lianhy' and app_key = 'd005c7be806367ca8a0beeee43ba8df1';'"
# #         cursor.execute(sql)
# #         result = cursor.fetchone()
# #         print(result)
# # finally:
# #     connection.close()
# # # sql = "'update rwork_app_user_badge set badge = 4 where user_id = 'lianhy' and app_key = 'd005c7be806367ca8a0beeee43ba8df1';'"