import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import sqlite3
import datetime

class Common:
    '''通用功能类'''
    # 存放所有选项的复选框组件
    lstNames = []
    
    @staticmethod
    def doSql(sql):
        '''用来执行SQL语句，尤其是INSERT和DELETE语句'''    
        with sqlite3.connect('dataVote.db') as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

    @staticmethod
    def getData(sql):
        '''根据指定的SELECT语句获取并返回数据'''
        with sqlite3.connect('dataVote.db') as conn:
            cur = conn.cursor()
            cur.execute(sql)
            temp = cur.fetchall()
        return temp
    
    @staticmethod
    def show():
        '''从数据库中读取并显示投票选项'''
        # 删除原有的复选框，同时清空选项复选框组件列表
        for check in Common.lstNames:
            check.destroy()
        Common.lstNames = []
        
        # 获取被投票的人名，动态创建复选框
        index1 = 0
        names = Common.getData('SELECT * FROM names')
        for index, line in enumerate(names):
            index1 = index
            # 动态创建变量和复选框，并将二者绑定
            exec('Common.name'+str(index)+'=tkinter.IntVar(root, value=0)')
            exec('checkName'+str(index)\
                 +'=tkinter.Checkbutton(root,variable=Common.name'+str(index)\
                 +',onvalue=1, offvalue=0, width=120)')
            eval('checkName'+str(index))['text'] = line[0]
            # 复选框左对齐
            eval('checkName'+str(index))['anchor'] = 'w'
            eval('checkName'+str(index)).place(x=180,
                                               y=index*30+10,
                                               width=120,
                                               height=20)
            Common.lstNames.append(eval('checkName'+str(index)))

        # 跟据情况动态调整窗口高度
        root.geometry('400x'+str((index1+1)*30+70)+'+400+300')
        return index1

    @staticmethod
    def createTable():
        '''根据需要创建数据表结构'''
        sql = 'SELECT COUNT(*) FROM sqlite_master WHERE name="names"'
        if Common.getData(sql)[0][0] == 0:
            sql = 'CREATE TABLE names(name TEXT)'
            Common.doSql(sql)

        sql = 'SELECT COUNT(*) FROM sqlite_master WHERE name="votes"'
        if Common.getData(sql)[0][0] == 0:
            sql = 'CREATE TABLE votes(name TEXT, voter TEXT, shijian TEXT)'
            Common.doSql(sql)

# 首先创建必要的数据表结构
Common.createTable()

#创建tkinter应用程序
root = tkinter.Tk()

# 窗口标题
root.title('投票小程序_董付国')

# 窗口初始大小和位置
root.geometry('400x180+400+300')

# 不允许改变窗口大小
root.resizable(False, False)

# 创建投票人信息组件
lbVoter = tkinter.Label(root, text='投票人：')
entryVoter = tkinter.Entry(root)

# 创建添加信息的按钮
def btnAddClick():
    names = tkinter.simpledialog.askstring('请输入选项',
                                           '使用英文逗号分隔',
                                           initialvalue='')
    if names:
        names = names.split(',')
        # 获取数据库中已有的选项
        sqlNames = 'SELECT name FROM names'
        oldNames = Common.getData(sqlNames)
        oldNames = [item[0] for item in oldNames]
        
        for name in names:
            # 已经存在的选项自动忽略
            if name not in oldNames:
                sql = 'INSERT INTO names values("'+name+'")'
                Common.doSql(sql)

    index = Common.show()
    modify(index)
btnAdd = tkinter.Button(root, text='添加选项', command=btnAddClick)

# 创建投票按钮
def btnVoteClick():
    # 目前还存在的问题：新增选项后无法直接投票，必须重启程序，待解决
    # 获取投票人名字
    voter = entryVoter.get().strip()
    if not voter:
        tkinter.messagebox.showerror('出错', '请输入投票人姓名')
        return
    
    # 检查该投票人是否已投票，每人只允许投一次
    sqlVoted = 'SELECT COUNT(*) FROM votes WHERE voter="'+voter+'"'
    count = Common.getData(sqlVoted)[0][0]
    if count != 0:
        tkinter.messagebox.showerror('站住', '不允许重复投票')
        return

    # 假装没有选择任何一项
    selected = False
    # 确认投票
    for index, name in enumerate(Common.lstNames):
        if eval('Common.name'+str(index)).get() == 1:
            sql = 'INSERT INTO votes(voter,name,shijian) values("'\
                  + voter + '","' + name['text']\
                  + '","' + str(datetime.datetime.now())[:19] + '")'
            Common.doSql(sql)
            selected = True
    if selected:
        tkinter.messagebox.showinfo('恭喜', '投票成功')
    else:
        tkinter.messagebox.showerror('逗我玩？',
                                     '必须至少选择一项进行投票')
btnVote = tkinter.Button(root, text='投票', command=btnVoteClick)

# 创建查看投票结果按钮
def btnResultClick():
    sql = 'SELECT name FROM votes'
    result = Common.getData(sql)
    d = dict()
    for item in result:
        d[item[0]] = d.get(item[0], 0) + 1
    result = '\n'.join([str(item) for item in d.items()])
    if result:
        tkinter.messagebox.showinfo('投票结果', result)
    else:
        tkinter.messagebox.showerror('失败', '暂时还没有投票数据')
btnResult = tkinter.Button(root,
                           text='查看结果',
                           command=btnResultClick)

# 创建清空选项按钮
def btnClearClick():
    sql = 'DELETE FROM names'
    Common.doSql(sql)
    index = Common.show()
    modify(index) 
btnClear = tkinter.Button(root,
                          text='清空选项',
                          command=btnClearClick)

# 创建清空投票结果的按钮
def btnClearResultClick():
    sql = 'DELETE FROM votes'
    Common.doSql(sql)
    tkinter.messagebox.showinfo('成功', '投票结果已删除')
btnClearResult = tkinter.Button(root,
                                text='清空投票结果',
                                command=btnClearResultClick)

# 动态计算并调整组件位置
def modify(index):
    lbVoter.place(x=80, y=(index+1)*30+10, width=60, height=20)
    entryVoter.place(x=160, y=(index+1)*30+10, width=80, height=20)
    btnAdd.place(x=10, y=(index+1)*30+40, width=60, height=20)
    btnVote.place(x=150, y=(index+1)*30+40, width=60, height=20)
    btnResult.place(x=220, y=(index+1)*30+40, width=60, height=20)
    btnClear.place(x=80, y=(index+1)*30+40, width=60, height=20)
    btnClearResult.place(x=290, y=(index+1)*30+40, width=90, height=20)

# 显示所有动态选项组件，然后调整静态组件的位置
index = Common.show()
modify(index)

# 启动消息主循环
root.mainloop()
