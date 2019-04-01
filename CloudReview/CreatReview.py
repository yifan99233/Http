from https import hrequests
from psql import SQL
from psql import Thisway
import random
import json
class Review(hrequests.Httpself, Thisway.State ,SQL.NDDL):
    def login(self):
        data = {'refreshCode': '073856d462eb2c28d443593fcc4446b2','appId':113,'staffId':'605611'}
        api = '/cloud_spot_check/spot_checks'
        this = self.Post(api = api , data = data)
        cookie = ''
        header = this.headers
        return cookie,header
    def test_creat(self,cookie = 'Hn0WCga4hCSl2RWhN2sEWAvZjYzRS2pyT9YEb7gz9T5TE29tsv7kSlrQviMwLyAr'):
        cookie = {'stream_hash': cookie}
        header = {'Content-Type': 'application/json'}
        api = '/cloud_spot_check/spot_checks'
        data = self.test_creat_data()
        print("标题", data['title'])
        print("摄影配置", data['photography_items'])
        print("化妆配置", data['makeup_items'])
        print("修片配置", data['trim_photo_items'])
        data = json.dumps(data)
        msg = self.Post(api = api ,data= data ,header = header,cookie = cookie).json()
        print(msg)
    def test_creat_data(self):
        str = random.choices(self.RandomStr(les = 8,time = 50 ,num = False))[0]
        def newItem():
            itesm = random.randint(1, 5)
            count = 0
            data = []
            for i in range(itesm-1):
                itm = random.choices(self.RandomStr(les=5, time=50, num=False))[0]
                thisrandit = random.randint(1,20)
                itm = {"name":itm,"score":thisrandit}
                data.append(itm)
                count = thisrandit + count
            data.append({"name":random.choices(self.RandomStr(les=5, time=50, num=False))[0],"score":100-count})
            return data
        sysdata = newItem()
        hzsdata = newItem()
        xpsdata = newItem()
        store = [1071,1113,1111,1134,1076,1107,1144,1129,1028,1082,1078,1137,1045,1085,1103,1110,1094,1035,1112,1081,1108,1109,1104,1099,1102,1114,1105,1106,1152,1116,1139,1151,1148,1146,1145,1143,1142,1141,1118,1140,1138,1133,1132,1131,1128,1127,1125,1122,1121,1119,1117,1098,1095,1080,1092,1001,1019,1018,1079,1090,1097,1054,1074,1070,1149,1120,1130,1100,1101,1062,1087,1123,1002,1115,1064,1027,1124,1032,1033,1088,1039,1004,1022,1126,1021,1020,1009,1003,1017,1016,1015,1005,1007,1014,1024,1008,1013,1012,1011,1010,1006,1068,1026,1096,1065,1073,1077,1063,1061,1060,1058,1086,1057,1056,1055,1053,1029,1052,1051,1049,1047,1044,1042,1041,1038,1037,1034,1031,1036]
        product = ["1","2","3","7","10","12","15","16","17","18","19","21","22","23","25","27","28","29","30","33","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","59","61","62","63","67","70","72","73","74","75","83","84","85","86","87","88","89","90","91","92","93","94","95","96","136","137","138","139","140","141","142","147","148","149","150","151","152","157","158","161","162","168","173","175","176","177","178","184","185","186","187","188","189","190","194","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217","218","219","220","221","232","233","234","235","241","242","243","244","248","249","250","251","252","253","260","261","262","263","264","271","272","273","275","276","284","285","286","290","291","292","296","298","300","301","302","303","304","305","306","307","308"]
        data = {"title":str,"start_time":"2019-03-01","end_time":"2019-03-25","extends":{"store_type":["blue"],"store":store,"product_id":product},"spot_check_count":"1000","photography_items":sysdata,"makeup_items":hzsdata,"trim_photo_items":xpsdata}
        return data

    def test_review(self,sid,cookie = "Hn0WCga4hCSl2RWhN2sEWAvZjYzRS2pyT9YEb7gz9T5TE29tsv7kSlrQviMwLyAr"):
        cookie = {'stream_hash': cookie}
        header = {'Content-Type' : 'application/json'}
        getItemapi = '/cloud_spot_check/spot_check/get_grade_items?spot_id=%d'%sid
        item = self.Get(api = getItemapi ,header = header).json()['msg']
        getIdapi = '/cloud_spot_check/spot_check/get_grade_list?spot_id=%d'%sid
        id = self.Get(api = getIdapi,header = header).json()['msg']['photos']
        m_id = [i['id']for i in id]
        try:
            photography = [iteem['name'] for iteem in item['photography']]
            photography.append("advise")
        except KeyError: photography = False
        try:
            makeup = [iteem['name'] for iteem in item['makeup']]
            makeup.append("advise")
        except KeyError:makeup = False
        try:
            trim_photo = [iteem['name'] for iteem in item['trim_photo']]
            trim_photo.append("advise")
        except KeyError:trim_photo =False
        print(photography,trim_photo,makeup)

        if photography != False:
            if makeup != False:
                if trim_photo != False:
                    ex = [{"photo_id":dk,
                           "photography":{zs:random.randint(0,5)for zs in photography},
                           "makeup":{zs:random.randint(0,5)for zs in makeup},
                           "trim_photo":{zs:random.randint(0,5)for zs in trim_photo}
                           } for dk in m_id ]
                else:
                    ex = [{"photo_id": dk,
                           "photography": {zs: random.randint(0, 5)for zs in photography},
                           "makeup": {zs: random.randint(0, 5)for zs in makeup}
                           } for dk in m_id]
            else:
                if trim_photo != False:
                    ex = [{"photo_id": dk,
                           "photography": {zs: random.randint(0, 5)for zs in photography},
                           "trim_photo": {zs: random.randint(0, 5)for zs in trim_photo}
                           } for dk in m_id]
                else:
                    ex = [{"photo_id": dk,
                           "photography": {zs: random.randint(0, 5)for zs in photography}
                           } for dk in m_id]
        else:
            if trim_photo != False:
                if makeup != False:
                    ex = [{"photo_id": dk,
                           "makeup": {zs: random.randint(0, 5)for zs in makeup},
                           "trim_photo": {zs: random.randint(0, 5)for zs in trim_photo}
                           } for dk in m_id]
                else:
                    ex = [{"photo_id": dk,
                           "trim_photo": {zs: random.randint(0, 5)for zs in trim_photo}
                           } for dk in m_id]
            else:
                ex = [{"photo_id": dk,
                       "trim_photo": {zs: random.randint(0, 5)for zs in trim_photo}
                       } for dk in m_id]
        data = {"spot_id":sid,"extends":ex}
        print(data)
        comapi = '/cloud_spot_check/spot_check/grades'
        commit = self.Post(api = comapi ,cookie = cookie ,data =json.dumps(data),header = header).json()
        print(commit)


