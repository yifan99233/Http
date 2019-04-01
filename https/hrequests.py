import requests


class Httpself():
    def __init__(self, url):
        self.url = url

    def Post(self, api, **data):

        url = self.url + api
        if 'header' in data.keys():
            if 'cookie' in data.keys():
                if 'data' in data.keys():
                    self.post = requests.post(url=url, headers=data['header'], cookies=data['cookie'],
                                              data=data['data'])
                else:
                    self.post = requests.post(url=url, headers=data['header'], cookies=data['cookie'])
            else:
                if 'data' in data.keys():
                    self.post = requests.post(url=url, headers=data['header'], data=data['data'])
                else:
                    self.post = requests.post(url=url, headers=data['header'])
        else:
            if 'cookie' in data.keys():
                if 'data' in data.keys():
                    self.post = requests.post(url=url, cookies=data['cookie'], data=data['data'])
                else:
                    self.post = requests.post(url=url, cookies=data['cookie'])
            else:

                self.post = requests.post(url=url, data=data['data'])
        return self.post

    def Get(self, api, **data):
        url = self.url + api
        if 'header' in data.keys():
            if 'cookie' in data.keys():
                if 'data' in data.keys():
                    print('wqe1')
                    self.get = requests.get(url=url, headers=data['header'], cookies=data['cookie'],
                                            params=data['data'])
                else:
                    print('wqe2')
                    self.get = requests.get(url=url, headers=data['header'], cookies=data['cookie'])
            else:
                if 'data' in data.keys():
                    print('wqe3')
                    self.get = requests.get(url=url, headers=data['header'], params=data['data'])
                else:
                    print('wqe3')
                    self.get = requests.get(url=url, headers=data['header'])
        else:
            if 'cookie' in data.keys():
                if 'data' in data.keys():
                    self.get = requests.get(url=url, cookies=data['cookie'], params=data['data'])
                else:

                    self.get = requests.get(url=url, cookies=data['cookie'])
            else:
                print('wqe5')
                self.get = requests.get(url=url, params=data['data'])

        return self.get

    def test_code(self, requests):
        m = requests.status_code
        if m == 200:
            return True
        else:
            return False

    def test_msg(self, requests, **data):
        try:
            if data == {}:
                m = requests.json()['msg']
            else:
                m = requests.json()['%s' % list(data.values())[0]]
        except:
            print("msg 处理出错")
        return m

    def test_text(self, requests):
        m = requests.text
        return m















