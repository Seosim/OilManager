import requests
import xmltodict

import json

from KeyData import *

class GasStation:
    def __init__(self, name, roadName, oRoadName, price, id, oilkind):
        self.name = name
        self.oldRoadName = oRoadName
        self.roadName = roadName
        x,y = addr_to_lat_lon(roadName, oRoadName)
        self.x = str(x)
        self.y = str(y)
        #self.price = {"DIESEL" : dVal, "GASOLINE" : gVal, "PRE_GASOLINE": pVal}
        self.price = price
        self.oilkind = oilkind
        self.id = id

    def ShowInfo(self):
        print("주유소 이름 : " + self.name)
        print("도로명 주소 : " + self.roadName)
        print("가격 : " + self.price)
        print("주유소ID : " + self.id)
        print("위도/경도 : " + self.x + ' / ' + self.y)

    def getInfo(self):
        infoUrl = f"http://www.opinet.co.kr/api/detailById.do?code={OilAPIcode}&out=xml&id={self.id}"
        infoResult = xmltodict.parse(requests.get(infoUrl).content)
        return infoResult["RESULT"]['OIL']


    def getPos(self):
        return self.x, self.y

class OilAPI:
    def __init__(self):
        self.localCode = "0116"
        self.oilName = "경유"

        self.gasStationList = []
        self.localCodeList = dict() #지역코드저장 (사용방법 self.localCodeList['서울'] = '01' 반환해줌)
        self.GuCodeList = {'01': {'종로구': '0101', '중구': '0102', '동대문구': '0103', '성동구': '0104', '성북구': '0105', '도봉구': '0106', '서대문구': '0107', '은평구': '0108', '마포구': '0109', '용산구': '0110', '영등포구': '0111', '동작구': '0112', '강남구': '0113', '강동구': '0114', '강서구': '0115', '구로구': '0116', '관악구': '0117', '노원구': '0118', '양천구': '0119', '중랑구': '0120', '서초구': '0121', '송파구': '0122', '광진구': '0123', '강북구': '0124', '금천구': '0125'}, '02': {'수원시': '0201', '성남시': '0202', '의정부시': '0203', '안양시': '0204', '부천시': '0205', '동두천시': '0206', '광명시': '0207', '이천시': '0208', '평택시': '0209', '구리시': '0210', '과천시': '0211', '안산시': '0212', '오산시': '0213', '의왕시': '0214', '군포시': '0215', '시흥시': '0216', '남양주시': '0217', '하남시': '0218', '고양시': '0219', '용인시': '0220', '양주시': '0221', '여주시': '0222', '화성시': '0224', '파주시': '0226', '광주시': '0228', '연천군': '0229', '포천시': '0230', '가평군': '0231', '양평군': '0232', '안성시': '0235', '김포시': '0236'}, '03': {'춘천시': '0301', '원주시': '0302', '강릉시': '0303', '속초시': '0304', '동해시': '0305', '태백시': '0306', '삼척시': '0307', '홍천군': '0322', '횡성군': '0323', '영월군': '0325', '평창군': '0326', '정선군': '0327', '철원군': '0328', '화천군': '0329', '양구군': '0330', '인제군': '0331', '고성군': '0332', '양양군': '0333'}, '04': {'청주시': '0401', '충주시': '0402', '제천시': '0403', '보은군': '0422', '옥천군': '0423', '영동군': '0424', '진천군': '0425', '괴산군': '0426', '음성군': '0427', '단양군': '0430', '증평군': '0431'}, '05': {'천안시': '0502', '공주시': '0503', '아산시': '0504', '보령시': '0505', '서산시': '0506', '논산시': '0507', '계룡시': '0508', '금산군': '0521', '부여군': '0526', '서천군': '0527', '청양군': '0529', '홍성군': '0530', '예산군': '0531', '당진시': '0533', '태안군': '0537'}, '06': {'전주시': '0601', '군산시': '0602', '익산시': '0603', '남원시': '0604', '정읍시': '0605', '김제시': '0606', '완주군': '0621', '진안군': '0622', '무주군': '0623', '장수군': '0624', '임실군': '0625', '순창군': '0627', '고창군': '0629', '부안군': '0630'}, '07': {'목포시': '0702', '여수시': '0703', '순천시': '0704', '나주시': '0705', '광양시': '0707', '담양군': '0722', '곡성군': '0723', '구례군': '0724', '고흥군': '0728', '보성군': '0729', '화순군': '0730', '장흥군': '0731', '강진군': '0732', '해남군': '0733', '영암군': '0734', '무안군': '0735', '함평군': '0737', '영광군': '0738', '장성군': '0739', '완도군': '0740', '진도군': '0741', '신안군': '0742'}, '08': {'포항시': '0801', '경주시': '0802', '김천시': '0803', '영주시': '0804', '영천시': '0805', '안동시': '0806', '구미시': '0807', '문경시': '0808', '상주시': '0809', '경산시': '0810', '군위군': '0822', '의성군': '0823', '청송군': '0825', '영양군': '0826', '영덕군': '0827', '청도군': '0832', '고령군': '0833', '성주군': '0834', '칠곡군': '0835', '예천군': '0840', '봉화군': '0842', '울진군': '0843', '울릉군': '0844'}, '09': {'창원시': '0902', '진주시': '0904', '통영시': '0906', '사천시': '0907', '김해시': '0908', '밀양시': '0909', '거제시': '0910', '양산시': '0911', '의령군': '0922', '함안군': '0923', '창녕군': '0924', '고성군': '0932', '남해군': '0934', '하동군': '0935', '산청군': '0936', '함양군': '0937', '거창군': '0938', '합천군': '0939'}, '10': {'중구': '1001', '서구': '1002', '동구': '1003', '영도구': '1004', '부산진구': '1005', '동래구': '1006', '남구': '1007', '북구': '1008', '해운대구': '1009', '사하구': '1010', '강서구': '1011', '금정구': '1012', '연제구': '1013', '수영구': '1014', '사상구': '1015', '기장군': '1031'}, '11': {'제주시': '1101', '서귀포시': '1102'}, '14': {'중구': '1401', '동구': '1402', '서구': '1403', '남구': '1404', '북구': '1405', '수성구': '1406', '달서구': '1407', '달성군': '1431'}, '15': {'중구': '1501', '동구': '1502', '미추홀구': '1503', '부평구': '1504', '서구': '1505', '남동구': '1506', '연수구': '1507', '계양구': '1508', '강화군': '1531', '옹진군': '1532'}, '16': {'동구': '1601', '서구': '1602', '북구': '1603', '광산구': '1604', '남구': '1605'}, '17': {'동구': '1701', '중구': '1702', '서구': '1703', '유성구': '1704', '대덕구': '1705'}, '18': {'중구': '1801', '남구': '1802', '동구': '1803', '북구': '1804', '울주군': '1831'}}
    #구 기준 지역코드 (사용방법 self.GuCodeList[self.localCodeList['서울']] 입력시 해당 지역 구 코드 알려줌)
        self.todayOil = dict()
        self.localPrice = dict()
        self.currentPrice = dict()

        self.GetLocalCode()
        self.FindCheapOilStation()
        self.GetTodayOilPrice()
        self.GetLocalOilPrice()
        self.GetCurrent7DaysPrice()

        self.saveOilStation = {}    #주유소 즐겨찾기 목록

    def SetOilName(self, name):
        self.oilName = name

    def SetLocalCode(self, code):
        self.localCode = code

    def GetLocalCode(self):
        sgcode = f"http://www.opinet.co.kr/api/areaCode.do?code={OilAPIcode}&out=xml&area=00"
        codeResult = xmltodict.parse(requests.get(sgcode).content)
        for ln in codeResult['RESULT']['OIL']:  # 시도코드
            self.localCodeList[ln['AREA_NM']] = ln['AREA_CD']

    def FindCheapOilStation(self):  # gasStationList에 주유소 데이터를 담는 함수
        self.gasStationList.clear()
        if self.oilName == '경유':
            oilCode = 'D047'
        elif self.oilName == '휘발유':
            oilCode = 'B027'
        elif self.oilName == '고급휘발유':
            oilCode = 'B034'

        url_cheapOS = f"http://www.opinet.co.kr/api/lowTop10.do?code={OilAPIcode}&out=xml&prodcd={oilCode}&area={self.localCode}&cnt=10"
        result_cheapOS = xmltodict.parse(requests.get(url_cheapOS).content)
        for gas in result_cheapOS['RESULT']['OIL']:
            gs = GasStation(gas['OS_NM'], gas['NEW_ADR'],gas['VAN_ADR'], gas['PRICE'], gas['UNI_ID'], self.oilName)
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

    def GetStationInfo(self, idx): #주유소 정보 리턴 함수
        return self.gasStationList[idx].getInfo()

def addr_to_lat_lon(addr, oAddr):  #주소를 위도 경도로 반환하는 함수
    posUrl = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
    headers = {"Authorization": "KakaoAK " + kakaoAPIcode}
    posResult = json.loads(str(requests.get(posUrl, headers=headers).text))

    if len(posResult['documents']):
        match_first = posResult['documents'][0]['address']
        return float(match_first['x']), float(match_first['y'])

    posUrl = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=oAddr)
    headers = {"Authorization": "KakaoAK " + kakaoAPIcode}
    posResult = json.loads(str(requests.get(posUrl, headers=headers).text))
    match_first = posResult['documents'][0]['address']
    return float(match_first['x']), float(match_first['y'])


oilAPI = OilAPI()