import requests

class Httpself():
    def __init__(self , url  , **data ):
        self.url = url
        if 'api' in data.keys():
            r =self.Post(  **data)
            self.header = r.headers
            self.cookie = r.cookies
        else:
            print("未登录，自行传递cookie!")



    def Post(self,api, **data):
        url = self.url + api
        if 'header' in data.keys():
            if data['header'] == 's':
                data['header'] = self.header
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    print(data['header'],data['cookie'],data['data'])
                    self.post =requests.post(url = url , headers = data['header'] , cookies = data['cookie'] , data = data['data'])
                else:
                    self.post =requests.post(url = url , headers = data['header'] , cookies = data['cookie'] )
            else:
                if 'data' in data.keys():
                    self.post =requests.post(url = url , headers = data['header'] , data = data['data'])
                else:
                    self.post =requests.post(url = url , headers = data['header'] )
        else:
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    self.post =requests.post(url = url , cookies = data['cookie'] , data = data['data'])
                else:
                    self.post =requests.post(url = url , cookies = data['cookie'])
            else:
               self.post =requests.post(url = url ,data = data['data'])
        print(self.post.json())
        print(self.post.text)
        print(self.post.status_code)

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




    def test_code(self):
        m = self.post.status_code
        if m == 200:
            return True
        else:
            return False



    def test_msg(self,**data):
        try:
            if data == {}:
                m = self.post.json()['msg']
            else:
                m = self.post.json()['%s'%list(data.values())[0]]
            print(m)
        except:
            print("msg 处理出错")
        return m




    def test_text(self):
        m = self.post.text
        return m



if __name__ == '__main__':
    url = 'http://qyfh.ops.hzmantu.com'
    apilogin = '/User/checkLogin'
    api = '/Cser/getHandleAccount'
    data = {'isMainto':1}
    datauser = {'user':'sys','pass':123}

    c = Httpself(url = url ,api = apilogin , data = datauser)
    c.test_code()
    c.test_msg()
    # m = c.Post(api = api , data = data , header = 's' , cookie = 's' )
    # # print(m.status_code)
    # # print(m.json())
    # # print(m.text)

