from business.base_64_ecoding import *
#
#
# # site_sit={"url":"http://rxdev.crc.com.cn:9191"}
# # site_uat={"url":""}
# site_sit=[{"url":"http://10.0.97.23:6062/runworkorg/rest/user/getSimpleEmpByLdap"
#           },{"url":"http://10.0.97.23:8038/email/services/rest/email/doEmail"
#           },{"url":"http://10.0.97.23:8080/card/rest/card/listTodayCard"
#           },{"url":"http://10.0.97.23:8038/exchange/services/calendar/calendarSearchApi"
#           },{"url":"http://10.0.97.23:8035/crcschedule/selectScheduleTeamList"
#           },{"url":"http://10.0.97.23:8080/leader_phone_book/phonebook/getCompanyList.do"
#           }
#           ]


# site_sit={"url":"http://rxdev.crc.com.cn:9191"}
# site_uat={"url":""}

accounts=["lanyi","lianhy"]

site_sit=[{"url":"http://10.0.97.23:6062/runworkorg/rest/user/getSimpleEmpByLdap"
          },{"url":"http://10.0.97.23:8038/email/services/rest/email/doEmail"#site1获取邮箱
          },{"url":"http://10.0.97.23:8080/card/rest/card/listTodayCard"
          },{"url":"http://10.0.97.23:8038/exchange/services/calendar/calendarSearchApi"
          },{"url":"http://10.0.97.23:8035/crcschedule/selectScheduleTeamList"
          },{"url":"http://10.0.97.23:8080/leader_phone_book/phonebook/getCompanyList.do"
          },{"url":"http://runworksit.crc.com.cn/runworklark/hello"# site6登陆
          },{"url":"http://runworksit.crc.com.cn/runworklark/hello"# site7数据同步
          },{"url":"http://myd.crc.com.cn/crcmsapprove_sit/recieveApproveData"# site8审批待办
          },{"url":"https://myd.crc.com.cn/emap/emapservice_v1"# site9首页
          },{"url":"http://rxdev.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"#site10如意通公众号+消息
          },{"url":"http://rxdev.crc.com.cn:9191/rest/app/sendmsg?rtpwebid=crc"#site11如意通应用消息
          },{"url":"http://rxdev.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"#site12如意通角标设置
          }
          ]
site_uat=[{"url":"http://myd.crc.com.cn/runworkorg_uat/rest/user/getSimpleEmpByLdap"
          },{"url":"http://10.0.97.23:8038/email/services/rest/email/doEmail"
          },{"url":"http://10.0.97.23:8080/card/rest/card/listTodayCard"
          },{"url":"http://10.0.97.23:8038/exchange/services/calendar/calendarSearchApi"
          },{"url":"http://10.0.97.23:8035/crcschedule/selectScheduleTeamList"
          },{"url":"http://10.0.97.23:8080/leader_phone_book/phonebook/getCompanyList.do"
          },{"url":"http://runworksit.crc.com.cn/runworklark/hello"# site6登陆
          },{"url":"http://runworksit.crc.com.cn/runworklark/hello"# site7数据同步
          },{"url":"http://myd.crc.com.cn/crcmsapprove_sit/recieveApproveData"# site8审批待办
          },{"url":"https://myd.crc.com.cn:9443/emap/emapservice_v1"# site9首页
          },{"url":"http://rxuat.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"#site10如意通公众号+消息
          },{"url":"http://rxuat.crc.com.cn:9191/rest/app/sendmsg?rtpwebid=crc"#site11如意通应用消息
          },{"url":"http://rxdev.crc.com.cn:9191/rest/app/setappbadge?rtpwebid=crc"#site12如意通角标设置
          }
          ]

# site6登陆 site7数据同步,site8 审批待办 site9轮播图



