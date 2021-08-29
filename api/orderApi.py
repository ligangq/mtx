# author:lee:2021/8/20 0020 19:12
from Testfan.apiFrame import config


class Order:
    def __init__(self):
        self.url = config.IP + '/mtx/index.php?s=/index/buy/add.html'

    def order(self,session):
        data = {
            'goods_id': 1,
            'buy_type': 'goods',
            'stock': 1,
            'ids': 2145,
            'address_id': 1777,
            'payment_id': 1,
            'site_model': 0,
            'spec': '',
            'user_note': ''
        }

        resp_order = session.post(self.url,data=data,headers=config.HEADERS)
        # 提取数据做数据关联    -->生成数据，放在公共区域
        config.JUMP_URL = resp_order.json().get('data').get('jump_url')
        return resp_order

