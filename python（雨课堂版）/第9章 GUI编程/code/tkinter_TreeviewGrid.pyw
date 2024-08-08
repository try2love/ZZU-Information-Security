import random
import tkinter
import tkinter.messagebox
from tkinter import Tk, Scrollbar, Frame, RIGHT, Y, LEFT
from tkinter.ttk import Treeview

# 创建tkinter应用程序窗口
root = Tk()
# 设置窗口大小和位置
root.geometry('500x340+400+300')
# 不允许改变窗口大小
root.resizable(False, False)
# 设置窗口标题
root.title('Treeview——Demo')

# 在窗体上创建Frame组件作为容易
frame = Frame(root)
frame.place(x=0, y=10, width=480, height=280)

# 在Frame容器中创建滚动条
scrollBar = Scrollbar(frame)
scrollBar.pack(side=RIGHT, fill=Y)

# 在Frame容器中使用Treeview组件实现表格功能
# Treeview组件，6列，显示表头，带垂直滚动条
tree = Treeview(frame,
                columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6'),
                show="headings",
                yscrollcommand=scrollBar.set)

# 设置每列宽度和对齐方式
tree.column('c1', width=70, anchor='center')
tree.column('c2', width=40, anchor='center')
tree.column('c3', width=40, anchor='center')
tree.column('c4', width=120, anchor='center')
tree.column('c5', width=100, anchor='center')
tree.column('c6', width=90, anchor='center')

# 设置每列表头标题文本
tree.heading('c1', text='姓名')
tree.heading('c2', text='性别')
tree.heading('c3', text='年龄')
tree.heading('c4', text='部门')
tree.heading('c5', text='电话')
tree.heading('c6', text='QQ')

# 左对齐，纵向填充
tree.pack(side=LEFT, fill=Y)

# Treeview组件与垂直滚动条结合
scrollBar.config(command=tree.yview)

# 定义并绑定Treeview组件的鼠标左键双击事件
def treeviewClick(event):
    selectedItem = tree.selection()[0]
    name = tree.item(selectedItem, 'values')[0]
    tkinter.messagebox.showinfo('报告', '你选择的是\n'+name)
tree.bind('<Double-1>', treeviewClick)

# 插入随机数据的按钮
def onbtnInsertClick():
    values = [str(random.randrange(1000)) for _ in range(6)]
    tree.insert('', 0, values=values)
btnInsert = tkinter.Button(root,
                           text='插入随机数据',
                           command=onbtnInsertClick)
btnInsert.place(x=80, y=310, width=120, height=20)

# 删除选中项的按钮
def onbtnDeleteClick():
    if not tree.selection():
        tkinter.messagebox.showerror('抱歉', '你还没有选择，不能删除')
        return
    for item in tree.selection():
        tree.delete(item)
btnDelete = tkinter.Button(root,
                           text='删除选中项',
                           command=onbtnDeleteClick)
btnDelete.place(x=220, y=310, width=120, height=20)

# 插入演示数据
for i in range(20):
    tree.insert('', i, values=[str(i)]*6)
    
# 运行程序，启动事件循环
root.mainloop()
