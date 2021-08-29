# author:lee:2021/8/21 0021 15:22
import requests

from Testfan.apiFrame.api.loginApi import MtxLogin
from Testfan.apiFrame.api.orderApi import Order
from Testfan.apiFrame.api.payOrderApi import PayOrder


class TestPay:
    def setup_class(self):
        self.session = requests.Session()
        # 调用登录成功接口
        MtxLogin().login_success(self.session)
        # 调用订单接口，获取jump_url
        Order().order(self.session)
        # 实例化支付接口
        self.payorder_obj = PayOrder()
    def test_payorder(self):
        # 请求支付接口
        resp_pay = self.payorder_obj.pay_order(self.session)
        # 断言
        assert '支付成功' in resp_pay.text