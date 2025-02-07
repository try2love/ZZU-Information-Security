from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymssql

# 连接数据库
server = '192.168.111.131'
user = 'sa'
userpassword = '111111'
database = 'test学生学籍管理系统'
conn = pymssql.connect(server, user, userpassword, database)
cursor = conn.cursor()


def Main():  # 登录界面
    # 修改密码的函数
    def XGMM():
        rt.destroy()
        rt3 = Tk()
        rt3.title('修改密码')
        rt3.geometry('800x400')

        Label(rt3, text='账户').place(x=100, y=70)
        Label(rt3, text='旧密码：').place(x=100, y=95)
        Label(rt3, text='新密码：').place(x=100, y=120)

        e3 = Entry(rt3, width=30)
        e3.place(x=200, y=70)
        e4 = Entry(rt3, show='*', width=30)
        e4.place(x=200, y=95)
        e5 = Entry(rt3, show='*', width=30)
        e5.place(x=200, y=120)

        def qx3():
            rt3.destroy()
            Main()

        def qr():
            s3 = e3.get()
            s4 = e4.get()
            s5 = e5.get()
            cursor.execute("SELECT * FROM information WHERE NO='%s' AND PASSWORD = '%s' " % (s3, s4))
            T = cursor.fetchone()
            if T is None:
                messagebox.showerror('修改失败', '账户或密码错误！')
            else:
                cursor.execute("UPDATE  information SET PASSWORD='%s' WHERE NO= '%s' " % (s5, s3))
                conn.commit()
                messagebox.showinfo("成功", '密码修改成功!!!')

        Button(rt3, command=qr, text="确认", width=10).place(x=140, y=150)
        Button(rt3, command=qx3, text="退出", width=10).place(x=240, y=150)  # 修改

    rt = Tk()
    rt.title('学生成绩管理系统')
    rt.geometry('605x328+800+200')
    lab1 = Label()
    lab1.place(x=0, y=0)
    Label(text='账户', font=("宋体", '12')).place(x=120, y=90)
    Label(text='密码', font=("宋体", '12')).place(x=120, y=130)
    e1 = Entry(width=30)
    e1.focus()
    e1.place(x=190, y=90)
    e2 = Entry(show='*', width=30)
    e2.place(x=190, y=130)

    def login():
        close = 1

        def student():
            rt.destroy()
            rt2 = Tk()
            c = "您好，学生'%s'" % s1
            rt2.title(c)
            rt2.geometry('800x400+800+200')
            columns = ("学号", "姓名", "学科", "成绩", "学分")
            tree = ttk.Treeview(rt2, height=15, show="headings", columns=columns)  # 隐藏首列
            tree.column("学号", width=100)  # 表示列,不显示
            tree.column("姓名", width=100)
            tree.column("学科", width=100)
            tree.column("成绩", width=100)
            tree.column("学分", width=100)
            tree.place(x=100, y=10)
            tree.heading("学号", text='学号', anchor=CENTER)
            tree.heading("姓名", text='姓名', anchor=CENTER)
            tree.heading("学科", text='学科', anchor=CENTER)
            tree.heading("成绩", text='成绩', anchor=CENTER)
            tree.heading("学分", text='学分', anchor=CENTER)

            def CXCJ():
                # 给树里面添加元素的查询语法
                x = tree.get_children()
                for item in x:
                    tree.delete(item)
                cursor.execute(
                    "select student.sno, sname, cname, grade, credit from student, course, sc where sc.sno=student.sno and sc.cno=course.cno and student.sno='%s'" % (
                            s1 - 100000))
                T = cursor.fetchall()
                for row in T:
                    tree.insert("", 0, values=(row[0], row[1], row[2], row[3], row[4]))

            def qx2():
                rt2.destroy()
                Main()

            Button(rt2, command=qx2, text="退出", width=10).place(x=650, y=300)
            Button(rt2, command=CXCJ, text="查询成绩", width=10).place(x=650, y=200)
            Button(rt2, command=qx2, text="回到首页", width=10).place(x=650, y=150)

        def teacher(close):
            if close == 1:
                rt.destroy()
            rt2 = Tk()
            c = "您好，教师'%s'" % s1
            rt2.title(c)
            rt2.geometry('920x600+600+100')
            cursor.execute(
                "select course.cname from information,course where information.no-300000=course.cno and information.no=%s " % s1)
            T = cursor.fetchone()
            Label(text='学生成绩管理', font=20, fg='red').place(x=350, y=10)
            Label(text='学号：', font=10).place(x=10, y=50)
            Label(text='姓名：', font=10).place(x=310, y=50)
            Label(text="科目： %s" % T, font=10).place(x=10, y=100)
            Label(text='成绩：', font=10).place(x=310, y=100)
            e3 = Entry(width=30)
            e3.focus()
            e3.place(x=90, y=50)
            e4 = Entry(width=30)
            e4.place(x=390, y=50)
            e5 = Entry(width=30)
            e5.place(x=390, y=100)
            listbox1 = Listbox(rt2)
            listbox1.place(width=600, height=400, x=30, y=150)

            def LRCJ():  # 录入成绩

                try:
                    sno = int(e3.get())
                    sname = e4.get()
                    grade = int(e5.get())
                    str333 = "select * from sc,student where sc.sno=student.sno and cno=%s and student.sname='%s' and student.sno=%s " % (
                    s1 - 300000, sname, sno)
                    cursor.execute(str333)
                    T1 = cursor.fetchall()
                except:
                    messagebox.showerror('录入失败', '请查看输入信息是否正确！')
                if T1 == []:
                    messagebox.showerror('录入失败', '请查看输入信息是否正确！')
                else:
                    str1 = "update sc set grade=%s where sno=%s and cno=%s;" % (grade, sno, s1 - 300000)
                    cursor.execute(str1)
                    conn.commit()
                    str2 = '已经录入学号为%s的学生%s的%s科目成绩，分数为%s' % (sno, sname, T, grade)
                    listbox1.insert(listbox1.size(), str2)

            def CXCJ():  # 查询成绩

                def gradetable():
                    columns = ("学号", "姓名", "学科", "成绩", "学分")
                    tree = ttk.Treeview(rt3, height=15, show="headings", columns=columns)  # 隐藏首列
                    tree.column("学号", width=120)  # 表示列,不显示
                    tree.column("姓名", width=120)
                    tree.column("学科", width=120)
                    tree.column("成绩", width=120)
                    tree.column("学分", width=120)
                    tree.place(x=55, y=200)
                    tree.heading("学号", text='学号', anchor=CENTER)
                    tree.heading("姓名", text='姓名', anchor=CENTER)
                    tree.heading("学科", text='学科', anchor=CENTER)
                    tree.heading("成绩", text='成绩', anchor=CENTER)
                    tree.heading("学分", text='学分', anchor=CENTER)
                    str1 = "select student.sno,sname,cname,grade,credit from sc,student,course where sc.cno=course.cno and sc.sno=student.sno and course.cno=%s" % (
                            s1 - 300000)
                    cursor.execute(str1)
                    T = cursor.fetchall()
                    for row in T:
                        tree.insert("", 0, values=(row[0], row[1], row[2], row[3], row[4]))

                def qx2():
                    rt3.destroy()
                    teacher(0)

                def high():
                    columns = ("学号", "姓名", "学科", "成绩", "学分")
                    tree = ttk.Treeview(rt3, height=15, show="headings", columns=columns)  # 隐藏首列
                    tree.column("学号", width=120)  # 表示列,不显示
                    tree.column("姓名", width=120)
                    tree.column("学科", width=120)
                    tree.column("成绩", width=120)
                    tree.column("学分", width=120)
                    tree.place(x=55, y=200)
                    tree.heading("学号", text='学号', anchor=CENTER)
                    tree.heading("姓名", text='姓名', anchor=CENTER)
                    tree.heading("学科", text='学科', anchor=CENTER)
                    tree.heading("成绩", text='成绩', anchor=CENTER)
                    tree.heading("学分", text='学分', anchor=CENTER)
                    str1 = "select student.sno,sname,cname,grade,credit from sc,student,course where sc.cno=course.cno and sc.sno=student.sno and course.cno=%s order by grade asc" % (
                            s1 - 300000)
                    cursor.execute(str1)
                    T = cursor.fetchall()
                    for row in T:
                        tree.insert("", 0, values=(row[0], row[1], row[2], row[3], row[4]))

                def low():
                    columns = ("学号", "姓名", "学科", "成绩", "学分")
                    tree = ttk.Treeview(rt3, height=15, show="headings", columns=columns)  # 隐藏首列
                    tree.column("学号", width=120)  # 表示列,不显示
                    tree.column("姓名", width=120)
                    tree.column("学科", width=120)
                    tree.column("成绩", width=120)
                    tree.column("学分", width=120)
                    tree.place(x=55, y=200)
                    tree.heading("学号", text='学号', anchor=CENTER)
                    tree.heading("姓名", text='姓名', anchor=CENTER)
                    tree.heading("学科", text='学科', anchor=CENTER)
                    tree.heading("成绩", text='成绩', anchor=CENTER)
                    tree.heading("学分", text='学分', anchor=CENTER)
                    str1 = "select student.sno,sname,cname,grade,credit from sc,student,course where sc.cno=course.cno and sc.sno=student.sno and course.cno=%s order by grade desc" % (
                            s1 - 300000)
                    cursor.execute(str1)
                    T = cursor.fetchall()
                    for row in T:
                        tree.insert("", 0, values=(row[0], row[1], row[2], row[3], row[4]))

                def average():
                    columns = ("学科", "平均成绩", "平均学分")
                    tree1 = ttk.Treeview(rt3, height=15, show="headings", columns=columns)  # 隐藏首列
                    tree1.column("学科", width=150)  # 表示列,不显示
                    tree1.column("平均成绩", width=150)
                    tree1.column("平均学分", width=150)
                    # tree.column("及格人数", width=150)
                    tree1.place(x=55, y=200)
                    tree1.heading("学科", text='学科', anchor=CENTER)
                    tree1.heading("平均成绩", text='平均成绩', anchor=CENTER)
                    tree1.heading("平均学分", text='平均学分', anchor=CENTER)
                    # tree.heading("及格人数", text='及格人数', anchor=CENTER)
                    str1 = "select cname, avg(grade), avg(credit) from sc,course where sc.cno=course.cno and sc.cno=%s group by cname" % (
                            s1 - 300000)
                    cursor.execute(str1)
                    T1 = cursor.fetchall()
                    for row in T1:
                        tree1.insert("", 0, values=(row[0], row[1], row[2]))
                    tree2 = ttk.Treeview(rt3, height=15, show="headings", columns='及格人数')  # 隐藏首列
                    tree2.column("及格人数", width=150)  # 表示列,不显示
                    # tree.column("及格人数", width=150)
                    tree2.place(x=505, y=200)
                    tree2.heading("及格人数", text='及格人数', anchor=CENTER)
                    str2 = "select count(*) from sc where sc.cno=%s and sc.grade>=60" % (s1 - 300000)
                    cursor.execute(str2)
                    T2 = cursor.fetchall()
                    for row in T2:
                        tree2.insert("", 0, values=(row[0]))

                rt2.destroy()
                rt3 = Tk()
                rt3.title("查询学生的成绩")
                rt3.geometry('920x600+600+100')
                Button(rt3, text='学生表', command=gradetable).place(x=150, y=40, width=200, height=80)
                Button(rt3, text='退出登录', command=qx2).place(x=500, y=40, width=200, height=80)
                Button(rt3, text='最高成绩', command=high).place(x=700, y=250, width=200, height=80)
                Button(rt3, text='最低成绩', command=low).place(x=700, y=350, width=200, height=80)
                Button(rt3, text='平均成绩及及格人数', command=average).place(x=700, y=450, width=200, height=80)

            def qx():  # 退出至主界面
                rt2.destroy()
                Main()

            btn2 = Button(rt2, text="录入成绩", command=LRCJ)
            btn3 = Button(rt2, text="查询成绩", command=CXCJ)
            btn4 = Button(rt2, text="退出登录", command=qx)
            btn2.place(x=700, y=200, width=200, height=75)
            btn3.place(x=700, y=300, width=200, height=75)
            btn4.place(x=700, y=400, width=200, height=75)

        def Administer(close):
            if close == 1:
                rt.destroy()
            rt2 = Tk()
            c = "您好，管理员'%s'" % s1
            rt2.title(c)
            rt2.geometry('920x300+600+100')

            def addstudent():
                rt2.destroy()
                rt3 = Tk()
                rt3.title("添加学生")
                rt3.geometry('920x540+600+100')
                listbox1 = Listbox(rt3)
                listbox1.place(width=380, height=180, x=510, y=330)

                # 学生信息展示区
                columns = ("学号", "姓名", "年龄")
                tree = ttk.Treeview(rt3, height=15, show="headings", columns=columns)  # 隐藏首列
                tree.column("学号", width=150)  # 表示列,不显示
                tree.column("姓名", width=150)
                tree.column("年龄", width=150)
                tree.place(x=30, y=180)
                tree.heading("学号", text='学号', anchor=CENTER)
                tree.heading("姓名", text='姓名', anchor=CENTER)
                tree.heading("年龄", text='年龄', anchor=CENTER)

                # 输入区
                Label(text='学生管理', font=20, fg='red').place(x=350, y=10)
                Label(text='学号：', font=10).place(x=10, y=50)
                Label(text='姓名：', font=10).place(x=310, y=50)
                Label(text='年龄：', font=10).place(x=10, y=100)
                Label(text='密码：', font=10).place(x=310, y=100)

                e3 = Entry(width=30)
                e3.focus()
                e3.place(x=90, y=50)
                e4 = Entry(width=30)
                e4.place(x=390, y=50)
                e5 = Entry(width=30)
                e5.place(x=90, y=100)
                e6 = Entry(width=30)
                e6.place(x=390, y=100)

                def add():
                    sno = int(float(e3.get()))
                    sname = e4.get()
                    sage = e5.get()
                    password = e6.get()
                    if sno == '' or sname == '' or sage == '' or password == '':
                        messagebox.showerror('添加失败', '请查看输入信息是否完整！')
                    else:
                        try:
                            str1 = "insert into student(sno,sname,sage) values('%s','%s','%s')" % (sno, sname, sage)
                            cursor.execute(str1)
                            conn.commit()
                            str2 = "insert into information(NO,PASSWORD,[identity]) values('%s','%s','student   ')" % (sno + 100000, password)
                            cursor.execute(str2)
                            conn.commit()
                            str3 = "已经添加用户%s,年龄%s，学号%s，登录账户为%s,密码为%s" % (sname, sage, sno, sno + 100000, password)
                            listbox1.insert(listbox1.size(), str3)
                        except:
                            messagebox.showerror('添加失败', '学号发生重复')

                def delete():
                    sno = int(e3.get())
                    if sno == '':
                        messagebox.showerror('添加失败', '请输入必要的学号信息')
                    else:
                        try:
                            str1 = "delete from information where NO=%s" % (sno+100000)
                            cursor.execute(str1)
                            conn.commit()
                            print("1")
                            str2 = "delete from student where sno=%s" % sno
                            cursor.execute(str2)
                            conn.commit()
                            print("2")
                            str3 = "已经删除学号为%s的学生" % sno
                            listbox1.insert(listbox1.size(), str3)
                        except:
                            messagebox.showerror('添加失败', '该学号用户不存在')

                def CX():
                    for child in tree.get_children():
                        tree.delete(child)
                    str1 = "select sno,sname,sage from information, student where student.sno=information.NO-100000 order by sno desc"
                    cursor.execute(str1)
                    T = cursor.fetchall()
                    for row in T:
                        tree.insert("", 0, values=(row[0], row[1], row[2]))

                def qx1():
                    rt3.destroy()
                    Administer(0)

                Button(rt3, text='学生情况表', command=CX).place(x=700, y=30, width=180, height=50)
                Button(rt3, text='添加', command=add).place(x=700, y=100, width=180, height=50)
                Button(rt3, text='删除', command=delete).place(x=700, y=170, width=180, height=50)
                Button(rt3, text='返回', command=qx1).place(x=700, y=240, width=180, height=50)

            def addteacher():
                rt2.destroy()
                rt3 = Tk()
                rt3.title("添加老师")
                rt3.geometry('920x540+600+100')
                listbox1 = Listbox(rt3)
                listbox1.place(width=380, height=180, x=510, y=330)

                # 老师信息展示区
                columns = ("编号", "姓名", "学科", "学分")
                tree = ttk.Treeview(rt3, height=15, show="headings", columns=columns)  # 隐藏首列
                tree.column("编号", width=112)  # 表示列,不显示
                tree.column("姓名", width=112)
                tree.column("学科", width=112)
                tree.column("学分", width=112)
                tree.place(x=30, y=180)
                tree.heading("编号", text='编号', anchor=CENTER)
                tree.heading("姓名", text='姓名', anchor=CENTER)
                tree.heading("学科", text='学科', anchor=CENTER)
                tree.heading("学分", text='学分', anchor=CENTER)

                # 输入区
                Label(text='教师管理', font=20, fg='red').place(x=350, y=10)
                Label(text='编号：', font=10).place(x=10, y=50)
                Label(text='姓名：', font=10).place(x=310, y=50)
                Label(text='学科：', font=10).place(x=10, y=100)
                Label(text='密码：', font=10).place(x=310, y=100)
                Label(text='学分：', font=10).place(x=510, y=160)

                e3 = Entry(width=30)
                e3.focus()
                e3.place(x=90, y=50)
                e4 = Entry(width=30)
                e4.place(x=390, y=50)
                e5 = Entry(width=30)
                e5.place(x=90, y=100)
                e6 = Entry(width=30)
                e6.place(x=390, y=100)
                e7 = Entry(width=10)
                e7.place(x=590, y=160)

                def add():
                    cno = int(e3.get())
                    teacher = e4.get()
                    cname = e5.get()
                    password = e6.get()
                    credit = e7.get()
                    if cno == '' or cname == '' or cname == '' or password == '' or credit == '':
                        messagebox.showerror('添加失败', '请查看输入信息是否完整！')
                    else:
                        try:
                            str1 = "insert into course(cno,ccredit,teacher,cname) values('%s','%s','%s','%s')" % (cno, credit, teacher, cname)
                            cursor.execute(str1)
                            conn.commit()
                            str2 = "insert into information(NO,PASSWORD,[identity]) values('%s','%s','teacher   ')" % (cno + 300000, password)
                            cursor.execute(str2)
                            conn.commit()
                            str3 = "已经添加教师%s，负责学科%s，编号%s，登录账户为%s,密码为%s" % (teacher, cname, cno, cno + 300000, password)
                            listbox1.insert(listbox1.size(), str3)
                        except:
                            messagebox.showerror('添加失败', '编号发生重复')

                def delete():
                    cno = int(e3.get())
                    if cno == '':
                        messagebox.showerror('添加失败', '请输入必要的编号信息')
                    else:
                        str1 = "delete from information where NO=%s" % (cno + 300000)
                        cursor.execute(str1)
                        conn.commit()
                        str2 = "delete from course where cno=%s" % cno
                        cursor.execute(str2)
                        conn.commit()
                        str3 = "已经删除编号号为%s的课程信息" % cno
                        listbox1.insert(listbox1.size(), str3)

                def CX():
                    for child in tree.get_children():
                        tree.delete(child)
                    str1 = "select cno,teacher,cname, ccredit from information, course where course.cno=information.NO-300000 order by cno desc"
                    cursor.execute(str1)
                    T = cursor.fetchall()
                    for row in T:
                        tree.insert("", 0, values=(row[0], row[1], row[2], row[3]))

                def qx1():
                    rt3.destroy()
                    Administer(0)

                Button(rt3, text='教师表', command=CX).place(x=700, y=30, width=180, height=50)
                Button(rt3, text='添加', command=add).place(x=700, y=100, width=180, height=50)
                Button(rt3, text='删除', command=delete).place(x=700, y=170, width=180, height=50)
                Button(rt3, text='返回', command=qx1).place(x=700, y=240, width=180, height=50)

            def select():
                rt2.destroy()
                rt3 = Tk()
                rt3.title("选课界面")
                rt3.geometry('920x600+600+100')
                listbox1 = Listbox(rt3)
                listbox1.place(width=380, height=300, x=510, y=280)

                columns = ("学号", "姓名")
                tree1 = ttk.Treeview(rt3, height=18, show="headings", columns=columns)  # 隐藏首列
                tree1.column("学号", width=70)  # 表示列,不显示
                tree1.column("姓名", width=70)
                tree1.place(x=20, y=190)
                tree1.heading("学号", text='学号', anchor=CENTER)
                tree1.heading("姓名", text='姓名', anchor=CENTER)
                str1 = "select sno,sname from student order by sno desc"
                cursor.execute(str1)
                T1 = cursor.fetchall()
                for row in T1:
                    tree1.insert("", 0, values=(row[0], row[1]))

                columns = ("编号", "教师", "学科", "学分")
                tree2 = ttk.Treeview(rt3, height=18, show="headings", columns=columns)  # 隐藏首列
                tree2.column("编号", width=70)  # 表示列,不显示
                tree2.column("教师", width=70)
                tree2.column("学科", width=70)
                tree2.column("学分", width=70)
                tree2.place(x=195, y=190)
                tree2.heading("编号", text='编号', anchor=CENTER)
                tree2.heading("教师", text='教师', anchor=CENTER)
                tree2.heading("学科", text='学科', anchor=CENTER)
                tree2.heading("学分", text='学分', anchor=CENTER)
                str2 = "select cno,teacher,cname,ccredit from course order by cno desc"
                cursor.execute(str2)
                T2 = cursor.fetchall()
                for row in T2:
                    tree2.insert("", 0, values=(row[0], row[1], row[2], row[3]))

                Label(text='选课系统', font=20, fg='red').place(x=450, y=10)
                Label(text='学号：', font=10).place(x=110, y=100)
                Label(text='编号：', font=10).place(x=460, y=100)


                e3 = Entry(width=30)
                e3.focus()
                e3.place(x=190, y=100)
                e4 = Entry(width=30)
                e4.place(x=540, y=100)

                def start():
                    sno = int(e3.get())
                    cno = int(e4.get())

                    if sno == '' or cno == '' :
                        messagebox.showerror('选课失败', '请查看输入信息是否完整！')
                    else:
                        try:
                            str1 = "insert into sc(sno,cno) values('%s','%s')" % (sno, cno)
                            cursor.execute(str1)
                            conn.commit()
                            str2 = "学号为%s的学生已经选课编号为%s的老师的课程" % (sno, cno)
                            listbox1.insert(listbox1.size(), str2)
                        except:
                            messagebox.showerror('添加失败', '信息出现错误，无法选课。')

                def end():
                    sno = int(e3.get())
                    cno = int(e4.get())

                    str1 = "select * from sc where sno=%s and cno=%s" % (sno, cno)
                    cursor.execute(str1)
                    T=cursor.fetchall()
                    if T == []:
                        messagebox.showerror('退课失败', '请重新输入正确的信息')
                    else:
                        str2 = "delete from sc where sno=%s and cno=%s" % (sno, cno)
                        cursor.execute(str2)
                        conn.commit()
                        str3 = "学号为%s的学生已经退课课程号号为%s的课程" % (sno, cno)
                        listbox1.insert(listbox1.size(), str3)

                def qx2():
                    rt3.destroy()
                    Administer(0)

                Button(rt3, text='选课', command=start).place(x=510, y=190, width=100, height=70)
                Button(rt3, text='退课', command=end).place(x=650, y=190, width=100, height=70)
                Button(rt3, text='返回', command=qx2).place(x=790, y=190, width=100, height=70)

            def qx():
                rt2.destroy()
                Main()

            Button(rt2, text='添加学生用户', command=addstudent).place(x=120, y=100, width=150, height=80)
            Button(rt2, text='添加老师用户', command=addteacher).place(x=295, y=100, width=150, height=80)
            Button(rt2, text='学生选课', command=select).place(x=475, y=100, width=150, height=80)
            Button(rt2, text='退出登录', command=qx).place(x=650, y=100, width=150, height=80)

        #####################分界线#######################

        s1 = int(e1.get())
        s2 = e2.get()
        cursor.execute("SELECT * FROM information WHERE NO='%s' AND PASSWORD = '%s' " % (s1, s2))
        t = cursor.fetchone()
        if t is None:
            messagebox.showerror('登录失败', '账户或密码错误！')
            # Main()
        elif t[2] == 'student   ':
            student()
        elif t[2] == 'teacher   ':
            teacher(1)
        elif t[2] == 'administor':
            Administer(1)

    btn1 = Button(rt, text="登录", command=login)
    btn1.place(x=100, y=200, width=150, height=40)
    btn2 = Button(rt, text="修改密码", command=XGMM)
    btn2.place(x=300, y=200, width=150, height=40)

    rt.mainloop()


Main()
