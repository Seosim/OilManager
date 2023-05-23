import tkinter as tk
import tkinter.ttk
from PIL import ImageTk

import MapData
import OilData

Width = 700
Height = 700

MapWidth = 300
MapHeight = 300

ChartWidth = Width
ChartHeight = 400

gasstations = []
gasstation = {
    "name": "sihmng",  # 주유소 이름
    "address": "경기 시흥시",  # 주유소 주소
    "lat": 0,  # 위도
    "lng": 0,  # 경도
    "gasoline": 1604,  # 휘발유값
    "Diesel" : 1495 # 경유 값
}
gasstations.append(gasstation)
# for item in items:
#     gasstation = {
#         "name": item.findtext("yadmNm"),  # 병원 이름
#         "address": item.findtext("addr"),  # 병원 주소
#         "lat": item.findtext("YPos"),  # 위도
#         "lng": item.findtext("XPos"),  # 경도
#         "doctors": item.findtext("drTotCnt"),  # 의사수
#     }
#     hospitals.append(hospital)

class Program:
    def up(self):
        pass
    def search(self):
        pass

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("기름값 도우미")
        self.font = "Arial 25"
        self.mfont = "Arial 15"


        #서심코드 : 오늘 기름 가격 그래프 표시 테스트
        self.notebook = tkinter.ttk.Notebook(self.window, width=Width, height=Height)
        self.frame1 = tk.Frame(self.window)
        self.notebook.add(self.frame1, text="ONE")
        self.notebook.pack()

        self.n1Title = tk.Label(self.frame1, text="오늘의 기름값", font=self.font)
        self.n1Title.place(x=0, y= 30)
        self.n1oilName1 = tk.Label(self.frame1, text="경유",font=self.mfont)
        self.n1oilName1.place(x=100, y= 130)
        self.n1oilPrice1 = tk.Label(self.frame1, text=str(OilData.oilAPI.todayOil["경유"][0]+ " / " + OilData.oilAPI.todayOil["경유"][1] ),font=self.mfont)
        self.n1oilPrice1.place(x=100, y= 200)

        self.frame2 = tk.Frame(self.window)
        self.notebook.add(self.frame2, text="TWO")
        self.notebook.pack()
        #-----------------------------상단에 글씨 띄우는 캔버스--------------------------------         START
        MainCanvas = tk.Canvas(self.frame2, bg = 'white', width=Width, height=Height/20)
        MainCanvas.pack()
        MainCanvas.create_text(Width / 2, Height / 40, text = '지역 주유소 최저가 검색')
        #-----------------------------상단에 글씨 띄우는 캔버스--------------------------------         END


        #----------------------------기름 종류, 지도 그리는 프레임---------------------------------     START
        frame1 = tk.Frame(self.frame2)
        frame1.pack(side=tk.TOP)
        #------------------------------지도를 그리는 캔버스-----------------------------------          START
        photo = ImageTk.PhotoImage(MapData.image)   #지도이미지
        mapLabel = tk.Label(frame1, image=photo, width=MapWidth, height=MapHeight)
        mapLabel.pack(side=tk.RIGHT)
        #------------------------------지도를 그리는 캔버스-----------------------------------          END

        #-------------------------------지역 선택하는 콤보박스---------------------------------         START
        # selected_gu = tk.StringVar()
        # selected_gu.set("시흥시")  # 초기값 설정
        # gu_options = set([gasstations['address'].split()[1] for hospital in hospitals])
        # gu_combo = ttk.Combobox(root, textvariable=selected_gu, values=list(gu_options))
        # gu_combo.pack()
        #-------------------------------지역 선택하는 콤보박스---------------------------------         END

        #-------------------------------기름 종류 선택하는 박스---------------------------------        START
        # 체크 박스
        tk.Checkbutton(frame1, text='경유', command=self.up).pack(side=tk.TOP)
        tk.Checkbutton(frame1, text='휘발유', command=self.up).pack(side=tk.TOP)
        tk.Checkbutton(frame1, text='고급 휘발유', command=self.up).pack(side=tk.TOP)
        tk.Checkbutton(frame1, text='가솔린', command=self.up).pack(side=tk.TOP)
        # 버튼
        tk.Button(frame1, text="검색", command=self.search).pack(side=tk.TOP)

        #-------------------------------기름 종류 선택하는 박스---------------------------------        END

        #----------------------------기름 종류, 지도 그리는 프레임---------------------------------     END

        #----------------------------기름값 도표 그리는 캔버스---------------------------------         START
        Chart = tk.Canvas(self.frame2, width=ChartWidth, height=ChartHeight)
        Chart.pack(side=tk.TOP)

        Chart.create_rectangle(100, ChartHeight-70, ChartWidth - 100, ChartHeight-50, fill = 'black', tags='Chart')
        # tk.Button(Chart, text="검색", command=self.search).pack(side=tk.TOP)
        #----------------------------기름값 도표 그리는 캔버스---------------------------------         END



        self.window.mainloop()


Program()        