# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import settings
from datetime import datetime
from barocert import *

kakaocertService = KakaocertService(settings.LinkID, settings.SecretKey)
kakaocertService.IPRestrictOnOff = settings.IPRestrictOnOff
kakaocertService.UseStaticIP = settings.UseStaticIP

"""
카카오톡 이용자에게 자동이체 출금동의를 요청합니다.
https://developers.barocert.com/reference/kakao/python/cms/api#RequestCMS
"""

# 이용기관 코드
clientCode = settings.ClientCode

try :
    obj = kakaocertService.getCMSStatus(clientCode, '02309110230400000010000000000005')
    print(obj.receiptID)
    print(obj.clientCode)
    print(obj.state)
    print(obj.expireIn)
    print(obj.callCenterName)
    print(obj.callCenterNum)
    print(obj.reqTitle)
    print(obj.authCategory)
    print(obj.returnURL)
    print(obj.requestDT)
    print(obj.viewDT)
    print(obj.completeDT)
    print(obj.expireDT)
    print(obj.verifyDT)
    print(obj.scheme)
    print(obj.appUseYN)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)