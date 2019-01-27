import requests

class Httpself():
    def __init__(self , url , api , **data ):
        self.url = url
        r =self.Post(url =url ,api = api,  **data)
        self.header = r.headers
        self.cookie = r.cookies



    def Post(self, api , **data):
        url = self.url + api
        if 'header' in data.keys():
            if data['header'] == 's':
                data['header'] = self.header
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    post =requests.post(url = url , headers = data['header'] , cookies = data['cookie'] , data = data['data'])
                else:
                    post =requests.post(url = url , headers = data['header'] , cookies = data['cookie'] )
            else:
                if 'data' in data.keys():
                    post =requests.post(url = url , headers = data['header'] , data = data['data'])
                else:
                    post =requests.post(url = url , headers = data['header'] )
        else:
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    post =requests.post(url = url , cookies = data['cookie'] , data = data['data'])
                else:
                    post =requests.post(url = url , cookies = data['cookie'])
            else:
               post =requests.post(url = url ,data = data['data'])
        return  post



    def Get(self,api,**data):
        url = self.url + api
        if 'header' in data.keys():
            if data['header'] == 's':
                data['header'] = self.header
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    get = requests.get(url=url, headers=data['header'], cookies=data['cookie'], data=data['data'])
                else:
                    get = requests.get(url=url, headers=data['header'], cookies=data['cookie'])
            else:
                if 'data' in data.keys():
                    get = requests.get(url=url, headers=data['header'], data=data['data'])
                else:
                    get = requests.get(url=url, headers=data['header'])
        else:
            if 'cookie' in data.keys():
                if data['cookie'] == 's':
                    data['cookie'] = self.cookie
                if 'data' in data.keys():
                    get = requests.get(url=url, cookies=data['cookie'], data=data['data'])
                else:
                    get = requests.get(url=url, cookies=data['cookie'])
            else:
                get = requests.get(url=url, data=data['data'])
        return get


    
if __name__ == '__main__':
    url = 'http://qyfh.ops.hzmantu.com'
    api = '/User/checkLogin'
    data = {'user':'sys','pass':123}
    c = Httpself(url = url , api=api , data = data)
