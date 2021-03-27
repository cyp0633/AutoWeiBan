import WeiBanAPI
import json
import time  # time.sleep延时
import os  # 兼容文件系统
import random
from urllib import request, parse
import http.cookiejar
import json
import random
import time

baseDelayTime = 1  # 基础延时秒数

randomDelayDeviation = 1  # 叠加随机延时差

getCookiesURL = 'https://weiban.mycourse.cn/#/login'  # 请求Cookies URL

loginURL = 'https://weiban.mycourse.cn/pharos/login/login.do'  # 登录请求 URL

getNameURL = 'https://weiban.mycourse.cn/pharos/my/getInfo.do'  # 请求姓名 URL

getProgressURL = 'https://weiban.mycourse.cn/pharos/project/showProgress.do'  # 请求进度 URL

getListCourseURL = 'https://weiban.mycourse.cn/pharos/usercourse/listCategory.do'  # 请求课程列表 URL

finishCourseURL = 'https://weiban.mycourse.cn/pharos/usercourse/finish.do'  # 请求完成课程URL

getRandImageURL = 'https://weiban.mycourse.cn/pharos/login/randImage.do'  # 验证码URL

doStudyURL = 'https://weiban.mycourse.cn/pharos/usercourse/study.do'  # 学习课程URL

# 获取验证码以及验证码ID URL
genQRCodeURL = 'https://weiban.mycourse.cn/pharos/login/genBarCodeImageAndCacheUuid.do'

# 用于二维码登录刷新登录状态
loginStatusURL = 'https://weiban.mycourse.cn/pharos/login/barCodeWebAutoLogin.do'

# 新接口 通过目录id获取课程列表
listCourseURL = 'https://weiban.mycourse.cn/pharos/usercourse/listCourse.do'

tenantCode = '41008202'  # 湖南大学ID

"""
# 密码登录，已经失效
def pwLogin():
    print(
        '默认院校为吉林大学珠海学院，ID:' + tenantCode + '\n'
        + '若有需要，请自行抓包获取院校ID修改' + '\n'
    )

    # 登录信息输入
    account = input('请输入账号\n')
    password = input('请输入密码\n')

    # 获取Cookies
    print('\n获取Cookies中')
    cookie = WeiBanAPI.getCookie()
    print('Cookies获取成功')
    time.sleep(2)

    randomTimeStamp = random.randint(1E8, 1E12)
    print('验证码,浏览器打开 https://weiban.mycourse.cn/pharos/login/randImage.do?time={}'.format(randomTimeStamp))

    verifyCode = input('请输入验证码')

    # 登录请求
    loginResponse = WeiBanAPI.login(account, password, tenantCode, randomTimeStamp, verifyCode, cookie)
    return loginResponse
"""


def main():
    # 显示License
    '''
    with open("./LICENSE", encoding="utf-8") as licenseFile:
        print(licenseFile.read())
    '''
    # 登录
    # loginResponse = pwLogin()
    # 补打空cookie
    print("正在连接网课服务器...\n")
    cookie = ''

    loginResponse = WeiBanAPI.qrLogin()

    # Gobal
    userProjectId = ''
    userId = ''
    ###

    try:
        print('登录成功，userName:' + loginResponse['data']['userName'])

        # 设置全局数据
        userProjectId = loginResponse['data']['preUserProjectId']
        userId = loginResponse['data']['userId']

        time.sleep(2)
    except BaseException:
        print('登录失败')
        print(loginResponse)  # TODO: 这里的loginResponse调用没有考虑网络错误等问题
        exit(0)

    # 请求解析并打印用户信息
    try:
        print('请求用户信息')
        stuInfoResponse = WeiBanAPI.getStuInfo(loginResponse['data']['userId'],
                                               tenantCode,
                                               cookie)
        print('用户信息：' + stuInfoResponse['data']['realName'] + '\n'
              + stuInfoResponse['data']['orgName']
              + stuInfoResponse['data']['specialtyName']
              )
        time.sleep(2)
    except BaseException:
        print('解析用户信息失败，将尝试继续运行，请注意运行异常')

    # 请求课程完成进度
    try:
        getProgressResponse = WeiBanAPI.getProgress(loginResponse['data']['preUserProjectId'],
                                                    tenantCode,
                                                    cookie)
        print('课程总数：' + str(getProgressResponse['data']['requiredNum']) + '\n'
              + '完成课程：' +
              str(getProgressResponse['data']['requiredFinishedNum']) + '\n'
              + '结束时间' + str(getProgressResponse['data']['endTime']) + '\n'
              + '剩余天数' + str(getProgressResponse['data']['lastDays'])
              )
        time.sleep(2)
    except BaseException:
        print('解析课程进度失败，将尝试继续运行，请注意运行异常')

    getListCourseResponse = {}

    # 请求课程列表
    try:
        getListCourseResponse = WeiBanAPI.getListCourse(loginResponse['data']['preUserProjectId'],
                                                        '3',
                                                        tenantCode,
                                                        '',
                                                        cookie)
        time.sleep(2)
    except BaseException:
        print('请求课程列表失败')

    print('解析课程列表并发送完成请求')

    for i in getListCourseResponse['data']:
        print('\n----章节码：' + i['categoryCode'] + '章节内容：' + i['categoryName'])
        courseList = WeiBanAPI.getCourseListByCategoryCode(
            i['categoryCode'], userProjectId, userId, tenantCode)
        for j in courseList['data']:
            print('课程内容：' + j['resourceName'] +
                  '\nuserCourseId:' + j['userCourseId'])

            if (j['finished'] == 1):
                print('已完成')
            else:
                print('发送完成请求')
                WeiBanAPI.doStudy(
                    userProjectId, j['resourceId'], tenantCode, userId)
                WeiBanAPI.finishCourse(j['userCourseId'], tenantCode, cookie)

                delayInt = WeiBanAPI.getRandomTime()
                print('\n随机延时' + str(delayInt))
                time.sleep(delayInt)


