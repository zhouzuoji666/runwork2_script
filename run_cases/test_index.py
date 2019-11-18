import requests
import random
import pytest
from common.con_fie import *


sites_sit=[site_sit[9]]
sites_uat=[site_uat[9]]
sit_tokens=["be956322c4e872495552133d10c66b06"]
uat_tokens=["ccfd29ea1d2dbe8138daedf0db1ed20d"]
class Testindex():
    @pytest.mark.parametrize("site", sites_sit)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("token", sit_tokens)
    def test_index_sit(self,site,account,token):
        """sit首页"""
        url = site["url"]
        doc = Testindex.test_index_sit.__doc__ + "site[{}]".format(str(site))
        data = return_indexdata(account,token)
        s = str(data)
        dataStr = {"xmas-json": s}
        r = requests.post(url, data=dataStr)
        print(r.text)
        assert str(r) == "<Response [200]>", doc

    @pytest.mark.parametrize("site", sites_uat)
    @pytest.mark.parametrize("account", accounts)
    @pytest.mark.parametrize("token", uat_tokens)
    def test_index_uat(self,site,account,token):
        """uat首页"""
        url = site["url"]
        doc = Testindex.test_index_uat.__doc__ + "site[{}]".format(str(site))
        data = return_indexdata(account,token)
        s = str(data)
        dataStr = {"xmas-json": s}
        r = requests.post(url, data=dataStr)
        print(r.text)
        assert str(r) == "<Response [200]>", doc