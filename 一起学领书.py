import tkinter as tk
import requests
import re
import time
import random
import threading
import tkinter.messagebox
import webbrowser
# 线程模块
# 本软件仅供交流学习使用，请勿用于非法用途！Github：https://github.com/zxcm1

# ===================以下为图形GUI=================== #
window = tk.Tk()
window.title('一起学刷书')
window.resizable(0, 0)
# 禁止用户修改窗口
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
dialog_width = 500
dialog_height = 400
# 前两个参数是窗口的大小，后面两个参数是窗口的位置
window.geometry("%dx%d+%d+%d" % (dialog_width, dialog_height,
                (screenwidth-dialog_width)/2, (screenheight-dialog_height)/2))


tk.Label(window, text="运行日志：").place(x='10', y='0')
tk.Label(window, text="彩虹接码").place(x='390', y='0')
tk.Label(window, text="账号：").place(x='300', y='20')
tk.Label(window, text="密码：").place(x='300', y='50')
tk.Label(window, text="讯代理").place(x='390', y='110')
tk.Label(window, text="spiderId：").place(x='275', y='130')
tk.Label(window, text="订单号：").place(x='290', y='160')
tk.Label(window, text="收货地址").place(x='340', y='240')
tk.Label(window, text="省").place(x='270', y='290')
tk.Label(window, text="市").place(x='345', y='290')
tk.Label(window, text="县").place(x='420', y='290')
tk.Label(window, text="详细地址：").place(x='270', y='320')
tk.Label(window, text="电话：").place(x='270', y='260')
tk.Label(window, text="姓名：").place(x='405', y='260')
tk.Label(window, text="课程ID/0随机：").place(x='270', y='350')

s = tk.Text(window, font=('microsoft yahei', 9))
s.place(x='10', y='20', width='250', height='370')
# 日志
user = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
user.place(x='340', y='20', width='150', height='20')
# 账号
pwq = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
pwq.place(x='340', y='50', width='150', height='20')
# 密码
spiderId = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
spiderId.place(x='340', y='130', width='150', height='20')
# spiderId
dh = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
dh.place(x='340', y='160', width='150', height='20')
# 订单号
sheng = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
sheng.place(x='290', y='290', width='50', height='20')
# 省
shi = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
shi.place(x='360', y='290', width='50', height='20')
# 市
xian = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
xian.place(x='440', y='290', width='50', height='20')
# 县
xiangxi = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
xiangxi.place(x='340', y='320', width='150', height='20')
# 详细地址
phone = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
phone.place(x='310', y='260', width='90', height='20')
# 电话
namen = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
namen.place(x='440', y='260', width='50', height='20')
# 姓名
xid = tk.Entry(window, show=None, selectbackground='DeepSkyBlue')
xid.place(x='360', y='350', width='50', height='20')
# 选择课程
s.insert(0.0, '一起学刷课程书')
s.insert(tk.END, '\n请将地址彩虹接码消息填写完整')
# ===================以下为全局变量=================== #
a = tk.StringVar()
a.set('开始')

c = 0
# 控制运行状态是否结束
token = ''
# 彩虹token
proxies = {}
# 代理
headerss = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
# Ua字典库
headersb = ''
# 随机ua
sfdl = ''
# 是否开启代理 0关闭 1开启
sfua = ''
# 是否开启随机ua 0关闭 1开启

# ===================以下为功能函数=================== #

def jg(title, message):
    # 弹窗提示
    tkinter.messagebox.showwarning(title=title, message=message)
    window.focus_force()


