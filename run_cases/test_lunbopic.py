import requests
import random
import pytest
from common.con_fie import *


sites_sit=[site_sit[9]]
sites_uat=[site_uat[9]]
class Testlunbo_pic():
    @pytest.mark.parametrize("site", sites_sit)
    @pytest.mark.parametrize("account", accounts)
    def test_lunbo_pic(self,site,account):
        """sit轮播图"""
        url = site["url"]
        doc = Testlunbo_pic.test_lunbo_pic.__doc__ + "site[{}]".format(str(site))
        data = return_lunbopicdata(account)
        s = str(data)
        dataStr = {"xmas-json": s}
        r = requests.post(url, data=dataStr)
        print(r)
        print(r.text)
        assert str(r) == "<Response [200]>", doc
    @pytest.mark.parametrize("site", sites_uat)
    @pytest.mark.parametrize("account", accounts)
    def test_lunbo_pic_uat(self,site,account):
        """uat轮播图"""
        url = site["url"]
        doc = Testlunbo_pic.test_lunbo_pic_uat.__doc__ + "site[{}]".format(str(site))
        data = return_lunbopicdata(account)
        s = str(data)
        dataStr = {"xmas-json": s}
        r = requests.post(url, data=dataStr)
        print(r)
        print(r.text)
        assert str(r) == "<Response [200]>", doc