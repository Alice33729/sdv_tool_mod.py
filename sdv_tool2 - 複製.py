import tkinter as tk
from tkinter import ttk, messagebox

#資料
class Crop:
    def __init__(self, name, season, buy, sell, year, text):
        self.name = name
        self.season = season
        self.buy = buy
        self.sell = sell
        self.year = year
        self.text = text
    #def Tiller(self,sell_s):
        #self.sell + self.sell*10% = sell_s


Blue_Jazz = Crop("Blue Jazz", "Spring", 30, 50, 1, "Flower")
Carrot = Crop("Carrot", "Spring", 0, 35, 1, "Can find by digging up Seed Spots.")
Garlic = Crop("Garlic", "Spring", 40, 60, 2, "Available from year 2 in Pierre's.")
Blueberry = Crop("Blueberry", "Summer", 80, 50, 1, "Keeps producing after maturity.")
Amaranth = Crop("Amaranth", "Fall", 70, 150, 1, "Harvested by using a Scythe.")
Powdermelon = Crop("Powdermelon", "Winter", 0, 60, 1, "Can find by digging up Seed Spots.")


def Show_Info(*args):
    reset()
    # 因為不用frame了，也就不用.grid()了
    # 因為有很多還沒使用的功能還留著這個寫法，所以請自行清除這部分。
    # info_Frame.grid()
    """Frame_Name.grid(column=0, row=0)
    List_Name.grid(column=0, row=0)
    Frame_Year.grid(column=4, row=0)
    List_Year.grid(column=0, row=0)"""

    # 用列表儲存需要處理的作物資料
    crop_list = []

    """if showSeason.get() == 'showsea_on':
        # print('showsea_on')
        List_Season.grid(column=0, row=0)
        Frame_Season.grid(column=1, row=0)

    if showPierre.get() == 'showpie_on':
        # print('showpie_on')
        List_Pierre.grid(column=0, row=0)
        Frame_Pierre.grid(column=2, row=0)

    if showRegular.get() == 'showreg_on':
        # print('showreg_on')
        List_Regular.grid(column=0, row=0)
        Frame_Regular.grid(column=3, row=0)

    if showText.get() == 'showtex_on':
        # print('showtex_on')
        List_Text.grid(column=0, row=0)
        Frame_Text.grid(column=5, row=0)"""

    if val_season.get() == 'All':
        if year1.get() == 'y1_on':
            # .grid()是功能，所以應該是先定義成label後再.grid()
            # 一般加入的範例如下：
            # tree.insert("", index="end", text=Blue_Jazz.name, values=[Blue_Jazz.year, Blue_Jazz.season, Blue_Jazz.buy, Blue_Jazz.sell,  Blue_Jazz.text])

            # crop_list = [Blue_Jazz, Garlic, Carrot, Blueberry, Amaranth, Powdermelon]
            # 與其定義有哪些，不如一個一個加進列表裡。
            crop_list.append(Blue_Jazz)
            crop_list.append(Carrot)
            crop_list.append(Blueberry)
            crop_list.append(Amaranth)
            crop_list.append(Powdermelon)

            """#Blue_Jazz
            Name_Blue_Jazz = tk.Label(Frame_Name, text= Blue_Jazz.name).grid()
            Season_Blue_Jazz = tk.Label(Frame_Season, text= Blue_Jazz.season).grid()
            Pierre_Blue_Jazz = tk.Label(Frame_Pierre, text= Blue_Jazz.buy).grid()
            Regular_Blue_Jazz = tk.Label(Frame_Regular, text= Blue_Jazz.sell).grid()
            Year_Blue_Jazz = tk.Label(Frame_Year, text= Blue_Jazz.year).grid()
            Text_Blue_Jazz = tk.Label(Frame_Text, text= Blue_Jazz.text).grid()
            #Carrot
            Name_Carrot = tk.Label(Frame_Name, text= Carrot.name).grid()
            Season_Carrot = tk.Label(Frame_Season, text= Carrot.season).grid()
            Pierre_Carrot = tk.Label(Frame_Pierre, text= Carrot.buy).grid()
            Regular_Carrot = tk.Label(Frame_Regular, text= Carrot.sell).grid()
            Year_Carrot = tk.Label(Frame_Year, text= Carrot.year).grid()
            Text_Carrot = tk.Label(Frame_Text, text= Carrot.text).grid()
            #Blueberry
            Name_Blueberry = tk.Label(Frame_Name, text= Blueberry.name).grid()
            Season_Blueberry = tk.Label(Frame_Season, text= Blueberry.season).grid()
            Pierre_Blueberry = tk.Label(Frame_Pierre, text= Blueberry.buy).grid()
            Regular_Blueberry = tk.Label(Frame_Regular, text= Blueberry.sell).grid()
            Year_Blueberry = tk.Label(Frame_Year, text= Blueberry.year).grid()
            Text_Blueberry = tk.Label(Frame_Text, text= Blueberry.text).grid()
            #Amaranth
            Season_Amaranth = tk.Label(Frame_Season, text= Amaranth.season).grid()
            Name_Amaranth = tk.Label(Frame_Name, text= Amaranth.name).grid()
            Pierre_Amaranth = tk.Label(Frame_Pierre, text= Amaranth.buy).grid()
            Regular_Amaranth = tk.Label(Frame_Regular, text= Amaranth.sell).grid()
            Year_Amaranth = tk.Label(Frame_Year, text= Amaranth.year).grid()
            Text_Amaranth = tk.Label(Frame_Text, text= Amaranth.text).grid()
            #Powdermelon
            Name_Powdermelon = tk.Label(Frame_Name, text= Powdermelon.name).grid()
            Season_Powdermelon = tk.Label(Frame_Season, text= Powdermelon.season).grid()
            Pierre_Powdermelon = tk.Label(Frame_Pierre, text= Powdermelon.buy).grid()
            Regular_Powdermelon = tk.Label(Frame_Regular, text= Powdermelon.sell).grid()
            Year_Powdermelon = tk.Label(Frame_Year, text= Powdermelon.year).grid()
            Text_Powdermelon = tk.Label(Frame_Text, text= Powdermelon.text).grid()"""
        if year2.get() == 'y2_on':
            crop_list.append(Garlic)

            """#Garlic
            Name_Garlic = tk.Label(Frame_Name, text= Garlic.name).grid()
            Season_Garlic = tk.Label(Frame_Season, text= Garlic.season).grid()
            Pierre_Garlic = tk.Label(Frame_Pierre, text= Garlic.buy).grid()
            Regular_Garlic = tk.Label(Frame_Regular, text= Garlic.sell).grid()
            Year_Garlic = tk.Label(Frame_Year, text= Garlic.year).grid()
            Text_Garlic = tk.Label(Frame_Text, text= Garlic.text).grid()"""

    # 這個好像重複了喔。
    if val_season.get() == 'All':
        pass
    elif val_season.get() == 'Spring':
        if year1.get() == 'y1_on':
            # Blue_Jazz
            Name_Blue_Jazz = tk.Label(Frame_Name, text=Blue_Jazz.name).grid()
            Season_Blue_Jazz = tk.Label(Frame_Season, text=Blue_Jazz.season).grid()
            Pierre_Blue_Jazz = tk.Label(Frame_Pierre, text=Blue_Jazz.buy).grid()
            Regular_Blue_Jazz = tk.Label(Frame_Regular, text=Blue_Jazz.sell).grid()
            Year_Blue_Jazz = tk.Label(Frame_Year, text=Blue_Jazz.year).grid()
            Text_Blue_Jazz = tk.Label(Frame_Text, text=Blue_Jazz.text).grid()
            # Carrot
            Name_Carrot = tk.Label(Frame_Name, text=Carrot.name).grid()
            Season_Carrot = tk.Label(Frame_Season, text=Carrot.season).grid()
            Pierre_Carrot = tk.Label(Frame_Pierre, text=Carrot.buy).grid()
            Regular_Carrot = tk.Label(Frame_Regular, text=Carrot.sell).grid()
            Year_Carrot = tk.Label(Frame_Year, text=Carrot.year).grid()
            Text_Carrot = tk.Label(Frame_Text, text=Carrot.text).grid()
        if year2.get() == 'y2_on':
            # Garlic
            Name_Garlic = tk.Label(Frame_Name, text=Garlic.name).grid()
            Season_Garlic = tk.Label(Frame_Season, text=Garlic.season).grid()
            Pierre_Garlic = tk.Label(Frame_Pierre, text=Garlic.buy).grid()
            Regular_Garlic = tk.Label(Frame_Regular, text=Garlic.sell).grid()
            Year_Garlic = tk.Label(Frame_Year, text=Garlic.year).grid()
            Text_Garlic = tk.Label(Frame_Text, text=Garlic.text).grid()

    elif val_season.get() == 'Summer':
        if year1.get() == 'y1_on':
            # Blueberry
            Name_Blueberry = tk.Label(Frame_Name, text=Blueberry.name).grid()
            Season_Blueberry = tk.Label(Frame_Season, text=Blueberry.season).grid()
            Pierre_Blueberry = tk.Label(Frame_Pierre, text=Blueberry.buy).grid()
            Regular_Blueberry = tk.Label(Frame_Regular, text=Blueberry.sell).grid()
            Year_Blueberry = tk.Label(Frame_Year, text=Blueberry.year).grid()
            Text_Blueberry = tk.Label(Frame_Text, text=Blueberry.text).grid()
        elif year2 == 'y2_on':
            pass

    elif val_season.get() == 'Fall':
        if year1.get() == 'y1_on':
            # Amaranth
            Name_Amaranth = tk.Label(Frame_Name, text=Amaranth.name).grid()
            Season_Amaranth = tk.Label(Frame_Season, text=Amaranth.season).grid()
            Pierre_Amaranth = tk.Label(Frame_Pierre, text=Amaranth.buy).grid()
            Regular_Amaranth = tk.Label(Frame_Regular, text=Amaranth.sell).grid()
            Year_Amaranth = tk.Label(Frame_Year, text=Amaranth.year).grid()
            Text_Amaranth = tk.Label(Frame_Text, text=Amaranth.text).grid()
        if year2.get() == 'y2_on':
            pass

    if val_season.get() == 'Winter':
        if year1.get() == 'y1_on':
            # Powdermelon
            Name_Powdermelon = tk.Label(Frame_Name, text=Powdermelon.name).grid()
            Season_Powdermelon = tk.Label(Frame_Season, text=Powdermelon.season).grid()
            Pierre_Powdermelon = tk.Label(Frame_Pierre, text=Powdermelon.buy).grid()
            Regular_Powdermelon = tk.Label(Frame_Regular, text=Powdermelon.sell).grid()
            Year_Powdermelon = tk.Label(Frame_Year, text=Powdermelon.year).grid()
            Text_Powdermelon = tk.Label(Frame_Text, text=Powdermelon.text).grid()
        if year2.get() == 'y2_on':
            pass

    # 陳列的列數以列表儲存
    # 因為年和名字一樣常駐，因此移到最前面。
    # 看起來columns叫什麼名字只是程式內的事，因為顯示的名字還是取決於heading。
    # year常駐，所以預設在列表裡。
    columns = ["year"]
    # 各列的名字也以列表儲存，作物名稱和年份是預設的。
    title_name = ["Name", "Year"]
    # 依照選擇的數值決定要顯示幾個列，還有它們的標題名字。
    if showSeason.get() == "showsea_on":
        columns.append("season")
        title_name.append("Season")
    if showPierre.get() == "showpie_on":
        columns.append("buy")
        title_name.append("Buy")
    if showRegular.get() == "showreg_on":
        columns.append("sell")
        title_name.append("Sell")
    if showText.get() == "showtex_on":
        columns.append("season")
        title_name.append("text")
    # treeview的columns直接以列表決定
    crop_tree["columns"] = columns

    # 以列表長度決定要加幾次，並把標題加上去。
    # 但是因為第一列總是會存在，所以標題數量會比列多一個。
    for i in range(len(title_name)):
        crop_tree.heading(f"#{i}", text=title_name[i])
    # tree.heading("#0", text="第一列的標題")
    # tree.heading("#1", text="第二列的標題")
    # tree.heading("#2", text="第三列的標題")
    # tree.heading("#3", text="第四列的標題")

    #crop_list裡面儲存要處理的作物（Class），因此後面可以指定item的.name等值。
    for item in crop_list:
        # 第一，決定有哪些值要顯示，因此這些值用一個列表儲存。
        # 以勾選的格子決定要加入哪些數值
        value = [item.year]
        if showSeason.get() == "showsea_on":
            value.append(item.season)
        if showPierre.get() == "showpie_on":
            value.append(item.buy)
        if showRegular.get() == "showreg_on":
            value.append(item.sell)
        if showText.get() == "showtex_on":
            value.append(item.text)
        # 再來，values直接沿用已經儲存資料的列表。text是第一列，因此是作物名。
        crop_tree.insert("", index="end", text=item.name, values=value)

    # 顯示treeview
    crop_tree.grid(column=0, row=6)


