import tkinter
import tkinter.ttk
import tkinter.messagebox

testData = {'01':'学校一', '02':'学校二',
            '03':'学校三', '0101':'学校一年级一',
            '010101':'学校一年级一班级一', '0102':'学校一年级二'}

# 按单位编码进行排序
data = sorted(testData.items(), key=lambda x: x[0])

# 编码越长，表示单位名称越小，嵌套关系越深
# 编码长的单位名称前面加的空格也多
data = [(len(item[0])-2)*2*' '+item[1] for item in data]

root = tkinter.Tk()
root.title('NestedRelation_Combobox')
root['height'] = 200
root['width'] = 320

comboSchool = tkinter.ttk.Combobox(root, values = data, width=160)
comboSchool.place(x=10, y=10, width=160, height=20)

# 组合框单击事件
def oncomboSelected(event):
    selectedItem = comboSchool.get()
    if selectedItem:
        tkinter.messagebox.showinfo('报告',
                                    '你选择了\n\n'+selectedItem.strip())
    else:
        tkinter.messagebox.showerror('警告', '你没有选择任何项')
comboSchool.bind('<<ComboboxSelected>>', oncomboSelected)

root.mainloop()
