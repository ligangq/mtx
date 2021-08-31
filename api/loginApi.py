# author:lee:2021/8/17 0017 14:18


from config import IP,HEADERS


class MtxLogin():
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'

    def login(self,session,data):
        resq_login = session.post(self.url, data=data, headers=HEADERS)
        return resq_login


    def login_success(self,session):
        data = {'accounts':'lee11','pwd':'123123'}
        resq_login = session.post(self.url, data=data, headers=HEADERS)
        return resq_login

