import requests
import xmltodict

import json

from KeyData import *

oilName = "경유"
localCode = "0116"

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

class OilAPI:
    def __init__(self):
        self.localCode = "0116"
        self.oilName = "경유"

        self.gasStationList = []
        self.todayOil = dict()
        self.localPrice = dict()
        self.currentPrice = dict()

        self.FindCheapOilStation()
        self.GetTodayOilPrice()
        self.GetLocalOilPrice()
        self.GetCurrent7DaysPrice()

        self.saveOilStation = {}    #주유소 즐겨찾기 목록

    def FindCheapOilStation(self):  # gasStationList에 주유소 데이터를 담는 함수
        if self.oilName == '경유':
            oilCode = 'D047'
        elif self.oilName == '휘발유':
            oilCode = 'B027'
        elif self.oilName == '고급휘발유':
            oilCode = 'B034'

        url_cheapOS = f"http://www.opinet.co.kr/api/lowTop10.do?code=F230511124&out=xml&prodcd={oilCode}&area={self.localCode}&cnt=10"
        result_cheapOS = xmltodict.parse(requests.get(url_cheapOS).content)
        for gas in result_cheapOS['RESULT']['OIL']:
            gs = GasStation(gas['OS_NM'], gas['NEW_ADR'], gas['PRICE'], gas['UNI_ID'])
            self.gasStationList.append(gs)

    def GetTodayOilPrice(self):  # 오늘 기름 평균값을 알려주는 함수(Dict로 리턴)
        url_todayOilPrice = f'http://www.opinet.co.kr/api/avgAllPrice.do?code={OilAPIcode}&out=xml'
        result_todayOilPrice = xmltodict.parse(requests.get(url_todayOilPrice).content)

        self.todayOil = {"고급휘발유": (result_todayOilPrice['RESULT']['OIL'][0]['PRICE'], result_todayOilPrice['RESULT']['OIL'][0]['DIFF']),
                    "휘발유": (result_todayOilPrice['RESULT']['OIL'][1]['PRICE'], result_todayOilPrice['RESULT']['OIL'][1]['DIFF']),
                    "경유": (result_todayOilPrice['RESULT']['OIL'][2]['PRICE'], result_todayOilPrice['RESULT']['OIL'][2]['DIFF'])}

    def GetLocalOilPrice(self):
        url_localOilPrice = f'http://www.opinet.co.kr/api/avgSidoPrice.do?code={OilAPIcode}&out=xml'
        result_localOilPrice = xmltodict.parse(requests.get(url_localOilPrice).content)

        for i, gas in enumerate(result_localOilPrice['RESULT']['OIL']):
            if i < 5: continue

            if i % 5 == 0:
                self.localPrice[gas['SIDONM']] = {}
                self.localPrice[gas['SIDONM']]["휘발유"] = (gas['PRICE'], gas['DIFF'])
            if i % 5 == 1:
                self.localPrice[gas['SIDONM']]["고급 휘발유"] = (gas['PRICE'], gas['DIFF'])
            if i % 5 == 3:
                self.localPrice[gas['SIDONM']]["경유"] = (gas['PRICE'], gas['DIFF'])

    def GetCurrent7DaysPrice(self):  # 현재 선택된 지역에 어제까지 최근 7일간 기름값
        if self.oilName == '경유':
            oilCode = 'D047'
        elif self.oilName == '휘발유':
            oilCode = 'B027'
        elif self.oilName == '고급휘발유':
            oilCode = 'B034'

        url_currentOilPrice = \
            f'http://www.opinet.co.kr/api/areaAvgRecentPrice.do?' \
            f'code={OilAPIcode}&out=xml&area={self.localCode}&prodcd={oilCode}'
        result_currentOilPrice = xmltodict.parse(requests.get(url_currentOilPrice).content)

        for i, gas in enumerate(result_currentOilPrice['RESULT']['OIL']):
            self.currentPrice[gas['DATE']] = gas['PRICE']

    def SaveOilStation(self, idx):  #주유소 즐겨찾기 함수
        g = self.gasStationList[idx]
        self.saveOilStation[g.name] = g

    def RemoveOilStation(self, name):   #주유소 즐겨찾기 해제 함수
        self.saveOilStation.pop(name)

def addr_to_lat_lon(addr):  #주소를 위도 경도로 반환하는 함수
    posUrl = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
    headers = {"Authorization": "KakaoAK " + kakaoAPIcode}
    posResult = json.loads(str(requests.get(posUrl, headers=headers).text))
    match_first = posResult['documents'][0]['address']
    return float(match_first['x']), float(match_first['y'])

sgcode = f"http://www.opinet.co.kr/api/areaCode.do?code={OilAPIcode}&out=xml&area=15"
codeResult = xmltodict.parse(requests.get(sgcode).content)
for i in codeResult['RESULT']['OIL']:   #시도코드
    # print(i)
    pass

oilAPI = OilAPI()