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

cms = KakaoCMS(        
    receiverHP = kakaocertService._encrypt('01012341234'),
    receiverName = kakaocertService._encrypt('홍길동'),
    receiverBirthday = kakaocertService._encrypt('19700101'),
    reqTitle = '출금동의 요청 메시지 제목',
    extraMessage = kakaocertService._encrypt('출금동의 커스텀 메시지'),
    expireIn = 1000,
    requestCorp = kakaocertService._encrypt("링크허브"),
    bankName = kakaocertService._encrypt("국민은행"),
    bankAccountNum = kakaocertService._encrypt("19-321442-1231"),
    bankAccountName = kakaocertService._encrypt("홍길동"),
    bankAccountBirthday = kakaocertService._encrypt("19700101"),
    bankServiceType = kakaocertService._encrypt("CMS"),
    appUseYN = False,
    # returnURL = 'https://kakao.barocert.com'
)

try :
    obj = kakaocertService.requestCMS(clientCode, cms)
    print(obj.receiptID)
    print(obj.scheme)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)