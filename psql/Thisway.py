from psql import SQL
import random
import requests
from bs4 import BeautifulSoup


class State(object):
    def RandomStr(self,les = 7,time = 5 , num = False):
        #生成字符串
        m = ['a','s','d','f','g','h','j','k','l','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m',1,4,7,8,5,2,3,6,9]
        Rstrs = set()
        if num == False:
            for count in range(time):
                for i in range(10):
                    random.shuffle(m)
                    Rstr = ''
                for x in range(les):
                    Rstr = Rstr + str(random.choice(m))
                Rstrs.add(Rstr)
        #生成随机数
        if num == True:
            for count in range(time):
                Rstr = ''
                for x in range(les):
                    Rstr = Rstr + str(random.randint(1,9))
                Rstrs.add(Rstr)
        return list(Rstrs)

    #范围内获取随机数
    def Rrandom(self,a = 1, b = 400 , count = 1):
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
    def BpoUpload(self , time = 1 , cookie = 'p8ppd4l6gm7cfqm27km90edig2' ):
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
                    hlist = self.Rphotos()
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
    url = 'http://qyfh.ops.hzmantu.com'
    data = {'user': 'xpszz', 'pass': 123}
    c = State()
    #c.BpoUpload()
    c.RandomStr(num = True)
