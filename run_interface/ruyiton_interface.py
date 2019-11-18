import requests
import random
import pymysql
import pytest
import time

import pymysql.cursors

url_sit = "http://rxdev.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"
url_uat= "http://rxuat.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"
username="wlpjn"
key="77f2b9ef710ef87a4d8671d9927d9b3a@apps.rxuat.crc.com.cn"
key="478b533a13e24f90834801c626cd7487@apps.rxdev.crc.com.cn"

number=19
app_keys={"dianli_sit":"3179614bfac948fb9f14411970b8df4f","MOA_sit":"8d50d06b1831d2c28a0beeee43ba8df1","MERP_sit":"d005c7be806367ca8a0beeee43ba8df1",
         "dianli_uat":"c00c18c5dd32479abf9245b619f54ff6","MOA_uat":"1f0578874977427fa6e80ca2852abbc0","MERP_uat":"9a143d1b7ec7e20858be5ce1e61cd0c3",
          "zaibei_uat":"3bcc6c0c5e2e4486ad743d4a38066e7d"}
app_key=app_keys["zaibei_uat"]
from_name={"gongzhonghao":"bf96b05127384cf1886ee6360dd49ea1@apps.rxdev.crc.com.cn","ldap":"lianhy"}
appkey_key="1674c3cc1488587a4d8671d9927d9b3a"
# app_key=app_keys["MERP_sit"]


# site="sit"
#测试app轻应用脚标需要改的参数有，site环境，设置脚标数，app_key值
def common_qing(connection,username,number):
    cursor = connection.cursor()
    # print(cursor)
    # select badge from rwork_app_user_badge where user_id="lianhy";
    # update rwork_app_user_badge set badge = 6 where user_id = 'lianhy';
    # sql="select * from rwork_app_user_badge where user_id='lianhy';"
    # sql="select * from rwork_app_user_badge where user_id='lianhy';"
    # sql="update rwork_app_user_badge set badge = 8 where user_id = 'lianhy';"
    # sql="update rwork_app_user_badge set badge = 10 where user_id = 'lianhy' and app_key='d005c7be806367ca8a0beeee43ba8df1';"
    # sql="update rwork_app_user_badge set badge = 11 where user_id = 'lianhy' and app_key='3179614bfac948fb9f14411970b8df4f';"
    # sql="update rwork_app_user_badge set badge = 16 where user_id = 'lianhy' and app_key='8d50d06b1831d2c28a0beeee43ba8df1';"
    sql="select * from rwork_app_user_badge where user_id='%s';"%(username)
    d=cursor.execute(sql)
    q=cursor.fetchall()
    for i in q:
        print(i)
    # sql="update rwork_app_user_badge set badge = %s where user_id = '%s' and app_key='%s';"%(number,username,app_key)
    # sql="update rwork_app_user_badge set badge = %s where user_id = '%s' and app_key='%s';"%(number,username,app_key)
    sql="update rwork_app_user_badge set badge = %s where user_id = '%s' and app_key='%s';"%(number,username,app_key)
    d=cursor.execute(sql)
    z=cursor.execute("commit")
    sql="select * from rwork_app_user_badge where user_id='%s';"%(username)
    d=cursor.execute(sql)
    d=cursor.fetchall()
    for i in d:
        print(i)
def qing_app(app_key,username,number):
    site = "sit"
    site="uat"
    if site=="sit":
        # qing_app_sql_sit()
        connection = pymysql.connect(host='10.0.97.24',
                                     user='runworksit',
                                     password='runworksit',
                                     db='runwork_badge',
                                     charset='utf8mb4',
                                     )
        common_qing(connection,username,number)
        url = "http://rxdev.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"
        data = {"badge": 4, "appkey": "%s" % (app_key), "user": "%s" % (username)}
        # data = {"badge": 4, "appkey": "d005c7be806367ca8a0beeee43ba8df1", "user":"%s"%(username)}
        # data={"badge":4,"appkey":"3179614bfac948fb9f14411970b8df4f","user":"%s"%(username)}
        r = requests.post(url, json=data)
        print(r)
        print(r.text)
    elif site=="uat":
        connection = pymysql.connect(host='10.0.55.160',
                                     user='runworkuat',
                                     password='runworkuat',
                                     db='runwork_badge_uat',
                                     charset='utf8mb4',
                                     )
        common_qing(connection,username,number)
        url = "http://rxuat.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"
        data = {"badge": 4, "appkey": "%s" % (app_key), "user": "%s" % (username)}
        # data = {"badge": 4, "appkey": "d005c7be806367ca8a0beeee43ba8df1", "user":"%s"%(username)}
        # data={"badge":4,"appkey":"3179614bfac948fb9f14411970b8df4f","user":"%s"%(username)}
        r = requests.post(url, json=data)
        print(r)
        print(r.text)
