from PIL import Image
import requests
import io

import OilData
from KeyData import *

class Map:
    def __init__(self):
        self.endpoint = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
        self.headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
        }
        # 중심 좌표
        self.lon, self.lat = OilData.oilAPI.gasStationList[0].getPos()
        self.center = f"{self.lon},{self.lat}"
        # 줌 레벨 - 0 ~ 20
        self.level = 14
        # 가로 세로 크기 (픽셀)
        self.w, self.h = 300, 300
        # 지도 유형 - basic, traffic, satellite, satellite_base, terrain
        self.maptype = "basic"
        # 반환 이미지 형식 - jpg, jpeg, png8, png
        self.format = "png"
        # 고해상도 디스펠레이 지원을 위한 옵션 - 1, 2
        self.scale = 1
        # 마커
        self.markers = f"""type:d|size:mid|pos:{self.lon} {self.lat}|color:red"""
        # 라벨 언어 설정 - ko, en, ja, zh
        self.lang = "ko"
        # 대중교통 정보 노출 - Boolean
        self.public_transit = True
        # 서비스에서 사용할 데이터 버전 파라미터 전달 CDN 캐시 무효화
        self.dataversion = ""

        self.idx = 0

        #이미지 데이터
        self.image = None

    def SetIdx(self, idx):
        self.idx = idx
        self.lon, self.lat = OilData.oilAPI.gasStationList[self.idx].getPos()
        self.center = f"{self.lon},{self.lat}"
        self.markers = f"""type:d|size:mid|pos:{self.lon} {self.lat}|color:red"""
        return self.GetImage()

    def SetStarIdx(self, idx):
        self.idx = idx
        self.lon, self.lat = OilData.oilAPI.saveOilStation[self.idx].getPos()
        self.center = f"{self.lon},{self.lat}"
        self.markers = f"""type:d|size:mid|pos:{self.lon} {self.lat}|color:red"""
        return self.GetImage()

    def ZoomIn(self):   #지도 확대
        self.level += 1
        if self.level > 17: self.level = 17
        self.markers = f"""type:d|size:mid|pos:{self.lon} {self.lat}|color:red"""
        return self.GetImage()

    def ZoomOut(self):
        self.level -= 1
        if self.level < 10: self.level = 10
        return self.GetImage()

    def GetImage(self):
        # URL
        url = f"{self.endpoint}?center={self.center}&level={self.level}&w={self.w}&h={self.h}&maptype={self.maptype}&format={self.format}&scale={self.scale}&markers={self.markers}&lang={self.lang}&public_transit={self.public_transit}&dataversion={self.dataversion}"
        res = requests.get(url, headers=self.headers)

        image_data = io.BytesIO(res.content)
        self.image = Image.open(image_data)
        return self.image

map = Map()

