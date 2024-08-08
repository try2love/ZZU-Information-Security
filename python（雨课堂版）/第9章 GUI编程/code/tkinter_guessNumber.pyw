import random
import tkinter
import tkinter.messagebox
import tkinter.simpledialog

root = tkinter.Tk()
# 窗口标题
root.title('猜数游戏--by董付国')
# 窗口初始大小和位置
root.geometry('280x80+400+300')
# 不允许改变窗口大小
root.resizable(False, False)

# 用户猜的数
varNumber = tkinter.StringVar(root, value='0')

# 允许猜的总次数
totalTimes = tkinter.IntVar(root, value=0)

# 已猜次数
already = tkinter.IntVar(root, value=0)

# 当前生成的随机数
currentNumber = tkinter.IntVar(root, value=0)

# 玩家玩游戏的总次数
times = tkinter.IntVar(root, value=0)

# 玩家猜对的总次数
right = tkinter.IntVar(root, value=0)

lb = tkinter.Label(root, text='请输入一个整数：')
lb.place(x=10, y=10, width=100, height=20)

# 用户猜数并输入的文本框
entryNumber = tkinter.Entry(root,
                            width=140,
                            textvariable=varNumber)
entryNumber.place(x=110, y=10, width=140, height=20)

# 默认禁用，只有开始游戏以后才允许输入
entryNumber['state'] = 'disabled'

# 按钮单击事件处理函数
def buttonClick():
    if button['text']=='Start Game':
        # 每次游戏时允许用户自定义数值范围
        # 玩家必须输入正确的数
        # 最小数值
        while True:
            try:
                start = tkinter.simpledialog.askinteger('允许的最小整数',
                                                        '最小数（必须大于100）',
                                                        initialvalue=1)
                if start != None:
                    assert start>0
                    break
            except:
                pass

        # 最大数值
        while True:
            try:
                end = tkinter.simpledialog.askinteger('允许的最大整数',
                                                      '最大数（必须大于1000）',
                                                      initialvalue=10)
                if end != None:
                    assert end>10 and end>start
                    break
            except:
                pass
            
        # 在用户自定义的数值范围内生成要猜的随机数
        currentNumber.set(random.randint(start, end))
        
        # 用户自定义一共允许猜几次
        # 玩家必须输入正确的整数
        while True:
            try:
                t = tkinter.simpledialog.askinteger('最多允许猜几次？',
                                                    '总次数（必须大于0）',
                                                    initialvalue=3)
                if t != None:
                    assert t>0
                    totalTimes.set(t)
                    break
            except:
                pass
        # 已猜次数初始化为0
        already.set(0)
        button['text'] = '剩余次数：' + str(t)
        
        # 把文本框初始化为0
        varNumber.set('0')
        
        # 启用文本框，允许用户开始输入整数
        entryNumber['state'] = 'normal'
        
        # 玩游戏的次数加1
        times.set(times.get() + 1)
    else:
        # 一共允许猜几次
        total = totalTimes.get()
        
        # 本次游戏的正确答案
        current = currentNumber.get()
        
        # 玩家本次猜的数
        try:
            x = int(varNumber.get())
        except:
            tkinter.messagebox.showerror('抱歉', '必须输入整数')
            return

        # 猜对了
        if x == current:
            tkinter.messagebox.showinfo('恭喜', '猜对啦')
            button['text'] = 'Start Game'
            
            # 禁用文本框
            entryNumber['state'] = 'disabled'

            # 猜对的次数加1
            right.set(right.get() + 1)
        else:
            # 本次游戏已猜次数加1
            already.set(already.get()+1)
            
            if x > current:
                tkinter.messagebox.showerror('抱歉', '猜的数太大了')
            else:
                tkinter.messagebox.showerror('抱歉', '猜的数太小了')
                
            # 可猜次数用完了
            if already.get() == total:
                tkinter.messagebox.showerror('抱歉',
                                             '游戏结束了，正确的数是：' +
                                             str(currentNumber.get()))
                button['text'] = 'Start Game'
                # 禁用文本框
                entryNumber['state'] = 'disabled'
            else:
                button['text'] = '剩余次数：' + str(total-already.get())
                
# 在窗口上创建按钮，并设置事件处理函数   
button = tkinter.Button(root,
                        text='Start Game',
                        command=buttonClick)
button.place(x=10, y=40, width=250, height=20)

# 关闭程序时提示战绩
def closeWindow():
    message = '共玩游戏 {0} 次，猜对 {1} 次！\n欢迎下次再玩！'
    message = message.format(times.get(), right.get())
    tkinter.messagebox.showinfo('战绩', message)
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)

# 启动消息主循环
root.mainloop()