qing_app(app_key,username,number)
def common_shenpi_api(connection,username):
    cursor = connection.cursor()
    sql="select * from busi_node where node_type='done' and user_id='%s';"%(username)
    node_type=[]
    d = cursor.execute(sql)
    q=cursor.fetchall()
    print(username)

    for i in q:
        print(i[0])
        node_type.append(i[0])
    print(node_type)
    id=random.choice(node_type)
    if node_type==[]:
        sql="update busi_node set node_type='done' where user_id='%s';"%(username)
        d = cursor.execute(sql)
        d = cursor.execute("commit")
        sql = "select * from busi_node where node_type='done' and user_id='%s';"%(username)
        node_type = []
        d = cursor.execute(sql)
        q = cursor.fetchall()
        for i in q:
            # print(i[0])
            node_type.append(i[0])
        id = random.choice(node_type)
        sql = "update busi_node set node_type='todo' where user_id='%s' and id='%s';" % (username,id)
        d = cursor.execute(sql)
        d = cursor.execute("commit")
    elif node_type!=[]:
        sql="update busi_node set node_type='todo' where user_id='%s' and id='%s';"%(username,id)
        d = cursor.execute(sql)
        d=cursor.execute("commit")
        sql="select count(*) from busi_node where user_id='%s' and node_type='todo';"%(username)
        d = cursor.execute(sql)
        # print(d)
        q=cursor.fetchall()
        for i in q:
            print(i)
def shenpi_app(username,key):
    site="sit"
    # site="uat"
    if site=="sit":
        connection = pymysql.connect(host='10.0.55.160',
                                     user='crcms_sit',
                                     password='crcms_sit',
                                     db='crcms_approve',
                                     charset='utf8mb4',
                                     )
        common_shenpi_api(connection, username)
        url = "http://rxdev.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"
        # url = "http://rxuat.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"
        # url="http://rxuat.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"
        data = {"extension": "", "msgType": "normal", "from": "%s" % (key),
                "to": "%s" % (username), "body": "(售电交易经理)2019-贵州电网-售电侧年度零售交易方案"}
        r = requests.post(url, json=data)
        print(r)
        print(r.text)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    elif  site=="uat":
        connection = pymysql.connect(host='10.0.49.160',
                                     user='crcms_uat',
                                     password='crcms_uat',
                                     db='crcms_approve',
                                     charset='utf8mb4',
                                     )
        common_shenpi_api(connection, username)
        url = "http://rxdev.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"
        url = "http://rxuat.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"
        # url="http://rxuat.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"
        data = {"extension": "", "msgType": "normal", "from": "%s" % (key),
                "to": "%s" % (username), "body": "(售电交易经理)2019-贵州电网-售电侧年度零售交易方案"}
        r = requests.post(url, json=data)
        print(r)
        print(r.text)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# shenpi_app(username,key)
def test_ruyitong_gongzhonghao(from_name,username):
    url=url_sit
    data = {
    "from":"%s"%(from_name["gongzhonghao"]),
    "to":"%s"%(username),
    "msgType":"normal",
    "body":"%s呵%s呵"%(random.randint(1,10000),random.randint(1,10000))
}
    r = requests.post(url, json=data)
    print(r)
    assert str(r)=="<Response [200]>"
    print(r.text)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# test_ruyitong_gongzhonghao(from_name,username)
def test_ruyitong_ldap_message(from_name,username):
    url=url_sit
    data = {
    "from":"%s"%(from_name["ldap"]),
    "to":"%s"%(username),
    "msgType":"normal",
    "body":"%s呵%s呵"%(random.randint(1,10000),random.randint(1,10000))
}
    r = requests.post(url, json=data)
    print(r)
    # assert str(r)=="<Response [200]>"
    # print("zzzzzzzzzzzzzzzzz")
    print(r.text)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# test_ruyitong_gongzhonghao(from_name,username)
def ruyiton_APPmessages(appkey_key,username):
    site="uat"
    if site=="sit":
        url="http://rxdev.crc.com.cn:9191/rest/app/sendmsg?rtpwebid=crc"
        data={
        "to":"%s"%(username),
        "body":"%s最早在消息ww内容啊"%(random.randint(1,1000)),
        "subject":"发送消息",
        "msgType":"chat",
        "appKey":"%s"%(appkey_key)
    }
        print("body:%s"%(data["body"]))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("username:%s"%(username))
        r=requests.post(url,json=data)
        print(r)
        # print("zzzzzzzzzzz")
        print(r.text)
    elif site=="uat":
        url = "http://rxuat.crc.com.cn:9191/rest/app/sendmsg?rtpwebid=crc"

        data = {
            "to": "%s" % (username),
            "body": "%s最早在消息ww内容啊" % (random.randint(1, 1000)),
            "subject": "发送消息",
            "msgType": "chat",
            "appKey": "%s" % (appkey_key)
        }
        r = requests.post(url, json=data)
        print(r)
        print("zzzzzzzzzzz")
        print(r.text)
username="lianhy"
ruyiton_APPmessages(appkey_key,username)
def shenpi_jiaobiao_sit_uat(username):
    url=url_uat
    data={"extension": "", "msgType": "normal", "from": "%s"%(key),
     "to": "%s"%(username), "body": "(售电交易经理)2019-贵州电网-售电侧年度零售交易方案"}
    r = requests.post(url, json=data)
    print(r)
    print(r.text)
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# shenpi_jiaobiao_sit_uat(username)
#