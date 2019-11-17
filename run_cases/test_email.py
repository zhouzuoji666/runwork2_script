import requests
import random
import pytest
from common.con_fie import *


sites_sit=[site_sit[1]]
# sites_uat=[site_uat[9]]
class Testlunbo_pic():
    @pytest.mark.parametrize("site", sites_sit)
    @pytest.mark.parametrize("account", accounts)
    def test_email_sit(self,site,account):
        """sit获取邮箱"""
        url = site["url"]
        doc = Testlunbo_pic.test_email_sit.__doc__ + "site[{}]".format(str(site))
        data = return_emaildata(account)
        s = str(data)
        dataStr = {"xmas-json": s}
        r = requests.post(url, data=dataStr)
        print(r)
        print(r.text)
        assert str(r) == "<Response [200]>", doc
    #暂无uat
    @pytest.mark.parametrize("site", sites_sit)
    @pytest.mark.parametrize("account", accounts)
    def test_email_sit(self, site, account):
        """sit获取邮箱"""
        url = site["url"]
        doc = Testlunbo_pic.test_email_sit.__doc__ + "site[{}]".format(str(site))
        data = return_emaildata(account)
        s = str(data)
        dataStr = {"xmas-json": s}
        r = requests.post(url, data=dataStr)
        print(r)
        print(r.text)
        assert str(r) == "<Response [200]>", doc


if __name__=="__main__":
    pass