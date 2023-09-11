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
kakaocertService.UseLocalTimeYN = settings.UseLocalTimeYN

"""
완료된 전자서명을 검증하고 전자서명 데이터 전문(signedData)을 반환 받습니다.
카카오 보안정책에 따라 검증 API는 1회만 호출할 수 있습니다. 재시도시 오류가 반환됩니다.
전자서명 완료일시로부터 10분 이후에 검증 API를 호출하면 오류가 반환됩니다.
https://developers.barocert.com/reference/kakao/dotnetcore/login/api#VerifyLogin
"""

# 이용기관 코드
clientCode = settings.ClientCode

try :
    obj = kakaocertService.verifyLogin(clientCode, '01a1ce28b1-5a7f-45fb-807b-def79b6e63a2')
    print(obj.txID)
    print(obj.state)
    print(obj.signedData)
    print(obj.ci)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)      