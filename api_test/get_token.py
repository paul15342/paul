import requests,json
import os
# list = []



class Api:
    def __new__(cls):

        if not hasattr(cls,'_instance'):
            cls._instance = super(Api,cls).__new__(cls)
            cls._instance.url = 'http://192.168.50.21:8181/api/user/login'
            cls._instance.name = 'ceshi1'
            cls._instance.password = 123456
        return cls._instance

    def get_name(self):
        return (self.name)

    def get_token(self):
        param ={}
        param['account']=self.name
        param['password']=self.password
        res = requests.post(self.url,data=param)
        text = json.loads(res.text)
        token = text['data']['token']
        return token

    def get_session(self):
        param = {}
        param['account'] = self.name
        param['password'] = self.password
        request = requests.Session()
        # res = request.post(url, data=param)
        # text = json.loads(res.text)
        # token = text['data']['token']
        return request

    def buy_goods(self,url,goodsId,number):
        global list
        param = {}
        param['token'] = self.get_token()
        param['goodsId'] = goodsId
        param['number'] = number
        res = self.get_session().post(url,data=param)
        text = json.loads(res.text)
        code = text['code']
        deductMoney = text['data']['deductMoney']
        status_code = res.status_code
        print (  status_code, code)

def compare(realValue,exValue):
    if realValue[0] == exValue['status_code'] :
        if realValue[1] == exValue['code']:
            print ('PASS')
        else:
            print ("失败")
    else:
        return False



def get_leatest_file():
    list = os.listdir(r'C:\Users\SCF\Desktop\new')
    return list

if __name__=='__main__':
    # Api().buy_goods("http://192.168.50.21:8181/api/shop/exchange",11,1)
    print (Api().get_session())