def zcch():
    # 注册彩虹接码账号子窗口
    root = tk.Toplevel()
    # 创建窗口
    root.grab_set()
    root.title('注册彩虹')
    root.resizable(0, 0)
    # 禁止用户修改窗口
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    dialog_width = 250
    dialog_height = 200
    # 前两个参数是窗口的大小，后面两个参数是窗口的位置
    root.geometry("%dx%d+%d+%d" % (dialog_width, dialog_height,
                  (screenwidth-dialog_width)/2, (screenheight-dialog_height)/2))
    tk.Label(root, text="彩虹注册").place(x='100', y='0')
    tk.Label(root, text="用户名：").place(x='20', y='30')
    tk.Label(root, text="登录密码：").place(x='10', y='60')
    tk.Label(root, text="确定密码：").place(x='10', y='90')
    tk.Label(root, text="二级密码：").place(x='10', y='120')

    userName = tk.Entry(root, show=None, selectbackground='DeepSkyBlue')
    userName.place(x='70', y='30', width='150', height='20')
    # 账号
    passWord = tk.Entry(root, show=None, selectbackground='DeepSkyBlue')
    passWord.place(x='70', y='60', width='150', height='20')
    # 密码
    repassWord = tk.Entry(root, show=None, selectbackground='DeepSkyBlue')
    repassWord.place(x='70', y='90', width='150', height='20')
    # 确定密码
    superCode = tk.Entry(root, show=None, selectbackground='DeepSkyBlue')
    superCode.place(x='70', y='120', width='150', height='20')
    # 二级密码

    def zc():
        url = 'http://caihongcode.net:4692/api/register?'
        payload = {
            'userName': userName.get(),
            'passWord': passWord.get(),
            'repassWord': repassWord.get(),
            'superCode': superCode.get(),
            'inviteCode': '5MLAT5SS',
            'userType': '1',
        }
        f = requests.get(url=url, params=payload, proxies=proxies).json()
        # print(f.url)
        if f['message'] == 'Success':
            jg(title='提示', message='注册成功！')

        jg(title='提示', message=f['message'])
        print(f['message'])

    def cz():
        webbrowser.open('http://caihongcode.net:8081/index.html',
                        new=2, autoraise=True)
    caihong = tk.Button(root, text='注册', font=('microsoft yahei', 9),
                        width=9, height=1, bd=1, command=zc).place(x='40', y='150')
    caihong = tk.Button(root, text='充值', font=('microsoft yahei', 9),
                        width=9, height=1, bd=1, command=cz).place(x='140', y='150')
    root.mainloop


def ch():
    # 彩虹接码
    global token
    # s.insert(tk.END,'\n登录彩虹接码...')
    userName = user.get()
    passWord = pwq.get()
    # print(userName)
    if userName == '':
        s.insert(tk.END, '\n请将彩虹账号填写完整！')
        s.see(tk.END)
    elif passWord == '':
        s.insert(tk.END, '\n请将彩虹密码填写完整！')
        s.see(tk.END)
    else:
        url = 'http://caihongcode.net:6911/api/auth?'
        data = {
            "userName": userName,
            "passWord": passWord,
            "userType": '1',
        }

        f = requests.get(url=url, params=data).json()
        print(f)
        if f['message'] == 'Success':
            result = f['result']
            token1 = result['token']
            print('余额:', result['balance'])
            msg = '\n登录成功 余额：' + result['balance']
            s.insert(tk.END, msg)
            s.see(tk.END)
            token = token1
        else:
            msg = '\n' + str(f['message'])
            s.insert(tk.END, msg)
            s.see(tk.END)


def dail():
    # 讯代理
    Id = spiderId.get()
    pdh = dh.get()
    url = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=' + \
        Id + '&orderno=' + pdh + '&returnType=2&count=1'
    f = requests.get(url).json()
    if f['RESULT'] == '请输入正确的spiderId!':
        s.insert(tk.END, '\n请输入正确的spiderId!')
        s.see(tk.END)
    elif f['RESULT'] == '订单不存在!':
        s.insert(tk.END, '\n订单不存在!')
        s.see(tk.END)
    else:
        RESULT = f['RESULT']
        postt = RESULT[0]
        print(postt)
        port = postt['port']
        ip = postt['ip']
        msg = '\n获取到IP:' + ip + ',端口:' + port
        s.insert(tk.END, msg)
        s.see(tk.END)
        http = 'http://' + ip + ':' + port
        proxies = {"http": http, "https": http}
        return proxies


