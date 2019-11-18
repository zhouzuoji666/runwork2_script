import requests
import random
import pytest
from common.con_fie import *
from business.base_64_ecoding import *

users=[{"CRFNSNY":""}]
sites_sit=[site_sit[8]]
sites_uat=[site_uat[8]]
date = "2019-10-%s %s:%s:%s" % (random.randint(18, 20), random.randint(10, 59), random.randint(10, 59), random.randint(10, 59))
class Testshenpidaiban():
    @pytest.mark.parametrize("user", users)
    @pytest.mark.parametrize("site", sites_sit)
    def test_shenpi_daiban_sit(self,user,site):
        """sit审批待办"""
        url = site["url"]
        print(url)
        doc = Testshenpidaiban.test_shenpi_daiban_sit.__doc__ + "site[{}]".format(str(site))
        data = return_shenpidata(user)
        r = requests.post(url, data=data)
        assert str(r) == "<Response [200]>",doc
        print(r)
        print(r.text)
    @pytest.mark.parametrize("user", users)
    @pytest.mark.parametrize("site", sites_uat)
    def test_shenpi_daiban_uat(self,user,site):
        """uat审批待办"""
        url = site["url"]
        print(url)
        doc = Testshenpidaiban.test_shenpi_daiban_uat.__doc__ + "site[{}]".format(str(site))
        data = return_shenpidata(user)
        r = requests.post(url, data=data)
        assert str(r) == "<Response [200]>",doc
        print(r)
        print(r.text)
