import tkinter
import os
from tkinter import filedialog


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
        label.grid(row=0, column=0)

        # 입력박스
        self.entry=tkinter.Entry(self.window)
        self.entry.grid(row=1, column=0)
        
        
        # 버튼

        button = tkinter.Button(self.window, overrelief="solid", width=15, command=self.onClick, repeatdelay=1000, repeatinterval=100, text="Button")
        button.grid(row=1, column=1)

        listbox = tkinter.Listbox(self.window, selectmode='extended', height=0)
        listbox.insert(0, "1번")
        listbox.insert(1, "2번")
        listbox.insert(2, "2번")
        listbox.insert(3, "2번")
        listbox.insert(4, "3번")
        listbox.grid(row=2, column=0)


        menubar=tkinter.Menu(self.window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        menu_1.add_command(label="하위 메뉴 1-1", command=self.onClick)
        menu_1.add_command(label="하위 메뉴 1-2", command=self.onClick)
        menu_1.add_separator()
        menu_1.add_command(label="하위 메뉴 1-3")
        menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

        self.window.config(menu=menubar)

        # 윈도우가 종료될 때 까지 실행
        self.window.mainloop()
    
    def onClick(self):
        print("on click")
        dir = filedialog.askdirectory(initialdir="/", title="select directory")
        print(dir)
        #pathString = os.path.basename(dir)
        self.entry.delete(0, len(dir))
        self.entry.insert(0, dir)
        return dir

if __name__ == '__main__':
    Example = Gui()