def getCookie():
    cookie = http.cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    return cookie


def qrLogin():
    qrCodeID = getQRCode()
    print(qrCodeID)
    print("完成扫码后输入 y 进行下一步：")

    _confirm_qr_code()

    response = _get_login_response(qrCodeID)
    current = time.time()
    while response['code'] != '0':
        print('未侦测到登录，请重试！')
        now = time.time()
        if _confirm_qr_code() and now - current > 5:
            response = _get_login_response(qrCodeID)
            current = now
        else:
            print("请不要请求过快！推荐间隔5s")
            continue

    return response


def _get_login_response(qrCodeID):
    responseText = getLoginStatus(qrCodeID)
    responseJSON = json.loads(responseText)
    return responseJSON


def _confirm_qr_code():
    print("请输入 y 确认扫码或者输入 Ctrl+c 退出程序")
    confirm = input()
    while confirm.lower() != "y":
        print("请按 y 键确认！！")
        confirm = input()

    return True

# 获取学生信息


def getStuInfo(userId, tenantCode, cookie):
    logger('开始请求用户数据')
    param = {
        'userId': userId,
        'tenantCode': tenantCode
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=getNameURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    logger(responseText)
    responseJSON = json.loads(responseText)
    return responseJSON


# 获取课程进度
def getProgress(userProjectId, tenantCode, cookie):
    param = {
        'userProjectId': userProjectId,
        'tenantCode': tenantCode
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=getProgressURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    return responseJSON


# 获取课程列表
def getListCourse(userProjectId, chooseType, tenantCode, name, cookie):
    param = {
        'userProjectId': userProjectId,
        'chooseType': chooseType,
        'tenantCode': tenantCode,
        'name': name
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=getListCourseURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    return responseJSON


# 完成课程请求
def finishCourse(userCourseId, tenantCode, cookie):
    param = {
        'userCourseId': userCourseId,
        'tenantCode': tenantCode,
    }
    url_values = parse.urlencode(param)  # GET请求URL参数
    req = request.Request(url=finishCourseURL + '?' + url_values, method='GET')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    print(responseText)


def getRandomTime():
    return baseDelayTime + random.randint(0, randomDelayDeviation)


def doStudy(userProjectId, userCourseId, tenantCode, userId):
    param = {
        'userProjectId': userProjectId,
        'courseId': userCourseId,
        'tenantCode': tenantCode,
        'userId': userId
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=doStudyURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    print(responseText)
    return


# 获取并返回QRCode 链接以及 QRCode ID
def getQRCode():
    req = request.Request(url=genQRCodeURL, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    logger('Response:' + responseText)
    print('请浏览器打开下面的二维码登录链接，使用二维码登录（若无法登录请检查是否已经在网页端绑定微信登录功能）')
    print(responseJSON['data']['imagePath'] + '\n')
    return responseJSON['data']['barCodeCacheUserId']


# 用于二维码登录，刷新是否已经成功登录
def getLoginStatus(qrCodeID):
    param = {
        'barCodeCacheUserId': qrCodeID
    }
    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=loginStatusURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    logger('Response:' + responseText)
    return responseText


# 获取课程列表，新接口
def getCourseListByCategoryCode(categoryCode, userProjectId, userId, tenantCode):
    param = {
        'userProjectId': userProjectId,
        'chooseType': 3,
        'categoryCode': categoryCode,
        'name': '',
        'userId': userId,
        'tenantCode': tenantCode,
        'token': ''
    }
    print(param)

    data = bytes(parse.urlencode(param), encoding='utf-8')
    req = request.Request(url=listCourseURL, data=data, method='POST')
    responseStream = request.urlopen(req)
    responseText = responseStream.read().decode('utf-8')
    responseJSON = json.loads(responseText)
    return responseJSON


def logger(str):
    print('log >>> ' + str)


if __name__ == '__main__':
    main()
