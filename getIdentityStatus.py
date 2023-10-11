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
본인인증 요청 후 반환받은 접수아이디로 본인인증 진행 상태를 확인합니다.
https://developers.barocert.com/reference/kakao/python/identity/api#GetIdentityStatus
"""

# 이용기관 코드
clientCode = settings.ClientCode

try:
    obj = kakaocertService.getIdentityStatus(clientCode, '02309110230400000010000000000002')
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