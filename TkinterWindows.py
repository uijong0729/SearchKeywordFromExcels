import tkinter
import os
from tkinter.constants import X
import GuiConstant as str
from tkinter import filedialog
from functools import partial
import xlrd as xls
import openpyxl as xlsx
from openpyxl import load_workbook
from openpyxl.descriptors.base import String

# 대괄호([])와 소괄호(())안의 공백은 피합니다.
# 쉼표(,), 쌍점(:)과 쌍반점(;) 앞의 공백은 피합니다.
class Gui: 
    def __init__(self):
        # 윈도우 창 생성
        self.window = tkinter.Tk()

        self.window.title("キーワード検索ツール")
        # 너비x높이+x좌표+y좌표
        self.window.geometry("640x400+100+100")
        self.window.resizable(True, True)

        label=tkinter.Label(self.window, text="キーワード検索ツール", width=40, height=3, fg="black", relief="solid")
        label.grid(row=0, column=0, columnspan=4)

        # 입력박스
        self.entry=tkinter.Entry(self.window)
        self.entry.grid(row=1, column=0)
        
        # 버튼
        button = tkinter.Button(self.window, overrelief="solid", width=15, command=partial(self.onClick, "aaa"), repeatdelay=1000, repeatinterval=100, text=str.BUTTON_OEPN)
        button.grid(row=1, column=1)

        # 검색박스 
        self.entryFind=tkinter.Entry(self.window)
        self.entryFind.grid(row=1, column=2)

        # 검색 버튼 
        button = tkinter.Button(self.window, overrelief="solid", width=15, command=partial(self.onFind, "aaa"), repeatdelay=1000, repeatinterval=100, text=str.BUTTON_FIND)
        button.grid(row=1, column=3)

        listbox = tkinter.Listbox(self.window, selectmode='extended', height=0)
        listbox.insert(0, "1번")

        listbox.insert(1, "2번")
        listbox.insert(2, "2번")
        listbox.insert(3, "2번")
        listbox.insert(4, "3번")
        listbox.grid(row=2, column=0)


        # menubar=tkinter.Menu(self.window)
        # menu_1=tkinter.Menu(menubar, tearoff=0)
        # menu_1.add_command(label=str.MENU_EXIT, command=self.ExitApp)
        # menubar.add_cascade(label=str.MENU_BAR, menu=menu_1)
        # self.window.config(menu=menubar)

        # 윈도우가 종료될 때 까지 실행
        self.window.mainloop()
    
    def onClick(self, msg):
        print(msg)
        dir = filedialog.askdirectory(initialdir="/", title="select directory")
        print(dir)
        #pathString = os.path.basename(dir)
        self.entry.delete(0, len(dir))
        self.entry.insert(0, dir)
        return dir
    
    # https://www.delftstack.com/ko/howto/python-tkinter/how-to-get-the-tkinter-label-text/
    def onFind(self, msg):
        # 필요 정보 취득
        path = self.entry.get()
        keyword = self.entryFind.get()
        print(path)
        # print(keyword)

        # 디렉토리내 검색
        list = os.listdir(path)
        for fileOne in list:
            full_filename = (os.path.join(path, fileOne)).replace("/", "\\")
            print(full_filename)
            if "xlsx" in fileOne:
                print("xlsx")
                # https://openpyxl.readthedocs.io/en/stable/
                wb = load_workbook(filename = fileOne)
                #sheet_ranges = wb['range names']
                #print(sheet_ranges['D18'].value)
            elif "xls" in fileOne:
                print("xls")
                book = xls.open_workbook(fileOne)
                # sheetNames = book.sheet_names()
                # if sheetNames.find(keyword) > 0:
                #    print(sheetNames)

                #  iter는 객체의 __iter__ 메서드를 호출해주고, next는 객체의 __next__ 메서드를 호출해줍니다. 
                it = iter(book)
                while (True):
                    sh = next(it, str.READ_FAIL)
                    if sh == str.READ_FAIL:
                        break
                    elif sh.name.find(keyword) > 0:
                        print(sh.name)
                    else:
                        for rx in range(sh.nrows):
                            print(sh.row(rx))

if __name__ == '__main__':
    Example = Gui()