# 有個想法是這樣的，與其特別設計一個重置按鈕，不如讓這個功能在每次搜尋時啟動。所以現在是reset在Show_Info()裡了。
def reset():
    # 這種取變數的做法只適用於class，除非從函式return變數，不然就必須要在函式外宣告變數並且從那裡取得。
    """
    Show_Info.Info_Frame.grid_forget()
    Show_Info.Info_Frame.grid_forget()
    Show_Info.Frame_Name.grid_forget()
    Show_Info.Frame_Season.grid_forget()
    Show_Info.Frame_Pierre.grid_forget()
    Show_Info.Frame_Regular.grid_forget()
    Show_Info.Frame_Year.grid_forget()
    Show_Info.Frame_Text.grid_forget()
    """
    # 上面的東西正確的寫法如下：
    """
    Info_Frame.grid_forget()
    Info_Frame.grid_forget()
    Frame_Name.grid_forget()
    Frame_Season.grid_forget()
    Frame_Pierre.grid_forget()
    Frame_Regular.grid_forget()
    Frame_Year.grid_forget()
    Frame_Text.grid_forget()
    """
    # 隱藏treeview
    crop_tree.grid_forget()
    # 聽說這樣可以清除treeview
    crop_tree.delete(*crop_tree.get_children())
    # Show_Info()

