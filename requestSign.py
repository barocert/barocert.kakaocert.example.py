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
카카오톡 이용자에게 단건(1건) 문서의 전자서명을 요청합니다.
https://developers.barocert.com/reference/kakao/python/sign/api-single#RequestSign
"""

# 이용기관 코드
clientCode = settings.ClientCode

sign = KakaoSign(        
    receiverHP = kakaocertService._encrypt('01012341234'),
    receiverName = kakaocertService._encrypt('홍길동'),
    receiverBirthday = kakaocertService._encrypt('19700101'),
    reqTitle = '인증요청 메시지 제목란',
    expireIn = 1000,
    token = kakaocertService._encrypt('전자서명단건테스트데이터'),
    tokenType = 'TEXT',
    appUseYN = False,
    returnURL = 'https://kakao.barocert.com'
)

try :
    obj = kakaocertService.requestSign(clientCode, sign)
    print(obj.receiptID)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)