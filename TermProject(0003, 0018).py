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
ChartHeight = 300

class Program:
    def SetChart(self):
        self.Chart = tk.Canvas(self.frame1, width=ChartWidth, height=ChartHeight)
        self.Chart.place(y=Height - ChartHeight)

    def DrawChart(self, kind):     #  - 고인호
        self.Chart.delete("Chart")
        if kind == 'dissel':
        # -------------------------------------- 전국 경유 막대그래프 ---------------------------------------------
            minprice = (float)(OilData.oilAPI.localPrice['서울']['경유'][0])
            minlocal = ''
            for i in OilData.oilAPI.localPrice:
                if (float)(OilData.oilAPI.localPrice[i]['경유'][0]) < minprice:
                    minprice = (float)(OilData.oilAPI.localPrice[i]['경유'][0])
                    minlocal = i

            # self.seoul = tk.Label(self.frame1, text=OilData.oilAPI.localPrice['서울']['경유'][0],font=self.mfont)
            # self.seoul.place(x=120, y= 50)

            count = 0
            for i in OilData.oilAPI.localPrice:
                if i == minlocal:
                    color = 'red3'
                else:
                    color = 'pale green'
                self.Chart.create_rectangle(110 + 30 * count, ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['경유'][0]) - minprice) - 100, 130 + 30 * count, ChartHeight - 20, fill = color, tags='Chart')        
                tk.Label(self.Chart, text=i, font=self.mfont).place(x=105 + 30 * count, y= ChartHeight-20)  # , tags='Chart'
                count += 1

            self.Chart.create_rectangle(50, ChartHeight - 40, ChartWidth - 50, ChartHeight - 20, fill = 'black', tags='Chart')
        # -------------------------------------- 전국 경유 막대그래프 ---------------------------------------------
        elif kind == 'gasoline':
        # -------------------------------------- 전국 휘발유 막대그래프 ---------------------------------------------
            minprice = (float)(OilData.oilAPI.localPrice['서울']['휘발유'][0])
            minlocal = ''
            for i in OilData.oilAPI.localPrice:
                if (float)(OilData.oilAPI.localPrice[i]['휘발유'][0]) < minprice:
                    minprice = (float)(OilData.oilAPI.localPrice[i]['휘발유'][0])
                    minlocal = i

            # self.seoul = tk.Label(self.frame1, text=OilData.oilAPI.localPrice['서울']['경유'][0],font=self.mfont)
            # self.seoul.place(x=120, y= 50)

            count = 0
            for i in OilData.oilAPI.localPrice:
                if i == minlocal:
                    color = 'red3'
                else:
                    color = 'pale green'
                self.Chart.create_rectangle(110 + 30 * count, ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['휘발유'][0]) - minprice) - 100, 130 + 30 * count, ChartHeight - 20, fill = color, tags='Chart')        
                tk.Label(self.Chart, text=i, font=self.mfont).place(x=105 + 30 * count, y= ChartHeight-20)  # , tags='Chart'
                count += 1

            self.Chart.create_rectangle(50, ChartHeight - 40, ChartWidth - 50, ChartHeight - 20, fill = 'black', tags='Chart')
        # -------------------------------------- 전국 휘발유 막대그래프 ---------------------------------------------
        elif kind == "premiumgasoline":
        # -------------------------------------- 전국 고급 휘발유 막대그래프 ---------------------------------------------
            minprice = (float)(OilData.oilAPI.localPrice['서울']['고급 휘발유'][0])
            minlocal = ''
            for i in OilData.oilAPI.localPrice:
                if (float)(OilData.oilAPI.localPrice[i]['고급 휘발유'][0]) < minprice:
                    minprice = (float)(OilData.oilAPI.localPrice[i]['고급 휘발유'][0])
                    minlocal = i

            # self.seoul = tk.Label(self.frame1, text=OilData.oilAPI.localPrice['서울']['경유'][0],font=self.mfont)
            # self.seoul.place(x=120, y= 50)

            count = 0
            for i in OilData.oilAPI.localPrice:
                if i == minlocal:
                    color = 'red3'
                else:
                    color = 'pale green'
                self.Chart.create_rectangle(110 + 30 * count, ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['고급 휘발유'][0]) - minprice) - 100, 130 + 30 * count, ChartHeight - 20, fill = color, tags='Chart')        
                tk.Label(self.Chart, text=i, font=self.mfont).place(x=105 + 30 * count, y= ChartHeight-20)  # , tags='Chart'
                count += 1

            self.Chart.create_rectangle(50, ChartHeight - 40, ChartWidth - 50, ChartHeight - 20, fill = 'black', tags='Chart')
        # -------------------------------------- 전국 고급 휘발유 막대그래프 ---------------------------------------------        

    def up(self):
        pass
    def search(self):
        pass

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("기름값 도우미")
        self.font = "Arial 15"
        self.mfont = "Arial 10"
        self.favoriteList = []
        self.selectedOilStation = None

        # 오늘 기름 가격 그래프 표시 테스트 - 서종배
        self.notebook = tkinter.ttk.Notebook(self.window, width=Width, height=Height)
        self.frame1 = tk.Frame(self.window)
        self.notebook.add(self.frame1, text="ONE")
        self.notebook.pack()
        # 오늘 기름 가격 그래프 표시 테스트 - 서종배

        # 기름 선택 버튼    - 고인호
        self.disselbutton = tk.Button(self.frame1, text='경유', command=lambda row="dissel": self.DrawChart(row))
        self.disselbutton.place(x=Width/2 - 100, y=50)

        self.gasolinebutton = tk.Button(self.frame1, text='휘발유', command=lambda row="gasoline": self.DrawChart(row))
        self.gasolinebutton.place(x=Width/2 - 50, y = 50)

        self.premiumgasolinebutton = tk.Button(self.frame1, text='고급 휘발유', command=lambda row="premiumgasoline": self.DrawChart(row))
        self.premiumgasolinebutton.place(x=Width/2 + 10, y = 50)
        # 기름 선택 버튼    - 고인호

        # 캔버스 set함수    - 고인호
        self.SetChart()
        # 캔버스 set함수    - 고인호

        self.n1Title = tk.Label(self.frame1, text="오늘의 기름값", font=self.font)
        self.n1Title.place(x=Width / 2 - 75, y= 0)
        self.n1oilName1 = tk.Label(self.frame1, text="경유",font=self.mfont)
        self.n1oilName1.place(x=40, y= 150)
        self.n1oilPrice1 = tk.Label(self.frame1, text=str(OilData.oilAPI.todayOil["경유"][0]+ " / " + OilData.oilAPI.todayOil["경유"][1] ),font=self.mfont)
        self.n1oilPrice1.place(x=10, y= 180)

        # self.n1oilName2 = tk.Label(self.frame1, text="휘발유",font=self.mfont)
        # self.n1oilName2.place(x=30, y= 350)
        # self.n1oilPrice2 = tk.Label(self.frame1, text=str(OilData.oilAPI.todayOil["휘발유"][0]+ " / " + OilData.oilAPI.todayOil["휘발유"][1] ),font=self.mfont)
        # self.n1oilPrice2.place(x=10, y= 380)

        # self.n1oilName3 = tk.Label(self.frame1, text="고급휘발유",font=self.mfont)
        # self.n1oilName3.place(x=20, y= 550)
        # self.n1oilPrice3 = tk.Label(self.frame1, text=str(OilData.oilAPI.todayOil["고급휘발유"][0]+ " / " + OilData.oilAPI.todayOil["휘발유"][1] ),font=self.mfont)
        # self.n1oilPrice3.place(x=10, y= 580)

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
        photo = ImageTk.PhotoImage(MapData.map.GetImage(0))   #지도이미지
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