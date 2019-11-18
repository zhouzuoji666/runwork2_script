import requests
import random
import pytest
from common.con_fie import *

# accounts=["lanyi","lianhy"]
sites_sit=[site_sit[0]]
sites_uat=[site_uat[0]]

class TestgetSimpleldap():
    @pytest.mark.parametrize("account",accounts)
    @pytest.mark.parametrize("site", sites_sit)
    def test_ruyitong_getSimpleldap_sit(self,account,site):
        """sit通讯录组织架构"""
        url = site["url"]
        print(url)
        doc = TestgetSimpleldap.test_ruyitong_getSimpleldap_sit.__doc__ + "site[{}]".format(str(site))
        data={"usrLogin":account}
        r = requests.post(url,json=data)
        assert str(r)=="<Response [200]>",doc
        print(r.text)
    @pytest.mark.parametrize("account",accounts)
    @pytest.mark.parametrize("site", sites_uat)
    def test_ruyitong_getSimpleldap_uat(self,account,site):
        """uat通讯录组织架构"""
        url = site["url"]
        print(url)
        doc = TestgetSimpleldap.test_ruyitong_getSimpleldap_uat.__doc__ + "site[{}]".format(str(site))
        data={"usrLogin":account}
        r = requests.post(url,json=data)
        assert str(r)=="<Response [200]>",doc
        print(r.text)