#程式本體
sdv = tk.Tk()
sdv.title('StardewValley Crop Tool ver.0.0[alpha]')        # 標題
sdv.geometry('1200x400')  #視窗大小(寬x高)
sdv.resizable(True, True)  #是否可以縮放(上下, 左右)

Option_Frame = tk.Frame(sdv)
Option_Frame.grid(sticky=tk.W)

#選取季節
val_season = tk.StringVar() # 建立文字變數
Season_title = tk.Label(Option_Frame, text='Season:')
Season_title.grid(column=0, row=0)

Season_All = tk.Radiobutton(Option_Frame, text='All',variable=val_season, value='All', )
Season_All.grid(column=1, row=0)
Season_All.select()  # 選取按鈕

Season_Spring = tk.Radiobutton(Option_Frame, text='Spring',variable=val_season, value='Spring', )
Season_Spring.grid(column=2, row=0)

Season_Summer = tk.Radiobutton(Option_Frame, text='Summer',variable=val_season, value='Summer', )
Season_Summer.grid(column=3, row=0)

Season_Fall = tk.Radiobutton(Option_Frame, text='Fall',variable=val_season, value='Fall', )
Season_Fall.grid(column=4, row=0)

Season_Winter = tk.Radiobutton(Option_Frame, text='Winter',variable=val_season, value='Winter', )
Season_Winter.grid(column=5, row=0)

