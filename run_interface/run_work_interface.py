import requests
from business.base_64_ecoding import *
import json
import random
#
site="sit"
site="uat"
userid="CRFNSNY"
username=""
emap_url="https://myd.crc.com.cn/emap/emapservice_v1"
username_emap="lianhy"
apicode_emap = "M0019000008"
token_emap = "ee37702de4d947a40411bc43098db5b6"
#待办
# s="{\"isdone\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:27:17\",\"nodeunid\":\"dc9e9842de0511e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"guodongqiu\",\"username\":\"郭东秋\"},""{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:15:03\",\"nodeunid\":\"0390b612de0411e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"longjun\",\"username\":\"龙均\"},{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:12:05\",\"nodeunid\":\"bd5da002de0311e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"zhangpeng\",\"username\":\"张鹏\"},{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 10:34:56\",\"nodeunid\":\"bb0d08fbddaa11e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"guodongqiu\",\"username\":\"郭东秋\"}],""\"isreaded\":[],""\"istodo\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\""+(date)+"\",\"nodeunid\":\"dd09e0a1de0511e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"whz\",\"username\":\"王宏周\"}],""\"isunread\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:15:04\",\"mobileurl\":\"0064^/h5-supervise/sit/index.html?hiddenNavBar=Y&cr_js_bridge=common¶m=eyJhIjoiIiwidW5pZCI6ImJhZWE0NTIyZGRhYTExZTlhZWI3MDoA1MDU2YTIzZWNmIiwiY29kZSI6ImZ1eXVuaW5nIiwidCI6IkZFRURCQUNLIiwibGRhcCI6IjFERThBMzhEODRBNDQ5QjlCMzQ4Q0MzM0FENzY5QkE2IiwiaWQiOiIyNzk4N2U2MGRlMDQxMWU5YWViNzAwNTA1NmEyM2VjZiIsInN5cyI6IjAwNjQiLCJsIjoiIn0%3D&todo_time_stamp=MjAxOS0wOS0yMyAyMToxNTowNA==&use_wkweb=1&time=$$time$$&todounid=27987e60de0411e9aeb7005056a23ecf\",\"nodeunid\":\"27987e60de0411e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf&nodeId=end&taskType=START\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"fuyuning\",\"username\":\"傅育宁\"}]}"
def my_daiban():
    date = "2019-10-%s %s:%s:%s" % (random.randint(18, 20), random.randint(10, 59), random.randint(10, 59), random.randint(10, 59))
    s = "{\"isdone\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:27:17\",\"nodeunid\":\"dc9e9842de0511e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"guodongqiu\",\"username\":\"郭东秋\"},""{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:15:03\",\"nodeunid\":\"0390b612de0411e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"longjun\",\"username\":\"龙均\"},{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:12:05\",\"nodeunid\":\"bd5da002de0311e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"zhangpeng\",\"username\":\"张鹏\"},{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 10:34:56\",\"nodeunid\":\"bb0d08fbddaa11e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"guodongqiu\",\"username\":\"郭东秋\"}],""\"isreaded\":[],""\"istodo\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"" + (
        date) + "\",\"nodeunid\":\"dd09e0a1de0511e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\""+(userid)+"\",\"username\":\""+(username)+"\"}],""\"isunread\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:15:04\",\"mobileurl\":\"0064^/h5-supervise/sit/index.html?hiddenNavBar=Y&cr_js_bridge=common¶m=eyJhIjoiIiwidW5pZCI6ImJhZWE0NTIyZGRhYTExZTlhZWI3MDoA1MDU2YTIzZWNmIiwiY29kZSI6ImZ1eXVuaW5nIiwidCI6IkZFRURCQUNLIiwibGRhcCI6IjFERThBMzhEODRBNDQ5QjlCMzQ4Q0MzM0FENzY5QkE2IiwiaWQiOiIyNzk4N2U2MGRlMDQxMWU5YWViNzAwNTA1NmEyM2VjZiIsInN5cyI6IjAwNjQiLCJsIjoiIn0%3D&todo_time_stamp=MjAxOS0wOS0yMyAyMToxNTowNA==&use_wkweb=1&time=$$time$$&todounid=27987e60de0411e9aeb7005056a23ecf\",\"nodeunid\":\"27987e60de0411e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf&nodeId=end&taskType=START\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"fuyuning\",\"username\":\"傅育宁\"}]}"
    url="http://myd.crc.com.cn/crcmsapprove_%s/recieveApproveData"%(site)
    s ={
    "mobiledoclink": "0064^/h5-supervise/sit/index.html?hiddenNavBar=Y&cr_js_bridge=common¶m=eyJhIjoiIiwidW5pZCI6ImJhZWE0NTIyZGRhYTExZTlhZWI3MDA1MDU2YTIzZWNmIiwiY29kZSI6Imd1b2RvbmdxaXUiLCJ0IjoiRkVFREJBQ0siLCJsZGFwIjoiMzIyNDZBQTZGRDc2NEM2OUFDMTI1Qjk4Njk0ODNEOTQiLCJpZCI6ImJiMGQwOGZiZGRhYTExZTlhZWI3MDA1MDU2YTIzZWNmIiwic3lzIjoiMDA2NCIsImwiOiIifQ%3D%3D&todo_time_stamp=MjAxOS0wOS0yMyAxMDozNDo1Ng==&use_wkweb=1&time=$$time$$&todounid=bb0d08fbddaa11e9aeb7005056a23ecf",
    "businessunid": "%sbaea4522ddaa11e9aeb7005056a22ecf"%(random.randint(1,1000)),
    "affixdata": "[]",
    "systemcode": "0064",
    "curnode": "立项完成",
    "nodeinfo": s,
    "curapprovename": "郭东秋",
    "title": "%snewdaiban" % (random.randint(1, 10000)),
    "businesstype": "FEEDBACK",
    "maininfo": "{\"baseinfo\":{}}",
    "flowcreatetime": "2019-09-23 10:34:56",
    "businessextendinfo": "",
    "flowstatus": "待结项",
    "businessname": "督办反馈",
    "approvalsn": "006420190923212717574697",
    "createrid": "guodongqiu",
    "creatername": "郭东秋",
    "pcdoclink": "http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf"
}
    print(s["businessunid"])
    value1=return_encodbase64(s)
    # print(value1)
    data={"request_data":value1,
          "esb_sn":"111111111111",
          "esb_sid":"22222222222222222222222222"
                        }
    r = requests.post(url, data = data)
    # print(r)
    print(r.text)

