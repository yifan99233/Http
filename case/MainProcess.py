from https import hrequests as Qur
from bs4 import BeautifulSoup
from psql import Thisway as way
import math



class Mprocess(object):



    def login(self , url , login = True , **data  ):
        self.Lhttp = Qur.Httpself(url)
        if login == True:
            self.Lhttp.Post(api = data['api'] , data = data['data'])
            self.header = self.Lhttp.post.request.headers
            self.cookie = {'PHPSESSID':self.Lhttp.post.cookies['PHPSESSID']}
        else:
            self.header = data['header']
            self.cookie = data['header']

        # 修片组长审核列表
        def zzlist(self):
            list = []
            RCaidInforUrl = '/Cker/getCheckList'
            RCaidInforData = {'name': '', 'page': 1, 'leader': -1}
            caid = self.Lhttp.test_msg(self.Lhttp.Post(api=RCaidInforUrl, header=self.header, cookie=self.cookie, data=RCaidInforData))
            for x in range(1, math.ceil(caid['total'] / 10) + 1):
                RCaidInforData = {'name': '', 'page': x, 'leader': -1}
                caid = self.Lhttp.test_msg(
                    self.Lhttp.Post(api=RCaidInforUrl, header=self.header, cookie=self.cookie, data=RCaidInforData))
                for x in caid['list']:
                    list.append(x['CA_Id'])
            return list

        def kpslist(self, header, cookie):
            pass

    def SysUpload ( self ,  aid , count = 4,time=1 ) :
        # 查找订单接口

        searchAccountUrl = '/Remote/searchAccount'
        searchAccountData = {'aidKey':aid}
        PtypeUrl = '/Remote/getAccountType'
        ptype = self.Lhttp.Get(api=PtypeUrl,cookie='s').json()['msg'][0]['accountType']
        v = self.Lhttp.test_msg(self.Lhttp.Post ( api=searchAccountUrl , data=searchAccountData  , cookie=self.cookie ))
        if v == '暂无相关订单':
            print('订单不存在')
        else:
            for i in range(time):
                p = v[0]
                pid = p['productIdArr'][0]['AI_Pid']
                list = way.Rnum().Rphotos(count = count)
                # 摄影师上传提交的参数

                try:
                    SubmitData = {}
                    num = 0
                    for i in list:
                        SubmitData['photoData[%d][path]' % num] = i
                        SubmitData['photoData[%d][count]' % num] = way.Rnum().Rrandom(4,4)[0]
                        SubmitData['photoData[%d][productId]' % num] = pid
                        SubmitData['photoData[%d][group]' % num] = ''
                        num+=1
                    SubmitData['name'] = p['A_Name']
                    SubmitData['phone'] = p['A_Phone']
                    SubmitData['note'] = p['note']
                    SubmitData['areye'] = 1
                    SubmitData['arface'] = 1
                    SubmitData['ardot'] = 1
                    SubmitData['isToday'] = 1
                    SubmitData['ptype'] = ptype
                    SubmitData['haimatiAid'] = aid
                    SubmitData['productArr[]'] = pid
                except:
                    print("参数生成失败")
                # print(SubmitData)
                # print(self.cookie)
                # print(self.header)
                try:
                    #摄影师上传提交接口地址
                    PsersubmitAccount = '/Pser/submitAccount'
                    #sys上传调 post请求
                    self.Lhttp.Post (   api = PsersubmitAccount , data = SubmitData , cookie = self.cookie )
                    print("摄影师已成功上传1单，流水号为："+self.HistoryPhotographer()[0])
                except:
                    print("提交失败")



    #摄影师上传历史记录
    def HistoryPhotographer(self, page=1):
        list = []
        for x in range(page):
            url = '/Account/uploadedAccount/p/%d' % x
            m = self.Lhttp.Get(api=url, cookie=self.cookie).text
            soup = BeautifulSoup(m, 'html.parser')
            [list.append(i.text) for i in soup.find_all("td")[0::5]]
        return list



    # 外包修片师提交订单
    def BpoUpload(self, time=1):
        way.Rnum().BpoUpload(time=time)



    def XpsUpload ( self , time = 1 , mainto = True) :
        SearchAccountCount = '/Cser/getPhotoQueue' #查看能接多少单
        RequestsAccountUrl = '/Cser/requestAccount' # 接单接口
        GetHandAccount = '/Cser/getHandleAccount'   #接单后查询接口/Cser/getHandleAccount?isMainto=1
        XpsSubmitUrl = '/Cser/submitAccount'
        if mainto == True:
            ismainto = 1
        else:
            ismainto = 0
        RequestsAccountData = { 'isMainto' : ismainto } #接单 参数
        for i in  range ( time ) :
            #查询可接单数
            msg = self.Lhttp.test_msg(self.Lhttp.Post(api = SearchAccountCount , cookie = self.cookie ))
            #点击接单
            msv = self.Lhttp.test_msg(self.Lhttp.Post(api=RequestsAccountUrl, data=RequestsAccountData, cookie=self.cookie, header=self.header))
            if msg['needCount']>0 or msv == '不可重复接单,请不要多次点击确认按钮':
                #接单
                msv = self.Lhttp.test_msg(self.Lhttp.Post( api = RequestsAccountUrl , data = RequestsAccountData , cookie = self.cookie , header = self.header ))
                if msv=='接单成功' or msv =='不可重复接单,请不要多次点击确认按钮':
                    #查询流水信息
                    if mainto == True:
                        pmsg = self.Lhttp.test_msg(self.Lhttp.Get ( api = GetHandAccount , cookie = self.cookie ,data = RequestsAccountData  ))
                    else:
                        pmsg=self.Lhttp.test_msg(self.Lhttp.Post ( api = GetHandAccount , cookie = self.cookie   ))
                    photoid = {}
                    photoid['aid'] = pmsg['CA_Id']
                    data = pmsg['photoData']
                    num = 0
                    list = way.Rnum().Rphotos(len(data))
                    for x in data:
                        photoid['photo[%d][id]'%num] = x['CP_Id']
                        photoid['photo[%d][path]'%num] = list[num][0]
                        photoid['photo[%d][modelPath]'%num] = ''
                        num+=1
                    state = self.Lhttp.test_msg(self.Lhttp.Post( api = XpsSubmitUrl , data = photoid  ,header= self.header,cookie = self.cookie ))
                    print("流水号："+photoid['aid']+"---已被修片师"+state)
                else:
                    print(msv)
            else:
                print("暂无可接订单")



    def Review(self , time = 1 , caid = '' ):
        #返回审核页面订单信息的接口 name ''   page   leader -1

        #审核详情界面的接口 aid
        AccountInforUrl = '/Cker/getCheckAccount'
        changestate = '/Cker/changePhotoState'
        changestatedata = { "plant" : "" , "weed" : "" }
        #通过审核的接口
        RPassUrl = '/Cker/passAccount'
        list = []
        if caid == '':

            for i in range(time):
                Caid = self.zzlist()[i]
                AccountInforData = {'aid': list()[i]}
                self.Lhttp.Post(api=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
                RPassData = {'aid': Caid, 'goodNote': '', 'badNote': '', 'isVisa': 0, 'splPrty': 0}
                if self.Lhttp.test_msg(self.Lhttp.Post(api=RPassUrl, data=RPassData, header=self.header, cookie=self.cookie)) == '操作成功':
                    print('%s该流水号修片师组长已审核'%Caid)
                else:
                    print('审核失败')
        else:
            AccountInforData = { 'aid' : caid }
            self.Lhttp.Post(api=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
            data = {'aid': caid, 'goodNote': '', 'badNote': '', 'isVisa': 0, 'splPrty': 0}
            self.Lhttp.Post(api = RPassUrl, data=data, header=self.header, cookie=self.cookie)
            if self.r.json()['msg'] == '操作成功':
                print('%s该流水号修片师组长已审核' % caid)
            else:
                print('审核失败')



    def kpsReview(self , cnum = '' , time = 1 ):
        RCaidInforurl = '/Cker/getCheckAccountList'
        AccountInforUrl = '/Account/doCheckAccount'
        pj = '/Cker/appraiseCserAccount'
        if cnum == '' :
            def kpslist():
                RCaidInforData = {'type': 3, 'key': '', 'state': 'all', 'page': 1}
                caid = self.Lhttp.test_msg(
                    self.Lhttp.Post(api=RCaidInforurl, header=self.header, cookie=self.cookie, data=RCaidInforData))["t"]
            for x in range(1,time+1):
                RCaidInforData = {'type': 3, 'key': '' , 'state': 'all' , 'page':x}
                caid = self.Lhttp.test_msg(self.Lhttp.Post(api=RCaidInforurl, header=self.header, cookie=self.cookie, data=RCaidInforData))["list"]
                for i in range(10):
                    Caid = caid[i]['aid']
                    RPassData = 'score=5&comment=456&aid=%s'%Caid
                    self.Lhttp.Post(api=pj, data=RPassData,  header=self.header, cookie=self.cookie)
                    AccountInforData = {'aid': Caid , 'isAgreeShare' : 1 }
                    m = self.Lhttp.test_msg(self.Lhttp.Post(api=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData))
                    self.Lhttp.Post(api=pj, data=RPassData, header=self.header, cookie=self.cookie)
                    if m == '微信通知未发送,该用户未关注微信公众号或已取消关注' or m == '微信通知将在稍后发送':
                        print(Caid+'该流水号看片师已审核')
                    else:
                        print(Caid+'看片师审核失败')
        else:
            Caid = cnum
            RPassData = 'score=5&comment=456&aid=%s' % Caid
            self.Lhttp.Post(api=pj, data=RPassData, header=self.header, cookie=self.cookie)
            AccountInforData = {'aid': Caid, 'isAgreeShare': 1}
            m = self.Lhttp.test_msg(self.Lhttp.Post(url=AccountInforUrl, header=self.header, cookie=self.cookie, data=AccountInforData))['msg']
            self.Lhttp.Post(api=pj, data=RPassData, header=self.header, cookie=self.cookie)
            if m == '微信通知未发送,该用户未关注微信公众号或已取消关注' or m == '微信通知将在稍后发送':
                print(Caid + '该流水号看片师已审核')
            else:
                print(Caid + '看片师审核失败')





url = 'http://qyfh.ops.hzmantu.com'
Lapi = '/User/checkLogin'
Ldata = {'user':'sys','pass':123}
c = Mprocess()
c.login(url = url , api = Lapi ,data = Ldata)
c.zzlist()
#c.Review()
#c.BpoUpload(time = 2)
#c.kpsReview()

print(c.HistoryPhotographer())
#c.SysUpload(aid = 2019012518399152)
#c.XpsUpload()


