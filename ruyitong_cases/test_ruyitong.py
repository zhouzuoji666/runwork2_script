import requests
import random
import pytest

accounts=["lanyi","lianhy"]


class Testruyitong():
    @pytest.mark.parametrize("account",accounts)
    def test_ruyitong_gongzhonghao(self,account):
        url = "http://rxdev.crc.com.cn:9191/rest/common/sendmsg?rtpwebid=crc"

        data = {
        "from":"bf96b05127384cf1886ee6360dd49ea1@apps.rxdev.crc.com.cn",
        "to":account,
        "msgType":"normal",
        "body":"啦啦了%s"%(random.randint(1,100))
    }
        r = requests.post(url, json=data)
        assert str(r)=="<Response [200]>"
        print("zzzzzzzzzzzzzzzzz")
        print(r.text)
    #
    @pytest.mark.parametrize("account", accounts)
    def test_ruyitong_APP(self, account):
        url="http://rxuat.crc.com.cn:9191/rest/app/sendmsg?rtpwebid=crc"
        data = {
            "to": "lianhy",
            "body": "消息ww内容啊",
            "subject": "发送消息",
            "msgType": "chat",
            "appKey": "1674c3cc1488587a4d8671d9927d9b3a"
        }
        r=requests.post(url,json=data)
        assert str(r) == "<Response [200]>"
        print("zzzzzzzzzzzzzzzzz")
        print(r.text)