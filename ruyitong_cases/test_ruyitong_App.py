import requests
import random
import pytest
from common.con_fie import *


# from_names=["bf96b05127384cf1886ee6360dd49ea1@apps.rxdev.crc.com.cn","lianhy"]
sites_sit=[site_sit[11]]
sites_uat=[site_uat[11]]
appkey_keys=["1674c3cc1488587a4d8671d9927d9b3a"]
class TestruyitongApp():
    @pytest.mark.parametrize("site", sites_sit)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("appkey_key", appkey_keys)
    def test_ruyitong_App_sit(self,site,account,appkey_key):
        """sit如意通应用消息"""
        url = site["url"]
        print(url)
        doc = TestruyitongApp.test_ruyitong_App_sit.__doc__ + "site[{}]".format(str(site))
        data=return_ruyitong_App(account, appkey_key)
        r = requests.post(url, json=data)
        assert str(r) == "<Response [200]>",doc
        print(r.text)
    @pytest.mark.parametrize("site", sites_uat)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("appkey_key", appkey_keys)
    def test_ruyitong_App_uat(self,site,account,appkey_key):
        """uat如意通应用消息"""
        url = site["url"]
        print(url)
        doc = TestruyitongApp.test_ruyitong_App_uat.__doc__ + "site[{}]".format(str(site))
        data=return_ruyitong_App(account, appkey_key)
        r = requests.post(url, json=data)
        assert str(r) == "<Response [200]>",doc
        print(r.text)