def huq(token):
    # 彩虹获取手机号
    xmid = '103681'
    # 项目ID
    sc = requests.get('http://caihongcode.net:8112/api/getProjectByKeyWordAll?',
                      {'token': token, 'projectIdOrName': xmid}).json()
    result = sc['result']
    list0 = result[0]
    users_id = list0['users_id']
    # 获取账号是否收藏项目ID
    if users_id == None:
        sc = requests.get('http://caihongcode.net:8112/api/createCollection?',
                          {'token': token, 'projectId': xmid}).json()
        print(sc['result'])
        # 收藏项目ID
    url = 'http://caihongcode.net:6911/api/getPhoneNumber?token=' + token + '&projectId=' + xmid + \
        '&mobileNo=&sectionNo=&taskCount=&selectOperator=&mobileCarrier=&regionalCondition=&selectArea=&area=&taskType=1&usedNumber=&manyTimes='
    f = requests.get(url).json()
    if f['code'] == 9999:
        s.insert(tk.END, '\n彩虹余额不足！')
        s.see(tk.END)
    else:
        result = f['result']
        lin = result[0]

        mobileNo = lin['mobileNo']
        mId = lin['mId']
        print('获取到手机号：', mobileNo)
        msg = '\n获取到手机号:' + mobileNo
        s.insert(tk.END, msg)
        s.see(tk.END)
        # print(mId)
        return mobileNo, mId


def huqy(token, mId):
    # 彩虹获取验证码
    usl = 'http://caihongcode.net:6911/api/getMessage?token=' + \
        token + '&mId=' + mId + '&developer='
    for i in range(20):
        f = requests.get(usl).json()
        time.sleep(3)
        if f['message'] == 'Success':
            result = f['result']
            smsContent = result['smsContent']
            paa = re.compile('：(.*?)，')
            us = re.findall(paa, smsContent)
            print('收到验证码：', us[0])
            msg = '\n获取到验证码：' + us[0]
            s.insert(tk.END, msg)
            s.see(tk.END)
            url = 'http://caihongcode.net:6911/api/releaseNumberAll?token=' + token
            requests.get(url)
            s.insert(tk.END, '\n释放手机号')
            s.see(tk.END)
            # 释放号码
            return us
        else:
            print(f['message'])
            msg = '\n第' + str(i) + '次获取验证码'
            s.insert(tk.END, msg)
            s.see(tk.END)
    s.insert(tk.END, '\n未获取到验证码，请手动重新点击开始！')
    s.see(tk.END)


def yzm(phone):
    # 获取验证码
    url = 'https://xue.17xueba.com/m/activity99/sms.vpage'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    }

    data = {
        "mobile": phone
    }

    f = requests.post(url=url, headers=headers,
                      data=data, proxies=proxies).json()
    s.insert(tk.END, '\n发送验证码成功！')
    s.see(tk.END)
    uri = 'http://caihongcode.net:6911/api/getBalance?token=' + token
    ye = requests.get(uri).json()
    result = ye['result']
    balance = result[0]
    msg = '\n彩虹余额：' + str(balance['balance'])
    s.insert(tk.END, msg)
    s.see(tk.END)
    print(f)


def dl(yz, phone):
    # 登录拼接cookie
    url = 'https://xue.17xueba.com/m/activity99/login.vpage'
    headers = {
        'User-Agent': headersb,
    }
    data = {
        "mobile": phone,
        "smsCaptcha": yz,
    }
    f = requests.post(url=url, headers=headers, data=data, proxies=proxies)
    # print(f.json())
    he = f.headers['Set-Cookie']
    pp = ['17x_s_uid=', '17x_s_sign=']
    # 匹配17x_s_uid和17x_s_sign
    Cookie = ''
    for p in pp:
        paa = re.compile(p + '(.*?);')
        us = re.findall(paa, he)
        for i in us:
            if i == '':
                pass
            else:
                Cookie = p + i + ';' + Cookie
    msg = '\n' + str(phone) + '：登录成功'
    s.insert(tk.END, msg)
    s.see(tk.END)
    return Cookie


