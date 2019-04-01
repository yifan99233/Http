from https import hrequests
import requests
from psql import SQL
from psql import Thisway
import time
import random
import json
import unicodedata
url = 'http://sfcy.ops.hzmantu.com'
class HMA_Account(hrequests.Httpself, Thisway.State ,SQL.NDDL):
    # 获取cookie
    def HmaCookie(self  ,data = {'user':'admin','pass': 123}):
        api = '/Home/Index/checkLogin'
        login = self.Post(api = api,data = data)
        header = login.request.headers
        cookie = {'PHPSESSID':'cqsrmqrcfs0hbubrgo5cmosg57'}
        return  header,cookie
    #获取对应产品级别价格
    def GetPrice(self,StoreId):
        host = 'rds11gs3kjhq3aeyr736o.mysql.rds.aliyuncs.com'
        db = 'haimati_dev'
        user = 'haimati_dev'
        password = 'YD0xk_kpD-32gR-M'
        msq = 'select S_Id,S_CityGroup from hmt_store where S_Id = %d;'%StoreId
        price = self.Nselect(sql=msq, host=host, db=db, user=user, password=password)[StoreId]
        sql = 'select PC_Pid,PC_OriPrice from hmt_product_citygroup where  PC_CityGroup = {}'.format(int(price))
        price = self.Nselect(sql = sql ,host = host ,db = db ,user = user ,password = password)
        return price
    #创建订单
    def CreatAccount(self,changes,count):
        header, _ = (self.HmaCookie())
        _, cookie = (self.HmaCookie())
        api = '/Home/Account/createAccount'
        Store_id = []
        [Store_id.append(i['S_Id']) for i in self.GetStore()]
        storem = []
        [storem.append(int(random.choices(Store_id)[0])) for xm in range(changes)]
        strw = [self.NewData(times = count,StoreId = xz)for xz in storem]
        AccountList = []
        for Schange in range(changes):
            StoreId = storem[Schange]
            self.ChangeStore(StoreId)
            for x in range(count):
                strw_ = strw[Schange][x]
                AccountState = self.Post(api=api, data=strw_, cookie=cookie, header=header).json()['msg']
                AccountF = self.GetAccountF()['aid']
                AccountList.append(AccountF)
                print(StoreId,AccountF,AccountState)
        return AccountList
    #生成随机订单参数
    def NewData(self,times,StoreId):
        header, _ = (self.HmaCookie())
        _, cookie = (self.HmaCookie())
        api = '/Home/Account/getDsConf'
        pser = self.Get(api=api, cookie=cookie).json()['msg']['productList']
        product = []
        newdata = {}
        price = self.GetPrice(StoreId)
        try:
            for i in pser:
                i['pid'] = i['id']
                i['pname'] = i['name']
                i['count'] = i['minPerson']
                i['sku'] = ''
                i['discount'] = 0
                i['price'] = price[i['id']]
                i['oriPrice'] = price[i['pid']]
                i.pop('name')
                i.pop('maxPerson')
                i.pop('id')
                i.pop('minPerson')
                product.append(i)
        except:
            pass
            #print("%d门店数据库记录不对应，请手动更改"%StoreId)
        strws = []

        for this in range(times):
            newdata['name'] = self.RandomStr(time = 1)[0]
            newdata['sex'] = random.choice([1,2])
            newdata['code'] = ''
            newdata['isSn'] = 0
            newdata['paytype'] = 11
            newdata['type'] = 1
            newdata['phone'] = self.RandomStr(les = 11 ,time = 1,num=True)[0]
            newdata['birth'] = time.strftime('%Y-%m-%d',time.localtime())
            newdata['ordertime'] = int(time.time())+1200
            choiceprice = random.choice(product)
            choiceprices = []
            choiceprices.append(choiceprice)
            newdata['money'] = choiceprice['price']
            newdata['payState'] = 2
            print(choiceprice)
            newdata['product'] = (json.dumps((choiceprices)))
            newdata['note'] = self.RandomStr(time = 1)[0]
            newdata['ordertime'] = time.strftime("%d-%m-%d %H:%M:%S",time.localtime(time.time()+500))
            strw = ''
            for i in newdata:
                strw+='%s=%s&' % (i, newdata[i])
            strws.append(strw)

        return strws
    #获取录单伙伴
    def GetPser(self):
        header, _ = (self.HmaCookie())
        _, cookie = (self.HmaCookie())

        api = '/Home/Public/getStaffTypeList'
        pser = self.Get(api = api , cookie = cookie).json()['msg']
        #[print(i) for i in pser]


        print(random.choice([1,2]))
    #每日绩效核对
    def updateExploitCheck(self):
        header,_ = (self.HmaCookie())
        _,cookie = (self.HmaCookie())
        now = time.strftime('%Y-%m-%d',time.localtime())
        api = '/Home/Account/editExploitCheck?checkTime='+now
        #getsendcount = '/Home/Purchase/getSendStatusCount'
        #l = self.Get(api=getsendcount,cookie = cookie).json()
        m = self.Get(api = api , cookie = cookie).json()['msg']['data']
        data = {}
        for num,i in enumerate(m) :
            for j,k in zip(i,i.values()):
                if i['ECKD_CheckValue'] == '':
                    i['ECKD_CheckValue'] = 37
                data['data[%d][%s]'%(num,j)] = k
        data['checkTime'] = now
        data['reason'] = 1
        data['reportAmount'] = 1
        data['reportCount'] = 1
        print(data)
    #获取门店
    def GetStore(self):
        header, _ = (self.HmaCookie())
        _, cookie = (self.HmaCookie())
        api = '/Home/Public/getStoreList'
        m = self.Get(api = api , cookie = cookie ).json()['msg']
        return m
    #初始化数据（化妆师、摄影师、客服）
    def InitializationData(self,time = 1,like = 2):
        with open('log.text','a') as log:
            with open('logfail.text','a') as logfail:
                    log.writelines("正在初始化数据\n")
                    print("开始初始化数据...")
                    api = '/Home/System/createStaff'
                    header, _ = (self.HmaCookie())
                    _, cookie = (self.HmaCookie())
                    name = self.RandomStr(time=time, num=False)
                    num = self.RandomStr(time=time, num=True)
                    store = self.GetStore()
                    ST_Id = []
                    listtype = [1, 2, 4] * 1000
                    for datastore in store:
                        ST_Id.append(datastore['S_Id'])
                    ST_Id = ST_Id * 15
                    ST_Id.sort()
                    userdata = []
                    for index, i, m, k, s in zip((enumerate(ST_Id)), name, num, listtype, ST_Id):
                        userdata.append({'name': i, 'num': m, 'hasCloud': 0, 'status': '', 'store': s, 'type': k})
                        msg = self.Post(api = api , cookie = cookie , header = header , data = userdata[index[0]]).json()['msg']
                        if msg == '该工号已存在相同岗位的员工信息,请检查':
                            logfail.writelines('%s,该工号已存在相同岗位的员工信息,请检查\n' % userdata[index[0]])
                            print(userdata[index[0]], "工号重复添加失败")
                        else:
                            print(userdata[index[0]])
                            log.writelines('%s\n'%userdata[index[0]])
    #切换门店
    def ChangeStore(self, store):
        header, _ = (self.HmaCookie())
        _, cookie = (self.HmaCookie())
        api = '/Home/Index/changeStore/sid/%d'%store
        try:
            self.Get(api = api , cookie = cookie )
        except:
            pass
    #获取订单号
    def GetAccountF(self,list = False):
        header, _ = (self.HmaCookie())
        _, cookie = (self.HmaCookie())
        api = '/Home/Account/getAccountList?state=0&type=1&key=&page=1&pageSize=10'
        if list == True:
            msg = self.Get(api = api ,cookie = cookie).json()['msg']['list']
        else:
            msg = self.Get(api = api , cookie = cookie).json()['msg']['list'][0]
        return msg




c = HMA_Account(url = url )
c.CreatAccount(1,5)