# my_daiban()
# a=0
# while a<=38:
#     my_daiban()
#     a+=1
# 登陆
def common_data(value1,apicode,username,token):
    data = {"biz":{"reqdata":value1},
            "sys":{"apicode":apicode,"ext1":username,"token":token,
                                            "emapsn":"M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                                            "keycode":"pkznf7585535558260675056455817306","appcode":"002601"}}
    return data

def run_login():
    url = "	http://10.0.97.23:6061/runwork/services/ldap/freeLogin"

    data ={"biz":"eyJ1c2VyTmFtZSI6ImxpYW5oeSJ9"}
    r = requests.post(url, data=data)
    print(r.text)
# run_login()
#轮播图
def lunbo_pic():
    url = "https://myd.crc.com.cn/emap/emapservice_v1"
    # url = "	http://10.0.97.23:6061/runwork/services/ldap/freeLogin"
    # value1 = return_encodbase64(s)
    data =  {"biz":{"reqdata":"eyJwYWNrYWdlTmFtZSI6ImNuLmNvbS5jcmMubWFuZ29TSVQiLCJ1c2VyQ29kZSI6ImN5ZCIsImFwcFR5cGUiOiJhIn0="},"sys":{"apicode":"M0026000001","ext1":"cyd","token":"3f7a71104ff134e8b1228d3d6215a6b7","emapsn":"M002601201803151603495e543256c480ac577d30f76f9120eb74569766","keycode":"pkznf7585535558260675056455817306","appcode":"002601"}}
    s=str(data)
    dataStr={"xmas-json":s}
    r = requests.post(url, data=dataStr)
    print(r.text)
# lunbo_pic()
#搜索
def yidong_appsearch():
    url = "https://myd.crc.com.cn/emap/emapservice_v1"
    # url = "	http://10.0.97.23:6061/runwork/services/ldap/freeLogin"
    s={
    "packageName": "cn.com.crc.mangoSIT",
    "appType": "a"
}
    value1 = return_encodbase64(s)
    data = {"biz":{"reqdata":value1},
            "sys":{"apicode":"M0029000005","ext1":"cyd","token":"9faafadd6d99cc10ff16e304d1635896",
                                            "emapsn":"M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                                            "keycode":"pkznf7585535558260675056455817306","appcode":"002601"}}
    s=str(data)
    dataStr={"xmas-json":s}
    r = requests.post(url, data=dataStr)
    print(r.text)
#首页
def run_shouye():
    url = "https://myd.crc.com.cn/emap/emapservice_v1"
    # url = "	http://10.0.97.23:6061/runwork/services/ldap/freeLogin"
    s ={"appPositionCodeList":["RW00010"],
    "userLdap":"lianhy",
    "queryType":"2"
    }
    value1 = return_encodbase64(s)
    data = {"biz": {"reqdata": value1},
            "sys": {"apicode": "M0026000778", "ext1": "lianhy", "token": "be956322c4e872495552133d10c66b06",
                    "emapsn": "M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                    "keycode": "pkznf7585535558260675056455817306", "appcode": "002601"}}
    s = str(data)
    dataStr = {"xmas-json": s}
    r = requests.post(url, data=dataStr)
    print(r.text)
run_shouye()
def run_shouye2():
    url = "https://myd.crc.com.cn/emap/emapservice_v1"
    # url = "	http://10.0.97.23:6061/runwork/services/ldap/freeLogin"
    s ={
  "userLdap": "lianhy",
  "appPositionCodeList": ["RW00010"],
  "saveType": "2",
  "appList": []
}
    value1 = return_encodbase64(s)
    data = {"biz": {"reqdata": value1},
            "sys": {"apicode": "M0026000776", "ext1": "cyd", "token": "cd36af6bd5e4a8a1b58a352134af3d0d",
                    "emapsn": "M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                    "keycode": "pkznf7585535558260675056455817306", "appcode": "002601"}}
    s = str(data)
    dataStr = {"xmas-json": s}
    r = requests.post(url, data=dataStr)
    print(r.text)
# run_shouye2()
#脚标
def run_jiaobiao_sit(username):
    url="http://rxdev.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"
    # url = "http://rxuat.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"
    data={"badge":4,"appkey":"d005c7be806367ca8a0beeee43ba8df1","user":"%s"%(username)}
    # data={"badge":4,"appkey":"3179614bfac948fb9f14411970b8df4f","user":"lianhy"}
    r = requests.post(url, json=data)
    print(r)
    print(r.text)
username="08wfp03"
# run_jiaobiao_sit(username)
def run_jiaobiao_uat():
    url="http://rxuat.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"
    data={"badge":4,"appkey":"c00c18c5dd32479abf9245b619f54ff6","user":"yaoxiuqiong"}
    r = requests.post(url, json=data)
    print(r)
    print(r.text)
# run_jiaobiao_uat()
#润活动
def run_activety():
    url="http://10.0.63.105:7001/activity/services/rest/basic/saveBaseInfo"
    data={
        "businessId"
    }
    pass
#返回账号所有俱乐部ID
def return_club_list():
    url="http://myd.crc.com.cn/crcclub/getCrcclubList"
    s={
        "ldap":"lianhy"
    }
    #编码请求
    value=return_encodbase64(s)
    data={"biz":value}
    r=requests.post(url,data=data)
    req=r.text
    req=json.loads(req)["returnData"]
    #解码响应数据
    req=return_decodebase64(req)
    req=(str(req, encoding = "utf-8"))
    req=json.loads(req)
    # print(req)
    id_list=[]
    for k,y in req.items():
        for i in y:
            for k1,y1 in i.items():
                if k1=="id":
                    # print(y1)
                    id_list.append(y1)
    return id_list
# return_club_list()
# club_detail=return_club_list()
# print(club_detail[0])
#俱乐部详情
def club_detail():
    club_detail = return_club_list()
    club_id=random.choice(club_detail)
    print(club_id)
    url="http://myd.crc.com.cn/crcclub/getCrcclubDetail"
    s={
        "clubId":str(club_id),
        "ldap":"lianhy"}
    # 编码请求
    value = return_encodbase64(s)
    data = {"biz": value}
    r = requests.post(url, data=data)
    req = r.text
    print(req)
# club_detail()
#随机加入俱乐部
def join_club():
    url="http://myd.crc.com.cn/crcclub/submitSignup"
    club_detail = return_club_list()
    club_id = random.choice(club_detail)
    print(club_id)
    s = {
        "clubId": str(club_id),
        "ldap": "lianhy"}
    # 编码请求
    value = return_encodbase64(s)
    data = {"biz": value}
    r = requests.post(url, data=data)
    req = r.text
    print(req)
# join_club()
# def mine_club():
def get_low_email():
    url="http://10.0.97.23:6062/runworkorg/rest/user/getEmailByLdaps"
    data={"biz":"eyJ1c2VyTG9naW4iOiJiYW9qdXRpYW4iLCJ1c2VyaWQiOiJTSVRJNjUtNlMwMSJ9"}
    r=requests.post(url, data=data)
    #解析回包
    req = r.text
    req = json.loads(req)["returnData"]
    req = return_decodebase64(req)
    print(req)
    req = (str(req, encoding="utf-8"))
    req = json.loads(req)
    print(req)
# get_low_email()
def get_high_email():
    url="http://10.0.97.23:6062/runworkorg/rest/user/getEmailByLdaps"
    data={"biz":"eyJ1c2VyTG9naW4iOiJiYW9qdXRpYW4iLCJ1c2VyaWQiOiJ0YW5naHVpNiJ9"}
    r=requests.post(url, data=data)
    # 解析回包
    req = r.text
    req = json.loads(req)["returnData"]
    req = return_decodebase64(req)
    print(req)
    req = (str(req, encoding="utf-8"))
    req = json.loads(req)
    print(req)
# get_high_email()
def common_emap(emap_url,username_emap,apicode_emap,token_emap):
    # site=site
    url = emap_url
    # s = {"isWeb":"false","ldapID":username_emap}
    s={"method":"getInboxEmailList","offset":10,"userid":"%s"%(username_emap),"subject":"蔡翔","propertySet":"","folderId":""}
    value1 = return_encodbase64(s)
    # apicode="M0019000008"
    # token="ee37702de4d947a40411bc43098db5b6"
    data=common_data(value1, apicode_emap, username_emap, token_emap)
    # site="uat"
    s = str(data)
    dataStr = {"xmas-json": s}
    r = requests.post(url, data=dataStr)
    print(r.text)
emap_url="https://myd.crc.com.cn/emap/emapservice_v1"
username_emap="lianhy"
apicode_emap="M0026000216"
token_emap="f8246174c4dc386d73393905417af82b"
# common_emap(emap_url,username_emap,apicode_emap,token_emap)
def year_dayoff():
    site="sit"
    url = emap_url
    s = {"isWeb":"false","ldapID":username_emap}
    value1 = return_encodbase64(s)
    apicode="M0019000008"
    token="ee37702de4d947a40411bc43098db5b6"
    data=common_data(value1, apicode, username_emap, token)
    # site="uat"
    s = str(data)
    dataStr = {"xmas-json": s}
    r = requests.post(url, data=dataStr)
    print(r.text)
# year_dayoff()