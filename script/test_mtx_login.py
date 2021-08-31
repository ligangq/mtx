# author:lee:2021/8/17 0017 14:23
import allure
import pytest
import requests

from api.loginApi import MtxLogin
from tools.analyze_data import analyze_data

class TestLogin():
    def setup_class(self):
        self.session = requests.session()
        self.login_obj = MtxLogin()

    def test_login_success(self):
        resp_login = self.login_obj.login_success(self.session)
        assert resp_login.json().get('msg') == '登录成功'

    @pytest.mark.parametrize('args',analyze_data('test_login','test_login'))
    @allure.title('登录异常，测试数据是：{args}')
    def test_login_fail(self,args):
        data = {'accounts':args.get('accounts'),'pwd':args.get('pwd')}
        resp_login = self.login_obj.login(self.session,data)
        assert resp_login.json().get('msg') == args.get('exp')