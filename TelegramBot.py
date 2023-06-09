import time
import OilData
import KeyData

import telepot

def handle(msg):
    global bot
    content_type, chat_type, chat_id = telepot.glance(msg)

    text = msg["text"]
    args = text.split()
    for code in OilData.oilAPI.GuCodeList.keys():
        if args[1] in OilData.oilAPI.GuCodeList[code]:
            local = OilData.oilAPI.GuCodeList[code][args[1]]
    OilData.oilAPI.TelegramCheap(local, args[2])

    message = ""

    if args[0] == "지역최저가":
        message += args[1] + " 의 최저가 주유소 정보 입니다.\n\n"
        for gas in OilData.oilAPI.telegramStation:
            oilstation = gas.getInfo()
            message += "주유소 이름 : " + oilstation['OS_NM'] + '\n' + "도로명 주소 : " + oilstation['NEW_ADR'] + '\n' \
                    + "구 주소명 : " + oilstation['VAN_ADR'] + '\n'
            for price in oilstation['OIL_PRICE']:
                if price['PRODCD'] == 'D047' : message += "경유 가격 : " + price['PRICE'] + '\n'
                elif price['PRODCD'] == 'B027': message += "휘발유 가격 : " + price['PRICE'] + '\n'
            message += "세차장 유무 : " + oilstation['CAR_WASH_YN'] + '\n'
            message += "편의점 유무 : " + oilstation['CVS_YN'] + '\n\n\n\n'
        bot.sendMessage("5719105561", message)


bot = telepot.Bot(KeyData.tel_key)
bot.sendMessage(KeyData.tel_id, "안녕하세요 기름값도우미 봇입니다.")
bot.message_loop(handle)

# while True:
#     time.sleep(10)