def cool1():
    cookie = 'TWMntVfOaWyYKWB4TQUCYwNQzjrlAZiZwRBlV4IW2tzDAOwhRXi6qfjy7dJjCr8f'
    url  = 'https://spot-v12.local.hzmantu.com'
    c = Review(url)
    c.test_creat(cookie)
def cool2():
    cookie = ''
    url = 'https://spot-v12.local.hzmantu.com'
    c = Review(url)
    c.test_creat()
def commit1():
    url = 'https://spot-v12.local.hzmantu.com'
    cookie = 'BudmnGRj4PY9gvJhImupa5XEKrgswUVBf3fvy6rymAuBgahTaa6r6CjwqDXsVXxc'
    c = Review(url)
    c.test_review(213,cookie)
def commit2():
    url = 'https://spot-v12.local.hzmantu.com'
    cookie = '0WppcZNAVlnsP1wJ4qe9cCmY0BrDEESZ9pZG0IPrt7tReBKDphcPOXLGASjx9duq'
    c = Review(url)
    c.test_review(213,cookie)
def commit3():
    url = 'https://spot-v12.local.hzmantu.com'
    cookie = 'ezVd11XkPPQcz7FkSI5xg2TMiU1pw4DklxHyDGbSt3hM8kV9X69khgnUqFOayrA4'
    c = Review(url)
    c.test_review(213,cookie)
def commit4():
    url = 'https://spot-v12.local.hzmantu.com'
    cookie = 'TWMntVfOaWyYKWB4TQUCYwNQzjrlAZiZwRBlV4IW2tzDAOwhRXi6qfjy7dJjCr8f'
    c = Review(url)
    c.test_review(213, cookie)
cool1()
cool2()
commit1()
commit2()
commit3()
commit4()