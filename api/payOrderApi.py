# author:lee:2021/8/21 0021 14:47
from Testfan.apiFrame import config
from Testfan.apiFrame.tools import logger

log = logger.GetLogger().get_logger()
class PayOrder():
    def __init__(self):
        '''
        这个支付接口是需要重定向，302的url是从提交订单的接口里面获取jump_url
        '''
        # 消费数据
        self.url = config.JUMP_URL


    def pay_order(self,session):

        resp = session.get(self.url,allow_redirects = False)
        resp_pay = session.get(resp.headers['location'])
        return resp_pay