def sp():
    # 商品选择
    url = 'https://xue.17xueba.com/m/market/fast/getProductIds.vpage?templateId=1371'
    headers = {
        'User-Agent': headersb,
    }
    productIds = requests.get(url, headers, proxies=proxies).json()
    pr = productIds['productIds']
    # print(pr)
    bl = ''
    x = xid.get()
    kid = pr
    if x == '':
        s.insert(tk.END, '\n未设置课程ID')
        s.see(tk.END)
    elif x == '0':
        s.insert(tk.END, '\n已设置随机课程')
        s.see(tk.END)
        v = random.randint(0, len(kid))
        kid = kid[v]
        msg = '\n随机课程ID：' + str(kid)
        s.insert(tk.END, msg)
        s.see(tk.END)
        return kid
    else:
        for i in kid:
            if str(i) == x:
                msgg = '\n设置课程ID：' + str(x)
                s.insert(tk.END, msgg)
                s.see(tk.END)
                bl = x
        if bl == '':
            msggg = '\n没有找到课程ID：' + str(x)
            s.insert(tk.END, msggg)
            s.see(tk.END)
        else:
            return bl


def cx():
    url = 'https://xue.17xueba.com/m/market/fast/getProductIds.vpage?templateId=1371'
    headers = {
        'User-Agent': headersb,
    }
    productIds = requests.get(url, headers, proxies=proxies).json()
    pr = productIds['productIds']
    uri = 'https://xue.17xueba.com/m/market/lb/productInfo.vpage'
    data = {
        'productIds': str(pr),
    }
    f = requests.post(url=uri, headers=headers,
                      data=data, proxies=proxies).json()

    data = f['data']
    # print(data)
    saleCourseBeanList = data['saleCourseBeanList']
    msg = ''
    for i in saleCourseBeanList:
        courseName = str(i['courseName'])
        productId = '\nID:' + str(i['productId'])
        subject = '\n课程内容:' + str(i['subject'])
        msg = msg + productId + courseName
        # s.insert(tk.END,courseName)
        # s.see(tk.END)
        # s.insert(tk.END,productId)
        # s.see(tk.END)
        # s.insert(tk.END,subject)
        # s.see(tk.END)

        print(courseName)
        print(productId)
        print(subject)

    jg(title='课程ID', message=msg)


def dzxz(Cookie):
    # 获取位置信息
    headers = {
        'Cookie': Cookie,
        'User-Agent': headersb,
    }
    url = 'https://xue.17xueba.com/m/order/provinces.vpage'
    m = requests.post(url=url, headers=headers, proxies=proxies).json()
    dataa = m['data']
    provinces = dataa['provinces']
    name = sheng.get()
    names = shi.get()
    namess = xian.get()

    dhh = phone.get()
    namem = namen.get()
    xx = xiangxi.get()
    if dhh == '':
        s.insert(tk.END, '\n电话号未填写')
        s.see(tk.END)
    elif namem == '':
        s.insert(tk.END, '\n姓名未填写')
        s.see(tk.END)
    else:

        # print(s)
        id = ''
        idd = ''
        iddd = ''
        for i in provinces:
            if i['name'] == name:
                id = i['code']
                # print(i['code'])

        if id == '':
            # print('没有找到',name)
            s.insert(tk.END, '\n省，未填写或填写错误')
            s.see(tk.END)
        else:
            print(id, name)
            # 省
            uri = 'https://xue.17xueba.com/m/user/regionlist.vpage?regionCode=' + \
                str(id)
            c = requests.get(url=uri, headers=headers, proxies=proxies).json()
            dataa = c['data']
            regionList = dataa['regionList']

            for i in regionList:
                if i['name'] == names:
                    idd = i['code']
                    # print(i['code'])

            if idd == '':
                # print('没有找到',names)
                s.insert(tk.END, '\n市，未填写或填写错误')
                s.see(tk.END)

            else:
                print(idd, names)
                # 市
                urk = 'https://xue.17xueba.com/m/user/regionlist.vpage?regionCode=' + \
                    str(idd)
                v = requests.get(url=urk, headers=headers,
                                 proxies=proxies).json()
                dataaa = v['data']
                regionList = dataaa['regionList']

                for i in regionList:

                    if i['name'] == namess:
                        iddd = i['code']
                        # print(i['code'])
                if iddd == '':
                    # print('没有找到',namess)
                    s.insert(tk.END, '\n县，未填写或填写错误')
                    s.see(tk.END)

                else:
                    if xx == '':
                        s.insert(tk.END, '\n详细未填写')
                        s.see(tk.END)
                    else:
                        print(iddd, namess)

                        msg = [namem, dhh, id, name,
                               idd, names, iddd, namess, xx]
                        return msg