# username
def return_lunbopicdata(username):
    data={"biz": {
        "reqdata": "eyJwYWNrYWdlTmFtZSI6ImNuLmNvbS5jcmMubWFuZ29TSVQiLCJ1c2VyQ29kZSI6ImN5ZCIsImFwcFR5cGUiOiJhIn0="},
        "sys": {"apicode": "M0026000001", "ext1": username, "token": "3f7a71104ff134e8b1228d3d6215a6b7",
                "emapsn": "M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                "keycode": "pkznf7585535558260675056455817306", "appcode": "002601"}}
    return data
def return_indexdata(username,token):
    s ={"appPositionCodeList":["RW00010"],
    "userLdap":username,
    "queryType":"2"
    }
    value1 = return_encodbase64(s)
    data = {"biz": {"reqdata": value1},
            "sys": {"apicode": "M0026000778", "ext1": username ,"token": token,
                    "emapsn": "M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                    "keycode": "pkznf7585535558260675056455817306", "appcode": "002601"}}
    return data
def return_ruyitpublic_messagedata(from_name,username):
    data = {
        "from": from_name,
        "to": username,
        "msgType": "normal",
        "body": "%s呵%s呵" % (random.randint(1, 10000), random.randint(1, 10000))
    }
    return data
def return_ruyitong_App(username,appkey_key):
        data={
        "to":username,
        "body":"%s最早在消息ww内容啊"%(random.randint(1,1000)),
        "subject":"发送消息",
        "msgType":"chat",
        "appKey":appkey_key
    }
        return data
def return_shenpidata(user):
    date = "2019-10-%s %s:%s:%s" % (
    random.randint(18, 20), random.randint(10, 59), random.randint(10, 59), random.randint(10, 59))
    s1 = "{\"isdone\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:27:17\",\"nodeunid\":\"dc9e9842de0511e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"guodongqiu\",\"username\":\"郭东秋\"},""{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:15:03\",\"nodeunid\":\"0390b612de0411e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"longjun\",\"username\":\"龙均\"},{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:12:05\",\"nodeunid\":\"bd5da002de0311e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"zhangpeng\",\"username\":\"张鹏\"},{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 10:34:56\",\"nodeunid\":\"bb0d08fbddaa11e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"guodongqiu\",\"username\":\"郭东秋\"}],""\"isreaded\":[],""\"istodo\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"" + (
        date) + "\",\"nodeunid\":\"dd09e0a1de0511e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"" + (
             list(user.keys())[0]) + "\",\"username\":\"" + (
             list(user.values())[
                 0]) + "\"}],""\"isunread\":[{\"extendinfo\":\"\",\"isonline\":\"yes\",\"lastupdatetime\":\"2019-09-23 21:15:04\",\"mobileurl\":\"0064^/h5-supervise/sit/index.html?hiddenNavBar=Y&cr_js_bridge=common¶m=eyJhIjoiIiwidW5pZCI6ImJhZWE0NTIyZGRhYTExZTlhZWI3MDoA1MDU2YTIzZWNmIiwiY29kZSI6ImZ1eXVuaW5nIiwidCI6IkZFRURCQUNLIiwibGRhcCI6IjFERThBMzhEODRBNDQ5QjlCMzQ4Q0MzM0FENzY5QkE2IiwiaWQiOiIyNzk4N2U2MGRlMDQxMWU5YWViNzAwNTA1NmEyM2VjZiIsInN5cyI6IjAwNjQiLCJsIjoiIn0%3D&todo_time_stamp=MjAxOS0wOS0yMyAyMToxNTowNA==&use_wkweb=1&time=$$time$$&todounid=27987e60de0411e9aeb7005056a23ecf\",\"nodeunid\":\"27987e60de0411e9aeb7005056a23ecf\",\"pcurl\":\"http://svmssit.crc.com.cn/matterForm.html?cId=baea4522ddaa11e9aeb7005056a23ecf&nodeId=end&taskType=START\",\"permission\":\"\",\"priority\":\"\",\"userid\":\"fuyuning\",\"username\":\"傅育宁\"}]}"
    s = {
        "mobiledoclink": "0064^/h5-supervise/sit/index.html?hiddenNavBar=Y&cr_js_bridge=common¶m=eyJhIjoiIiwidW5pZCI6ImJhZWE0NTIyZGRhYTExZTlhZWI3MDA1MDU2YTIzZWNmIiwiY29kZSI6Imd1b2RvbmdxaXUiLCJ0IjoiRkVFREJBQ0siLCJsZGFwIjoiMzIyNDZBQTZGRDc2NEM2OUFDMTI1Qjk4Njk0ODNEOTQiLCJpZCI6ImJiMGQwOGZiZGRhYTExZTlhZWI3MDA1MDU2YTIzZWNmIiwic3lzIjoiMDA2NCIsImwiOiIifQ%3D%3D&todo_time_stamp=MjAxOS0wOS0yMyAxMDozNDo1Ng==&use_wkweb=1&time=$$time$$&todounid=bb0d08fbddaa11e9aeb7005056a23ecf",
        "businessunid": "%sbaea4522ddaa11e9aeb7005056a22ecf" % (random.randint(1, 1000)),
        "affixdata": "[]",
        "systemcode": "0064",
        "curnode": "立项完成",
        "nodeinfo": s1,
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

    value1 = return_encodbase64(s)
    data = {"request_data": value1,
            "esb_sn": "111111111111",
            "esb_sid": "22222222222222222222222222"
            }
    return data
def return_ruyitong_setappbadgedata(app_key,username):
    data = {"badge": 4, "appkey": app_key, "user": username}
    return data
def return_emaildata(username):
    data={"biz": {"method": "getInboxEmailList", "offset": 10, "userid": username ,"subject": "蔡翔", "propertySet": "itemSender",
          "folderId": ""}}
    return data