#年份
Year_title = tk.Label(Option_Frame, text='Year:')
Year_title.grid(column=0, row=1)
#第一年
year1 = tk.StringVar()   # 設定文字變數，並綁定第一個 Checkbutton
Year_1 = tk.Checkbutton(Option_Frame, text='1',
                            variable=year1, onvalue='y1_on', offvalue='y1_off', )
Year_1.grid(column=1, row=1)
Year_1.select()   # 開始時勾選
#第二年以上
year2 = tk.StringVar()   # 設定文字變數，並綁定第二個 Checkbutton
Year_2 = tk.Checkbutton(Option_Frame, text='2+',
                            variable=year2, onvalue='y2_on', offvalue='y2_off', )
Year_2.grid(column=2, row=1)
Year_2.deselect()   # 開始時不要勾選

#技能加成
Skill_title = tk.Label(Option_Frame, text='Skill:')
Skill_title.grid(column=0, row=2)

skillTiller = tk.StringVar()   
Skill_Tiller = tk.Checkbutton(Option_Frame, text='Tiller',
                            variable=skillTiller, onvalue='till_on', offvalue='till_off', )
Skill_Tiller.grid(column=1, row=2)
Skill_Tiller.deselect()   # 開始時不要勾選

#顯示
Show_title = tk.Label(Option_Frame, text='Show:')
Show_title.grid(column=0, row=3)

