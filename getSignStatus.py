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
전자서명(단건) 요청 후 반환받은 접수아이디로 인증 진행 상태를 확인합니다.
https://developers.barocert.com/reference/kakao/python/sign/api-single#GetSignStatus
"""

# 이용기관 코드
clientCode = settings.ClientCode

try :
    obj = kakaocertService.getSignStatus(clientCode, '02309110230400000010000000000003')
    print(obj.receiptID)
    print(obj.clientCode)
    print(obj.state)
    print(obj.requestDT)
    print(obj.viewDT)
    print(obj.completeDT)
    print(obj.expireDT)
    print(obj.verifyDT)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)