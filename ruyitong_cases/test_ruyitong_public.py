import requests
import random
import pytest
from common.con_fie import *


from_names=["bf96b05127384cf1886ee6360dd49ea1@apps.rxdev.crc.com.cn","lianhy"]
sites_sit=[site_sit[10]]
sites_uat=[site_uat[10]]
class Testruyitongpublicmessage():
    @pytest.mark.parametrize("site", sites_sit)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("from_name", from_names)
    def test_ruyitong_public_message_sit(self,site,account,from_name):
        """sit公众号+消息"""
        url = site["url"]
        print(url)
        doc = Testruyitongpublicmessage.test_ruyitong_public_message_sit.__doc__ + "site[{}]".format(str(site))
        data=return_ruyitpublic_messagedata(from_name, account)
        r = requests.post(url, json=data)
        assert str(r)=="<Response [200]>",doc
        print(r.text)
    @pytest.mark.parametrize("site", sites_uat)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("from_name", from_names)
    def test_ruyitong_public_message_uat(self,site,account,from_name):
        """uat公众号+消息"""
        url = site["url"]
        print(url)
        doc = Testruyitongpublicmessage.test_ruyitong_public_message_uat.__doc__ + "site[{}]".format(str(site))
        data=return_ruyitpublic_messagedata(from_name, account)
        r = requests.post(url, json=data)
        assert str(r)=="<Response [200]>",doc
        print(r.text)

