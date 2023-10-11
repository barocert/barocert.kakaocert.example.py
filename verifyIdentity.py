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
완료된 전자서명을 검증하고 전자서명값(signedData)을 반환 받습니다.
반환받은 전자서명값(signedData)과 [1. RequestIdentity] 함수 호출에 입력한 Token의 동일 여부를 확인하여 이용자의 본인인증 검증을 완료합니다.
카카오 보안정책에 따라 검증 API는 1회만 호출할 수 있습니다. 재시도시 오류가 반환됩니다.
전자서명 완료일시로부터 10분 이후에 검증 API를 호출하면 오류가 반환됩니다.
https://developers.barocert.com/reference/kakao/python/identity/api#VerifyIdentity
"""

# 이용기관 코드
clientCode = settings.ClientCode

try :
    obj = kakaocertService.verifyIdentity(clientCode, '02309110230400000010000000000002')
    print(obj.receiptID)
    print(obj.state)
    print(obj.signedData)
    print(obj.ci)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)