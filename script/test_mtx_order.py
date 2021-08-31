# author:lee:2021/8/20 0020 19:19
import requests

from api.orderApi import Order
from api.loginApi import MtxLogin

class TestOrder:
    def setup_class(self):
        self.session = requests.Session()
        self.order_obj = Order()

    def test_order(self):
        '''
        依赖登录接口，api级别，请求级别
        :return:
        '''
        # 调用成功的登录接口
        MtxLogin().login_success(self.session)

        req_order = self.order_obj.order(self.session)
        assert req_order.json().get('msg') == "提交成功"