def shdz(Cookie, receiptName, phoen, backupPhone, receiptMobile, provinceName, cityCode, cityName, countryCode, countryName, detailAddress):
    # 改收货地址
    print('开始改收货地址')
    url = 'https://xue.17xueba.com/m/userorder/saveaddress.vpage'
    headers = {
        'Cookie': Cookie,
        'User-Agent': headersb,
    }

    diz = '{"receiptName":"%s","receiptMobile":"%s","backupPhone":"%s","receiptAddress":{"provinceCode":%s,"provinceName":"%s","cityCode":%s,"cityName":"%s","countryCode":%s,"countryName":"%s","detailAddress":"%s"},"defaultAddress":true}' % (
        str(receiptName), str(phoen), str(backupPhone), str(receiptMobile), str(provinceName), str(cityCode), str(cityName), str(countryCode), str(countryName), str(detailAddress))
    # print(diz)

    data = {'address': diz}

    f = requests.post(url=url, headers=headers,
                      data=data, proxies=proxies).json()
    # print(f)
    data = f['data']
    address = data['address']
    s.insert(tk.END, '\n地址修改成功！')
    s.see(tk.END)
    msg = '\n地址ID：' + str(address['id'])
    msgg = '\n地址：' + str(address['fullAddress'])
    s.insert(tk.END, msg)
    s.see(tk.END)
    s.insert(tk.END, msgg)
    s.see(tk.END)
    # print('地址ID：',address['id'])
    # print('地址：',address['fullAddress'])
    return address['id']


def bm(id, Cookie, name, templateId):
    # 报名课程
    s.insert(tk.END, '\n课程下单中')
    s.see(tk.END)
    headers = {
        'Cookie': Cookie,
        'User-Agent': headersb,
    }
    uri = 'https://xue.17xueba.com/m/market/fix-child-name.vpage'
    i = requests.post(url=uri, headers=headers, data={
                      'childName': name}, proxies=proxies).json()
    print(i)
    urb = 'https://xue.17xueba.com/m/market/version/checkAddress.vpage'
    b = requests.post(url=urb, headers=headers, data={
                      'addressId': '28530931', 'childName': name}, proxies=proxies).json()
    print(b)
    url = 'https://xue.17xueba.com/m/market/order/createuserorder.vpage'
    idd = '[{"productId":%s,"segmentId":53240}]' % (templateId)
    data = {
        'templateId': '1371',
        # 渠道ID
        'yqsource': 'jztapp-jztoperation-jztdxfwx-1046',
        'addressId': id,
        # 收货地址ID
        'goodsType': '3',
        'productInfo': idd,
        'isJzt': 'false',
        'isStu': 'false',
        'onSaleType': 'SINGLE',
        'productType': 'PRODUCT',
        'marketExtraCode': '{"templateId":"1371","yqsource":"jztapp-jztoperation-jztdxfwx-1046"}',
        'masterId': '',
        'orderSource': 'pc-web'
    }

    f = requests.post(url=url, headers=headers,
                      data=data, proxies=proxies).json()
    print(f)
    dataa = f['data']
    if dataa == None:
        s.insert(tk.END, '\n账号已被别人下单跳过此账号')
        s.see(tk.END)
    else:
        payOrderId = dataa['payOrderId']
        s.insert(tk.END, '\n下单成功')
        s.see(tk.END)
        msg = '\n订单号：' + str(payOrderId)
        s.insert(tk.END, msg)
        s.see(tk.END)
        print('订单号：', payOrderId)


