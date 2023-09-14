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
카카오톡 이용자에게 본인인증을 요청합니다.
https://developers.barocert.com/reference/kakao/python/identity/api#RequestIdentity
"""

# 이용기관 코드
clientCode = settings.ClientCode

identity = KakaoIdentity(        
    receiverHP = kakaocertService._encrypt('01012341234'),
    receiverName = kakaocertService._encrypt('홍길동'),
    receiverBirthday = kakaocertService._encrypt('19700101'),
    reqTitle = '인증요청 메시지 제목란',
    expireIn = 1000,
    token = kakaocertService._encrypt('본인인증요청토큰'),
    appUseYN = False,
    returnURL = 'https://kakao.barocert.com',
)

try:
    obj = kakaocertService.requestIdentity(clientCode, identity)
    print(obj.receiptID)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)