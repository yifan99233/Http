import random
from psql import SQL
from bs4 import BeautifulSoup
import requests

class Rnum(object):



    #范围内获取随机数
    def Rrandom(self,a = 1, b = 5 , count = 1):
        list = []
        if count > b+1 - a:
            print("count不能大于范围内的值")
        else:
            while True:
                    if len(list)>count-1:
                        break
                    list_a = random.randint( a, b )
                    if list_a not in list:
                        list.append(list_a)
        return list



    #随机获取照片
    def Rphotos(self  , count = 4):
        id =self.Rrandom( count = count )
        list = []
        for x in id:
            list_path =SQL.Sql().Select('select photo from photo where id in ("%d")'%x)[0][0]
            list.append(list_path)
        return list



    #外包修片师提交订单
    def BpoUpload(self , time = 1 , cookie = 'e29i69v93hl9d74vrk4kdejl21' ):
        for i in  range(time):
            cookies = {'thinkphp_show_page_trace':'0|0'}
            cookies['PHPSESSID'] = cookie
            print(cookies)
            getaccount = 'http://bpo.qyfh.ops.hzmantu.com/Api/startAccount'
            get = requests.get(url = getaccount,cookies = cookies)
            try:
                if get.json()['msg'] == "接单成功" or get.json()['msg'] =='接单失败,不可重复接单,请不要多次点击确认按钮':
                    get = requests.get(url = 'http://bpo.qyfh.ops.hzmantu.com/Index/handle',cookies = cookies).text
                    soup = BeautifulSoup(get,'html.parser')
                    aid = str(soup.find('td').text.strip())[0:17]
                    list = soup.find_all('label')
                    mlist = []
                    [mlist.append(x.text[5:].strip()) for x in list]
                    num = 0
                    data = {}
                    hlist = self.Rphotos(a = 1 , b = 400 )
                    data['aid'] = aid
                    for i in mlist:
                        data['photo[%d][oldname]'%num] = i
                        data['photo[%d][newname]'%num] = hlist[num]
                        num+=1
                    r = requests.post(url = 'http://bpo.qyfh.ops.hzmantu.com/Api/submitPhoto',data =data,cookies = cookies)
                    print(r.json())
                    #print(aid,r.json())
                else:
                    print("暂无订单可以上传")
            except:
                print('cookie信息已过期，请更换cookie信息')




if __name__ == '__main__':
    c = Rnum()
    m = c.Rphotos(count = 4)
    print(random.randint(4,4))
