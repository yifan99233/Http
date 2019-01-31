import requests

class Httpself():
    def __init__(self , url  , **data ):

        self.url = url
        if 'api' in data.keys():
            m =self.Post(  **data)
            self.header = self.post.request.headers
            self.cookie = {'PHPSESSID':self.post.cookies['PHPSESSID']}
        else:
            print("未登录，自行传递cookie!")



    def Post(self,api, **data):

        url = self.url + api
        if 'header' in data.keys():
            if 'cookie' in data.keys():
                if 'data' in data.keys():
                    print("1")
                    self.post =requests.post(url = url , headers = data['header'] , cookies = data['cookie'] , data = data['data'])
                else:
                    print("2")
                    self.post =requests.post(url = url , headers = data['header'] , cookies = data['cookie'] )
            else:
                if 'data' in data.keys():
                    print("3")
                    self.post =requests.post(url = url , headers = data['header'] , data = data['data'])
                else:
                    print("4")
                    self.post =requests.post(url = url , headers = data['header'] )
        else:
            if 'cookie' in data.keys():
                if 'data' in data.keys():
                    print("5")
                    self.post =requests.post(url = url , cookies = data['cookie'] , data = data['data'])
                else:
                    print("6")
                    self.post =requests.post(url = url , cookies = data['cookie'])
            else:
                print('7')
                self.post =requests.post(url = url ,data = data['data'])
        return  self.post



    def Get(self,api,**data):
        url = self.url + api
        if 'header' in data.keys():
            if data['header'] == 's':
                data['header'] = self.header
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    self.get = requests.get(url=url, headers=data['header'], cookies=data['cookie'], data=data['data'])
                else:
                    self.get = requests.get(url=url, headers=data['header'], cookies=data['cookie'])
            else:
                if 'data' in data.keys():
                    self.get = requests.get(url=url, headers=data['header'], data=data['data'])
                else:
                    self.get = requests.get(url=url, headers=data['header'])
        else:
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    self.get = requests.get(url=url, cookies=data['cookie'], data=data['data'])
                else:
                    self.get = requests.get(url=url, cookies=data['cookie'])
            else:
                self.get = requests.get(url=url, data=data['data'])
                self.get.status_code
        return self.get



    def test_code(self , requests):
        m = requests.status_code
        if m == 200:
            return True
        else:
            return False



    def test_msg(self , requests ,**data):
        try:
            if data == {}:
                m = requests.json()['msg']
            else:
                m = requests.json()['%s'%list(data.values())[0]]
        except:
            print("msg 处理出错")
        return m




    def test_text(self , requests):
        m = requests.text
        return m














if __name__ == '__main__':
    url = 'http://qyfh.ops.hzmantu.com'
    apilogin = '/User/checkLogin'
    api = '/Cser/getHandleAccount'
    data = {'isMainto':1}
    datauser = {'user':'sys','pass':123}

    c = Httpself(url = url ,api = apilogin , data = datauser)

    # m = c.Post(api = api , data = data , header = 's' , cookie = 's' )
    # # print(m.status_code)
    # # print(m.json())
    # # print(m.text)

