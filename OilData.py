import requests
import xmltodict

import json

from KeyData import *


def addr_to_lat_lon(addr):  #주소를 위도 경도로 반환하는 함수
    posUrl = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
    headers = {"Authorization": "KakaoAK " + kakaoAPIcode}
    posResult = json.loads(str(requests.get(posUrl, headers=headers).text))
    match_first = posResult['documents'][0]['address']
    return float(match_first['x']), float(match_first['y'])

class GasStation:
    def __init__(self, name, roadName, price, id):
        self.name = name
        self.roadName = roadName
        x,y = addr_to_lat_lon(roadName)
        self.x = str(x)
        self.y = str(y)
        #self.price = {"DIESEL" : dVal, "GASOLINE" : gVal, "PRE_GASOLINE": pVal}
        self.price = price
        self.id = id

    def ShowInfo(self):
        print("주유소 이름 : " + self.name)
        print("도로명 주소 : " + self.roadName)
        print("가격 : " + self.price)
        print("주유소ID : " + self.id)
        print("위도/경도 : " + self.x + ' / ' + self.y)

    def getPos(self):
        return self.x, self.y

gasStationList = [] #최저가 주유소 리스트

def FindCheapOilStation():  #gasStationList에 주유소 데이터를 담는 함수
    global gasStationList
    global oilName, localCode

    if oilName == '경유': oilCode = 'D047'
    elif oilName == '휘발유': oilCode = 'B027'
    elif oilName == '고급휘발유' : oilCode = 'B034'

    url_cheapOS = f"http://www.opinet.co.kr/api/lowTop10.do?code=F230511124&out=xml&prodcd={oilCode}&area={localCode}&cnt=10"
    result_cheapOS = xmltodict.parse(requests.get(url_cheapOS).content)
    for gas in result_cheapOS['RESULT']['OIL']:
        gs = GasStation(gas['OS_NM'], gas['NEW_ADR'], gas['PRICE'], gas['UNI_ID'])
        gasStationList.append(gs)
        gs.ShowInfo()

def FindTodayOilPrice():    #오늘 기름 평균값을 알려주는 함수(Dict로 리턴)
    url_todayOilPrice = f'http://www.opinet.co.kr/api/avgAllPrice.do?code={OilAPIcode}&out=xml'
    result_todayOilPrice = xmltodict.parse(requests.get(url_todayOilPrice).content)

    todayOil = {"고급휘발유" : (result_todayOilPrice['RESULT']['OIL'][0]['PRICE'],result_todayOilPrice['RESULT']['OIL'][0]['DIFF']),
                "휘발유" : (result_todayOilPrice['RESULT']['OIL'][1]['PRICE'],result_todayOilPrice['RESULT']['OIL'][1]['DIFF']),
                "경유" : (result_todayOilPrice['RESULT']['OIL'][2]['PRICE'],result_todayOilPrice['RESULT']['OIL'][2]['DIFF'])}
    print(todayOil)
    return todayOil

oilName = "경유"
localCode = "0116"
FindCheapOilStation()
FindTodayOilPrice()





sgcode = f"http://www.opinet.co.kr/api/areaCode.do?code={OilAPIcode}&out=xml&area=15"
gOilURL = f"http://www.opinet.co.kr/api/avgAllPrice.do?code={OilAPIcode}&out=xml"
myLocalOilPriceURL = f'http://www.opinet.co.kr/api/avgSigunPrice.do?code={OilAPIcode}&out=xml&sido=01&sigun=0116'

#result = xmltodict.parse(requests.get(url).content)
codeResult = xmltodict.parse(requests.get(sgcode).content)
gOilResult = xmltodict.parse(requests.get(gOilURL).content)
myLocalOilPriceResult = xmltodict.parse(requests.get(myLocalOilPriceURL).content)

print(codeResult) #시도코드 발행
for i in codeResult['RESULT']['OIL']:
    print(i)
# print(result) #현재 설정지역 에서 최저값 주유소 10개 검색
# print(gOilResult['RESULT']['OIL']) # 하루마다 전국 기름값 평균 데이터 정보
# print(myLocalOilPriceResult) #설정지역 평균 기름값
# print()