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
카카오톡 이용자에게 복수(최대 20건) 문서의 전자서명을 요청합니다.
https://developers.barocert.com/reference/kakao/python/sign/api-multi#RequestMultiSign
"""

# 이용기관 코드
clientCode = settings.ClientCode

multiSignTokens = []
for x in range(0,5):
    multiSignTokens.append(
        KakaoMultiSignTokens(
            reqTitle = "전자서명(복수) 요청 메시지 제목" + str(x),
            token = kakaocertService._encrypt("전자서명(복수) 요청 원문" + str(x)) 
        )
    )    

multiSign = KakaoMultiSign(        
    receiverHP = kakaocertService._encrypt('01012341234'),
    receiverName = kakaocertService._encrypt('홍길동'),
    receiverBirthday = kakaocertService._encrypt('19700101'),
    reqTitle = '전자서명(복수) 요청 메시지 제목',
    expireIn = 1000,
    tokens = multiSignTokens,
    tokenType = 'TEXT',
    appUseYN = False,
    # returnURL = 'https://kakao.barocert.com'
)

try :
    obj = kakaocertService.requestMultiSign(clientCode, multiSign)
    print(obj.receiptID)
    print(obj.scheme)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)