# 其實可以設定成BoolVar，值就是True或False，這樣寫if式時可以直接判定這個值是t還是f
#季節
showSeason = tk.StringVar()   
Show_Season = tk.Checkbutton(Option_Frame, text='Season',
                            variable=showSeason, onvalue='showsea_on', offvalue='showsea_off', )
Show_Season.grid(column=1, row=3)
Show_Season.select()   # 開始時勾選
#買入價格
showPierre = tk.StringVar()   
Show_Pierre = tk.Checkbutton(Option_Frame, text="Pierre's",
                            variable=showPierre, onvalue='showpie_on', offvalue='showpie_off', )
Show_Pierre.grid(column=2, row=3)
Show_Pierre.select()   # 開始時勾選
#賣出價格
showRegular = tk.StringVar()   
Show_Regular = tk.Checkbutton(Option_Frame, text="Regular",
                            variable=showRegular, onvalue='showreg_on', offvalue='showreg_off', )
Show_Regular.grid(column=3, row=3)
Show_Regular.select()   # 開始時勾選
#說明
showText = tk.StringVar()   
Show_Text = tk.Checkbutton(Option_Frame, text='Text',
                            variable=showText, onvalue='showtex_on', offvalue='showtex_off', )
Show_Text.grid(column=4, row=3)
Show_Text.select()   # 開始時勾選

# 資訊框架
Info_Frame = ttk.Frame(sdv)
# Info_Frame.grid(column=0, row=5)

# 所有東西的Label
Frame_Name = ttk.LabelFrame(Info_Frame, text='Name')
Frame_Name.grid(column=0, row=0)
Frame_Season = ttk.LabelFrame(Info_Frame, text='Season')
Frame_Pierre = ttk.LabelFrame(Info_Frame, text="Pierre's")
Frame_Regular = ttk.LabelFrame(Info_Frame, text='Regular')
Frame_Year = ttk.LabelFrame(Info_Frame, text='Year')
Frame_Text = ttk.LabelFrame(Info_Frame, text='Text')
List_Name = ttk.Label(Frame_Name,)
List_Year = ttk.Label(Frame_Year,)
List_Season = ttk.Label(Frame_Season,)
List_Pierre = ttk.Label(Frame_Pierre,)
List_Regular = ttk.Label(Frame_Regular,)
List_Text = ttk.Label(Frame_Text,)

# treeview 啟動方法。columns參數後面才決定。
# 注意這是ttk版本。
crop_tree = ttk.Treeview(sdv)

# 按鈕
Show_Button = tk.Button(Option_Frame, text='search', command=Show_Info)
Show_Button.grid(column=0, row=4)

test_Button = tk.Button(Option_Frame, text='Clear', command=reset)
test_Button.grid(column=1, row=4)

sdv.mainloop()
