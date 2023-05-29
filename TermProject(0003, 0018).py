import tkinter as tk
import tkinter.ttk
import tkinter.font
from PIL import ImageTk

import MapData
import OilData

Width = 700
Height = 700

MapWidth = 300
MapHeight = 300

ChartWidth = Width
ChartHeight = 300
Chart2Height = 250

class Program:
    def DrawChart(self, kind):     #  - 고인호
        self.Chart = tk.Canvas(self.frame1, width=ChartWidth, height=ChartHeight, bg=self.skycolor)
        self.Chart.place(y=Height - ChartHeight * 1.5)

        if kind == 'dissel':
            self.n1oilName1 = tk.Label(self.Chart, text="경유",font=self.mfont, bg=self.skycolor)
            self.n1oilName1.place(x=Width / 2 - 25, y= 0)
            self.n1oilPrice1 = tk.Label(self.Chart, text=str(OilData.oilAPI.todayOil["경유"][0]+ " / " + OilData.oilAPI.todayOil["경유"][1] ),font=self.mfont, bg=self.skycolor)
            self.n1oilPrice1.place(x=Width / 2 - 50, y= 30)
        # -------------------------------------- 전국 경유 막대그래프 ---------------------------------------------
            minprice = (float)(OilData.oilAPI.localPrice['서울']['경유'][0])
            minlocal = ''
            for i in OilData.oilAPI.localPrice:
                if (float)(OilData.oilAPI.localPrice[i]['경유'][0]) < minprice:
                    minprice = (float)(OilData.oilAPI.localPrice[i]['경유'][0])
                    minlocal = i

            # self.seoul = tk.Label(self.Chart, text=OilData.oilAPI.localPrice['서울']['경유'][0],font=self.mfont)
            # self.seoul.place(x=120, y= 50)

            count = 0
            for i in OilData.oilAPI.localPrice:
                if i == minlocal:
                    color = 'tomato'
                else:
                    color = 'pale green'
                self.Chart.create_rectangle(110 + 30 * count, ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['경유'][0]) - minprice) - 100, 130 + 30 * count, ChartHeight - 20, fill = color, tags='Chart')        
                tk.Label(self.Chart, text=i, font=self.mfont, bg=self.skycolor).place(x=105 + 30 * count, y= ChartHeight-20)
                tk.Label(self.Chart, text=OilData.oilAPI.localPrice[i]['경유'][0], font=self.chartfont, bg=self.skycolor).place(x=105 + 30 * count, y= ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['경유'][0]) - minprice) - 120)
                count += 1
        # -------------------------------------- 전국 경유 막대그래프 ---------------------------------------------
        elif kind == 'gasoline':
            self.n1oilName1 = tk.Label(self.Chart, text="휘발유",font=self.mfont, bg=self.skycolor)
            self.n1oilName1.place(x=Width / 2 - 30, y= 0)
            self.n1oilPrice1 = tk.Label(self.Chart, text=str(OilData.oilAPI.todayOil["휘발유"][0]+ " / " + OilData.oilAPI.todayOil["휘발유"][1] ),font=self.mfont, bg=self.skycolor)
            self.n1oilPrice1.place(x=Width / 2 - 50, y= 30)
        # -------------------------------------- 전국 휘발유 막대그래프 ---------------------------------------------
            minprice = (float)(OilData.oilAPI.localPrice['서울']['휘발유'][0])
            minlocal = ''
            for i in OilData.oilAPI.localPrice:
                if (float)(OilData.oilAPI.localPrice[i]['휘발유'][0]) < minprice:
                    minprice = (float)(OilData.oilAPI.localPrice[i]['휘발유'][0])
                    minlocal = i

            count = 0
            for i in OilData.oilAPI.localPrice:
                if i == minlocal:
                    color = 'tomato'
                else:
                    color = 'pale green'
                self.Chart.create_rectangle(110 + 30 * count, ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['휘발유'][0]) - minprice) - 100, 130 + 30 * count, ChartHeight - 20, fill = color, tags='Chart')        
                tk.Label(self.Chart, text=i, font=self.mfont, bg=self.skycolor).place(x=105 + 30 * count, y= ChartHeight-20)  # , tags='Chart'
                tk.Label(self.Chart, text=OilData.oilAPI.localPrice[i]['휘발유'][0], font=self.chartfont, bg=self.skycolor).place(x=105 + 30 * count, y= ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['휘발유'][0]) - minprice) - 120)
                count += 1
        # -------------------------------------- 전국 휘발유 막대그래프 ---------------------------------------------
        elif kind == "premiumgasoline":
            self.n1oilName1 = tk.Label(self.Chart, text="고급 휘발유",font=self.mfont, bg=self.skycolor)
            self.n1oilName1.place(x=Width / 2 - 40, y= 0)
            self.n1oilPrice1 = tk.Label(self.Chart, text=str(OilData.oilAPI.todayOil["고급휘발유"][0]+ " / " + OilData.oilAPI.todayOil["고급휘발유"][1] ),font=self.mfont, bg=self.skycolor)
            self.n1oilPrice1.place(x=Width / 2 - 50, y= 30)
        # -------------------------------------- 전국 고급 휘발유 막대그래프 ---------------------------------------------
            minprice = (float)(OilData.oilAPI.localPrice['서울']['고급 휘발유'][0])
            minlocal = ''
            for i in OilData.oilAPI.localPrice:
                if (float)(OilData.oilAPI.localPrice[i]['고급 휘발유'][0]) < minprice:
                    minprice = (float)(OilData.oilAPI.localPrice[i]['고급 휘발유'][0])
                    minlocal = i
                    
            count = 0
            for i in OilData.oilAPI.localPrice:
                if i == minlocal:
                    color = 'tomato'
                else:
                    color = 'pale green'
                self.Chart.create_rectangle(110 + 30 * count, ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['고급 휘발유'][0]) - minprice) - 100, 130 + 30 * count, ChartHeight - 20, fill = color, tags='Chart')        
                tk.Label(self.Chart, text=i, font=self.mfont, bg=self.skycolor).place(x=105 + 30 * count, y= ChartHeight-20)  # , tags='Chart'
                tk.Label(self.Chart, text=OilData.oilAPI.localPrice[i]['고급 휘발유'][0], font=self.chartfont, bg=self.skycolor).place(x=105 + 30 * count, y= ChartHeight - ((float)(OilData.oilAPI.localPrice[i]['고급 휘발유'][0]) - minprice) - 120)
                count += 1
        # -------------------------------------- 전국 고급 휘발유 막대그래프 ---------------------------------------------      
        self.Chart.create_rectangle(50, ChartHeight - 40, ChartWidth - 50, ChartHeight - 20, fill = 'black', tags='Chart')  


    def DrawLocalChart(self):
        self.Chart = tk.Canvas(self.frame2, width=ChartWidth, height=Chart2Height, bg=self.skycolor)
        self.Chart.place(y=50)

        self.n1oilName1 = tk.Label(self.Chart, text=self.selected_oil.get(),font=self.mfont, bg=self.skycolor)
        self.n1oilName1.place(x=Width / 2 - 25, y= 0)
        # -------------------------------------- 지역 막대그래프 ---------------------------------------------
        minprice = (float)(OilData.oilAPI.gasStationList[0].price)
        minlocal = 0
        for i in range(10):
            if (float)(OilData.oilAPI.gasStationList[i].price) < minprice:
                minprice = (float)(OilData.oilAPI.gasStationList[i].price)
                minlocal = i

        count = 0

        colorlst = ['gold', 'ghost white', 'DarkGoldenrod4', 'gray40']

        for i in range(10):
            if 0 <= i <= 2:
                color = colorlst[i]
            else:
                color = colorlst[3]
            self.Chart.create_rectangle(110 + 50 * count, Chart2Height - ((float)(OilData.oilAPI.gasStationList[i].price) - minprice) *1.5 - 100, 130 + 50 * count, Chart2Height - 20, fill = color, tags='Chart')        
            tk.Label(self.Chart, text=(str)(i + 1) + "등", font=self.mfont, bg=self.skycolor).place(x=105 + 50 * count, y= Chart2Height-20)
            tk.Label(self.Chart, text=OilData.oilAPI.gasStationList[i].price, font=self.chart2font, bg=self.skycolor).place(x=105 + 50 * count, y= Chart2Height - ((float)(OilData.oilAPI.gasStationList[i].price) - minprice) * 1.5 - 120)
            count += 1
        self.Chart.create_rectangle(50, Chart2Height - 40, ChartWidth - 50, Chart2Height - 20, fill = 'black', tags='Chart')
        # -------------------------------------- 지역 막대그래프 ---------------------------------------------

        # 최저가 주유소 정보 라벨    - 고인호
        namestation = tk.Label(self.frame2, text=OilData.oilAPI.gasStationList[0].name, font=self.mfont, bg=self.groundcolor, fg='white').place(x=Width / 2 , y= Height - 70)
        placestation = tk.Label(self.frame2, text=OilData.oilAPI.gasStationList[0].roadName, font=self.mfont, bg=self.groundcolor, fg='white').place(x=Width / 2 , y= Height - 50)
    

    def select_si(self):
        print(self.selected_si.get())
        self.gu_options = set([i for i in OilData.oilAPI.GuCodeList[OilData.oilAPI.localCodeList[self.selected_si.get()]]])
        self.gu_options = tkinter.ttk.Combobox(self.frame2, textvariable=self.selected_gu, values=list(self.gu_options))
        self.gu_options.place(x = 50, y =Height - 125)

    def search(self):
        # OilData.oilAPI.SetLocalCode(OilData.oilAPI.localCodeList[self.selected_si.get()])
        OilData.oilAPI.SetLocalCode(OilData.oilAPI.GuCodeList[OilData.oilAPI.localCodeList[self.selected_si.get()]][self.selected_gu.get()])
        OilData.oilAPI.SetOilName(self.selected_oil.get())
        OilData.oilAPI.FindCheapOilStation()
        global photo1
        photo1 = ImageTk.PhotoImage(MapData.map.SetIdx(0))   #지도이미지
        self.mapLabel.config(image=photo1)
        self.mapLabel['image'] = photo1
        self.mapLabel.place(x=Width // 2, y=Height -MapHeight - 100)
        self.DrawLocalChart()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("기름값 도우미")
        self.font = tkinter.font.Font(family="문체부 제목 바탕체", size=25, weight='bold')
        self.mfont = tkinter.font.Font(family="Arial", size=10)
        self.chartfont = tkinter.font.Font(family="Arial", size=6)
        self.chart2font = tkinter.font.Font(family="Arial", size=8)
        self.favoriteList = []
        self.selectedOilStation = None

        self.skycolor = '#d4f8ff'
        self.groundcolor = '#292929'

        #이미지 생성 - 서종배
        SearchImage = tk.PhotoImage(file='./image/SearchButton.png')
        PGimage = tk.PhotoImage(file='./image/PreGasoline.png')
        DSimage = tk.PhotoImage(file='./image/Diesel.png')
        GSimage = tk.PhotoImage(file='./image/Gasoline.png')
        bgImage= tk.PhotoImage(file="./image/GasManagerBG.png")


        # 오늘 기름 가격 그래프 표시 테스트 - 서종배
        self.notebook = tkinter.ttk.Notebook(self.window, width=Width, height=Height)
        self.frame1 = tk.Frame(self.window)
        self.notebook.add(self.frame1, text="ONE")
        self.notebook.pack()

        #배경추가
        self.bg1 = tk.Label(self.frame1, image=bgImage)
        self.bg1.pack()


        # 기름 선택 버튼    - 고인호
        self.disselbutton = tk.Button(self.frame1, text='경유', command=lambda row="dissel": self.DrawChart(row), image=DSimage,borderwidth=0 )
        self.disselbutton.place(x=Width/2 - 150, y=50)

        self.gasolinebutton = tk.Button(self.frame1, text='휘발유', command=lambda row="gasoline": self.DrawChart(row), image=GSimage,borderwidth=0)
        self.gasolinebutton.place(x=Width/2 - 50, y = 50)

        self.premiumgasolinebutton = tk.Button(self.frame1, text='고급 휘발유', command=lambda row="premiumgasoline": self.DrawChart(row), image=PGimage,borderwidth=0)
        self.premiumgasolinebutton.place(x=Width/2 + 50, y = 50)

        # Title
        self.n1Title = tk.Label(self.frame1, text="오늘의 기름값", font=self.font, bg=self.skycolor)
        self.n1Title.place(x=Width / 2 - 110, y= 0)

        # 지도 나오는 프레임
        self.frame2 = tk.Frame(self.window)
        self.notebook.add(self.frame2, text="TWO")
        self.notebook.pack()

        self.bg2 = tk.Label(self.frame2, image=bgImage)
        self.bg2.pack()

        # 상단에 글씨    - 고인호
        MainName = tk.Label(self.frame2, text='지역 주유소 최저가 검색', font=self.font, bg=self.skycolor)
        MainName.place(x=Width/4, y=0)

        # 지도를 그리는 캔버스    - 고인호
        photo = ImageTk.PhotoImage(MapData.map.GetImage())   #지도이미지
        self.mapLabel = tk.Label(self.frame2, image=photo, width=MapWidth, height=MapHeight)
        self.mapLabel.place(x=Width//2, y=Height -MapHeight - 100)

        # 지역 선택하는 콤보박스    - 고인호
        self.selected_si = tk.StringVar()
        self.selected_si.set("서울")  # 초기값 설정
        self.si_options = set([i for i in OilData.oilAPI.localCodeList])
        self.si_combo = tkinter.ttk.Combobox(self.frame2, textvariable=self.selected_si, values=list(self.si_options))
        self.si_combo.place(x = 50, y =Height - 100)

        self.selected_gu = tk.StringVar()
        self.selected_gu.set("")  # 초기값 설정
        self.gu_options = set([i for i in OilData.oilAPI.GuCodeList[OilData.oilAPI.localCodeList[self.selected_si.get()]]])
        self.gu_options = tkinter.ttk.Combobox(self.frame2, textvariable=self.selected_gu, values=list(self.gu_options), postcommand=self.select_si)
        self.gu_options.place(x = 50, y =Height - 125)

        # 기름 종류 선택    - 고인호
        self.oilkind = ["경유", "휘발유", "고급휘발유"]

        self.selected_oil = tk.StringVar()
        self.selected_oil.set("경유")  # 초기값 설정
        self.oil_options = set([i for i in self.oilkind])
        self.oil_combo = tkinter.ttk.Combobox(self.frame2, textvariable=self.selected_oil, values=list(self.oil_options))
        self.oil_combo.place(x = 50, y =Height - 200)
        # 체크 박스
        # tk.Checkbutton(self.frame2, text='경유', command=self.up,image=DSimage).place(x=50, y=300)
        # tk.Checkbutton(self.frame2, text='휘발유', command=self.up, image=GSimage).place(x=50, y=350)
        # tk.Checkbutton(self.frame2, text='고급 휘발유', command=self.up, image=PGimage).place(x=50, y=400)
        # 버튼
        tk.Button(self.frame2, text="검색", command=self.search, image=SearchImage, borderwidth=0, bg=self.groundcolor).place(x=50,y=Height - 70)

        self.window.mainloop()


Program()        