def xzl():
    global sfdl
    s = var1.get()
    sfdl = s
    # print(s)


def xzi():
    global sfua
    s = var2.get()
    sfua = s
    # print(s)


def ua():

    s = random.randint(0, len(headerss))

    headers = headerss[0]
    return headers


def cc():
    headers = {
        'User-Agent': headersb,
    }
    print(requests.get('http://182.92.230.39/l.php',
          proxies=proxies, headers=headers).text)


def mainc(func, *args):
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()


def main():
    # 彩虹接码登录
    global proxies
    global headersb
    if token == "":
        s.insert(tk.END, '\n请先登录彩虹接码')
        s.see(tk.END)
        return 'bk'
    else:

        if sfdl == 1:
            proxies = dail()
            print(proxies)
            # 设置代理
        else:
            pass

        if sfua == 1:
            headersb = ua()
            print(headersb)
        else:
            pass

        m = huq(token)

        # 用彩虹接
        # 码获取手机号

        yzm(m[0])
        # # # 发验证码

        yz = huqy(token=token, mId=m[1])
        # 获取验证码

        # 填验证码
        print(yz[0])
        print(m[0])

        Cookie = dl(yz=yz[0], phone=m[0])
        # 获取Cookie
        dz = dzxz(Cookie)

        id = shdz(Cookie=Cookie, receiptName=dz[0], phoen=dz[1], backupPhone=m[0], receiptMobile=dz[2],
                  provinceName=dz[3], cityCode=dz[4], cityName=dz[5], countryCode=dz[6], countryName=dz[7], detailAddress=dz[8])
        # 改收货地址
        spp = sp()
        # 选择课程
        if spp == None:
            pass
        else:
            bm(id=id, Cookie=Cookie, name=dz[0], templateId=spp)
        # # 报名


def mainb():
    while True:
        if c == 0:
            s.insert(tk.END, '\n已结束')
            s.see(tk.END)
            break
        else:
            bk = main()
            if bk == 'bk':
                break


def xh():
    global c
    b = '开始'
    n = '结束'
    if c == 0:
        c = 1
        a.set(n)
        mainc(mainb)
    else:
        c = 0
        a.set(b)
        mainc(mainb)

# ===================以下为图形GUI=================== #


caihong = tk.Button(window, text='登录', font=('microsoft yahei', 9),
                    width=9, height=1, bd=1, command=ch).place(x='420', y='80')
zcc = tk.Button(window, text='注册/充值彩虹', font=('microsoft yahei', 9),
                width=13, height=1, bd=1, command=zcch).place(x='290', y='80')
Buttonn = tk.Button(window, text='测试', font=('microsoft yahei', 9),
                    width=9, height=1, bd=1, command=dail).place(x='420', y='190')
Buttonm = tk.Button(window, text='点击查询课程ID', font=(
    'microsoft yahei', 9), width=13, height=1, bd=1, command=cx).place(x='290', y='190')
Buttono = tk.Button(window, textvariable=a, font=(
    'microsoft yahei', 9), width=10, height=1, bd=1, command=xh).place(x='420', y='360')

var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='是否开启代理', variable=var1,
                    onvalue=1, offvalue=0, command=xzl).place(x='270', y='220')
c2 = tk.Checkbutton(window, text='是否开启随机UA', variable=var2,
                    onvalue=1, offvalue=0, command=xzi).place(x='380', y='220')

jg(title='重要提示！', message='本软件仅供交流学习使用，请勿用于非法用途！\nGithub：https://github.com/zxcm1')
window.mainloop()
