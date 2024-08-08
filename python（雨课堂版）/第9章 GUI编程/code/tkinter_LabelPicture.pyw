import os
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk

# 创建tkinter应用程序窗口
root = tkinter.Tk()
# 设置窗口大小和位置
root.geometry('430x650+40+30')
# 不允许改变窗口大小
root.resizable(False, False)
# 设置窗口标题
root.title('使用Label显示图片')

# 获取当前文件夹中所有图片文件列表
suffix = ('.jpg', '.bmp', '.png')
pics = [p for p in os.listdir('.') if p.endswith(suffix)]

current = -1
def changePic(flag):
    '''flag=-1表示上一个，flag=1表示下一个'''
    global current
    new = current + flag
    
    if new < 0:
        tkinter.messagebox.showerror('', '这已经是第一张图片了')
    elif new >= len(pics):
        tkinter.messagebox.showerror('', '这已经是最后一张图片了')
    else:
        # 获取要切换的图片文件名
        pic = pics[new]
        
        # 创建Image对象并进行缩放
        im = Image.open(pic)
        w, h = im.size
        
        # 这里假设用来显示图片的Label组件尺寸为400*600
        if w > 400:
            h = int(h*400/w)
            w = 400
        if h > 600:
            w = int(w*600/h)
            h = 600
            
        im = im.resize((w,h))
        
        # 创建PhotoImage对象，并设置Label组件图片
        im1 = ImageTk.PhotoImage(im)
        lbPic['image'] = im1
        lbPic.image = im1
        
        current = new

# “上一张”按钮
def btnPreClick():
    changePic(-1)
btnPre = tkinter.Button(root, text='上一张', command=btnPreClick)
btnPre.place(x=100, y=20, width=80, height=30)

# “下一张”按钮
def btnNextClick():
    changePic(1)
btnNext = tkinter.Button(root, text='下一张', command=btnNextClick)
btnNext.place(x=230, y=20, width=80, height=30)

# 用来显示图片的Label组件
lbPic = tkinter.Label(root, text='test', width=400, height=600)
changePic(1)
lbPic.place(x=10, y=50, width=400, height=600)

# 启动消息主循环
root.mainloop()
