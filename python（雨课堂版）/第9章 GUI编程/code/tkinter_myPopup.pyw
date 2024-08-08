import tkinter
from tkinter.commondialog import Dialog

root = tkinter.Tk()
root.title('测试-弹出自定义对话框')
root.geometry('300x100+400+300')
root.resizable(False,False)

class MyPopup:
    def __init__(self, title, message):
        # 弹出式窗口中信息内容的宽度和高度
        # 如果有换行符，则按最长的行来计算宽度
        self.width = len(max(message.split(),key=len))*40
        self.height = message.count('\n')*70
        
        # 创建顶层组件，不允许改变大小，顶层显示
        self.top = tkinter.Toplevel(root)
        self.top.resizable(False,False)
        self.top.attributes('-topmost', 1)
        self.top['bg'] = '#41ba70'

        # 不显示标题栏
        self.top.overrideredirect(True)

        # 显示伪标题，使用Label组件模拟
        # 使用默认字体，一个汉字约占15个像素位置
        self.lbTitle = tkinter.Label(self.top, text=title)
        self.lbTitle['fg'] = 'red'
        self.lbTitle['bg'] = 'yellow'
        self.lbTitle.place(x=5,
                           y=5,
                           width=len(title)*15,
                           height=20)

        # 要显示的消息，使用Label组件模拟，25号字，黑体
        # 约占40个像素的位置
        self.lbMessage = tkinter.Label(self.top,
                                       text=message,
                                       font=("黑体",25,"bold"))
        self.lbMessage['bg'] = 'white'
        self.lbMessage.place(x=30,
                             y=30,
                             width=self.width,
                             height=self.height)

        # 确定按钮，根据message的长度动态估算起始位置
        def onbtnOkClick():
            self.top.destroy()
            return 'Ok'
        self.btnOk = tkinter.Button(self.top,
                                    text='确定',
                                    command=onbtnOkClick)
        self.btnOk.place(x=self.width//2,
                         y=self.height+45,
                         width=60,
                         height=20)

        # 关闭按钮，使用英语字母X模拟
        # 根据message长度动态估算起始位置
        def onbtnCloseClick():
            self.top.destroy()
            return 'Close'
        self.btnClose = tkinter.Button(self.top,
                                       text='X',
                                       command=onbtnCloseClick)
        self.btnClose['bg'] = '#b91140'
        self.btnClose.place(x=self.width+20,
                            y=5,
                            width=30,
                            height=20)
        g = str(self.width+60)+'x'+str(self.height+80)+'+500+300'
        self.top.geometry(g)

        # 鼠标左键按下，允许拖动弹出式窗口位置
        self.X = 0
        self.Y = 0
        self.canMove = False
        def onLeftButtonDown(event):
            self.X = event.x
            self.Y = event.y
            self.canMove = True
        self.top.bind('<Button-1>', onLeftButtonDown)

        # 鼠标抬起
        def onLeftButtonUp(event):
            self.canMove = False
        self.top.bind('<ButtonRelease-1>', onLeftButtonUp)

        # 鼠标移动，改变弹出式窗口位置
        def onLeftButtonMove(event):
            if not self.canMove:
                return
            newX = self.top.winfo_x() + (event.x-self.X)
            newY = self.top.winfo_y() + (event.y-self.Y)
            g = str(self.width+60)+'x'+str(self.height+80)+'+'+str(newX)+'+'+str(newY)
            self.top.geometry(g)
        self.top.bind('<B1-Motion>', onLeftButtonMove)

# 弹出消息对话框的按钮
def onbtnPopupClick():
    btnPopup['state'] = 'disabled'
    w = MyPopup('恭喜', '测试成功\n哈哈嘿嘿呼呼')
    btnPopup.wait_window(w.top)
    
    # 避免弹出式窗口尚未关闭就关闭主窗口时引发错误
    try:
        btnPopup['state'] = 'normal'
    except:
        pass
btnPopup = tkinter.Button(root,
                          text='弹出对话框',
                          command=onbtnPopupClick)
btnPopup.place(x=100, y=40, width=80, height=20)

root.mainloop()
