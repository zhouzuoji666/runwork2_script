from business.base_64_ecoding import *
import requests
account="lianhy"
apicode="M0026000001"
tocken="cd36af6bd5e4a8a1b58a352134af3d0d"
def run_shouye2(account,apicode,tocken):
    url = "https://myd.crc.com.cn/emap/emapservice_v1"
    # url = "	http://10.0.97.23:6061/runwork/services/ldap/freeLogin"
    s ={
  "userLdap": "%s"%(account),
  "appPositionCodeList": ["RW00010"],
  "saveType": "2",
  "appList": []
}
    value1 = return_encodbase64(s)
    data = {"biz": {"reqdata": value1},
            "sys": {"apicode": "%s"%(apicode), "ext1": "cyd", "token": "%s"%(tocken),
                    "emapsn": "M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                    "keycode": "pkznf7585535558260675056455817306", "appcode": "002601"}}
    s = str(data)
    dataStr = {"xmas-json": s}
    r = requests.post(url, data=dataStr)
    print(r.text)
# run_shouye2(account,apicode,tocken)
account="lianhy"
apicode="M0026000001"
tocken="cd36af6bd5e4a8a1b58a352134af3d0d"
def run_active(account,apicode,tocken):
    url = "https://myd.crc.com.cn/emap/emapservice_v1"
    # url = "	http://10.0.97.23:6061/runwork/services/ldap/freeLogin"
    s ={
  "userLdap": "%s"%(account),
  "appPositionCodeList": ["RW00010"],
  "saveType": "2",
  "appList": []
}
    value1 = return_encodbase64(s)
    data = {"biz": {"reqdata": value1},
            "sys": {"apicode": "%s"%(apicode), "ext1": "cyd", "token": "%s"%(tocken),
                    "emapsn": "M002601201803151603495e543256c480ac577d30f76f9120eb74569766",
                    "keycode": "pkznf7585535558260675056455817306", "appcode": "002601"}}
    s = str(data)
    dataStr = {"xmas-json": s}
    r = requests.post(url, data=dataStr)
    print(r.text)
# run_active(account,apicode,tocken)
# tp=(1,2,3)
# d={}
# # tp=list(tp)
# for i in tp:
#     # print(i)
#     d[i]=i
#     #
#     # print(type(i))
# # print(d)
# a=0
# for y in d.values():
#     print(y)
#     if y!=1:
#         a=a+y
#     elif y==1:
#         a=a-y
#
#
# print(a)
tp=(1,2,3,4,5,6)
def return_tp(tp):
    s=0
    for i in tp:
        if i not in [2,3]:
            s=s+i
        else:
            s=s-i
    return s
print (return_tp(tp))