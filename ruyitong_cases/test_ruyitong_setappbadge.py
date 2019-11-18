import requests
import random
import pytest
from common.con_fie import *


#以下是sit&uat appkey
# app_keys={"dianli_sit":"3179614bfac948fb9f14411970b8df4f","MOA_sit":"8d50d06b1831d2c28a0beeee43ba8df1","MERP_sit":"d005c7be806367ca8a0beeee43ba8df1",
#          "dianli_uat":"c00c18c5dd32479abf9245b619f54ff6","MOA_uat":"1f0578874977427fa6e80ca2852abbc0","MERP_uat":"9a143d1b7ec7e20858be5ce1e61cd0c3",
#           "zaibei_uat":"3bcc6c0c5e2e4486ad743d4a38066e7d"}
from_names=["bf96b05127384cf1886ee6360dd49ea1@apps.rxdev.crc.com.cn","lianhy"]
sites_sit=[site_sit[12]]
sites_uat=[site_uat[12]]
sit_appkeys=["3179614bfac948fb9f14411970b8df4f","8d50d06b1831d2c28a0beeee43ba8df1","d005c7be806367ca8a0beeee43ba8df1"]
class Testruyitongpublicmessage():
    @pytest.mark.parametrize("site", sites_sit)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("appkey", sit_appkeys)
    def test_ruyitong_public_message_sit(self,site,account,appkey):
        """sit设置角标"""
        url = site["url"]
        print(url)
        doc = Testruyitongpublicmessage.test_ruyitong_public_message_sit.__doc__ + "site[{}]".format(str(site))
        data=return_ruyitong_setappbadgedata(appkey,account)
        r = requests.post(url, json=data)
        assert str(r)=="<Response [200]>",doc
        print(r.text)
    @pytest.mark.parametrize("site", sites_uat)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("appkey", sit_appkeys)
    def test_ruyitong_public_message_uat(self,site,account,appkey):
        """uat设置角标"""
        url = site["url"]
        print(url)
        doc = Testruyitongpublicmessage.test_ruyitong_public_message_uat.__doc__ + "site[{}]".format(str(site))
        data=return_ruyitong_setappbadgedata(appkey,account)
        r = requests.post(url, json=data)
        assert str(r)=="<Response [200]>",doc
        print(r.text)

