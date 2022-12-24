import tkinter as tk
import sqlite3
import os

class commandPage():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('管理员')

        self.conn = sqlite3.connect('helping.db')
        self.cur = self.conn.cursor()
        
        #获取所有物品类别信息，储存为self.kinds
        self.cur.execute("select name from sqlite_master where type='table'")
        self.kinds = self.cur.fetchall()
        self.kinds=[line[0] for line in self.kinds]

        self.root['height'] = 300
        self.root['width'] = 600

        self.labeName = tk.Label(self.root, text='用户管理:', font=("微软雅黑", 10), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=25, width=125, height=20)

        self.labeName = tk.Label(self.root, text='物品管理:', font=("微软雅黑", 10), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=100, width=125, height=20)

        # 创建按钮组件，同时设置按钮事件处理函数
        buttonNewApply = tk.Button(self.root, text='审核新用户', command=self.NewApply)
        buttonNewApply.place(x=150, y=55, width=120, height=30)
        buttonChangeClass = tk.Button(self.root, text='更改物品类型', command=self.ChangeClass)
        buttonChangeClass.place(x=300, y=130, width=120, height=30)
        buttonNewClass = tk.Button(self.root, text='设置新物品类型', command=self.AddClass)
        buttonNewClass.place(x=150, y=130, width=120, height=30)        
        self.root.mainloop()

    # 用户审核按钮事件处理函数
    def NewApply(self):
        self.fi=''

        def View():
            if not os.path.getsize('apply.txt'):
                #self.fi='没有新申请'
                self.labelPrompt.config(text ='没有新申请')
            else:
                f = open('apply.txt', 'r', encoding='utf-8')
                self.fi = f.readline()
                self.labelPrompt.config(text =self.fi)
                f.close()

        def Agree():
            f = open('apply.txt', 'r', encoding='utf-8')
            self.l = f.readline()
            f.close()
            if self.l == self.fi and self.l:
                file = open('apply.txt', 'r', encoding='utf-8')
                lines = file.readlines()
                del lines[0]
                file.close()

                file_new = open('apply.txt','w')
                file_new.writelines(lines)
                file_new.close()

                file_info = open('info.txt','a')
                file_info.write(self.fi)
                file_info.close()
                self.labelPrompt.config(text ='已同意')
            else:
                #self.fi='请使用查看按钮更新申请'
                self.labelPrompt.config(text ='请使用查看按钮更新申请')

        def Deny():
            f = open('apply.txt', 'r', encoding='utf-8')
            self.l = f.readline() 
            f.close()
            if self.l == self.fi and self.l:
                file = open('apply.txt', 'r', encoding='utf-8')
                lines = file.readlines()
                del lines[0]
                file.close()

                file_new = open('apply.txt','w')
                file_new.writelines(lines)
                file_new.close()
                self.labelPrompt.config(text ='已拒绝')

            else:
                self.labelPrompt.config(text ='请使用查看按钮更新申请')

        def OK():
            self.root['height'] = 300
            self.labelPrompt.destroy()  # 删除控件
            self.buttonView.destroy()
            self.buttonAgree.destroy()
            self.buttonDeny.destroy()
            self.labelMessage.destroy()

        self.labelMessage = tk.Label(self.root, text='新用户审核', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
        self.labelMessage.place(x=0, y=200, width=600, height=30)
        self.root['height'] = 400
        self.labelPrompt = tk.Label(self.root, text=self.fi, font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelPrompt.place(x=0, y=250, width=400, height=30)

        self.buttonView = tk.Button(self.root, text='查看新申请', font=("微软雅黑", 14), activeforeground='#ff0000', command=View)
        self.buttonView.place(x=100, y=300, width=80, height=30)
        self.buttonAgree = tk.Button(self.root, text='同意', font=("微软雅黑", 14), activeforeground='#ff0000', command=Agree)
        self.buttonAgree.place(x=200, y=300, width=80, height=30)
        self.buttonDeny = tk.Button(self.root, text='不通过', font=("微软雅黑", 14), activeforeground='#ff0000', command=Deny)
        self.buttonDeny.place(x=300, y=300, width=80, height=30)

        self.buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        self.buttonOkk.place(x=500, y=350, width=80, height=30)



    def AddClass(self):
        self.txt = ''
        def Add():
            name = self.entryItem.get()
            pp = self.entryproperty.get()
            if not name:
                self.txt = '请输入物品名称'
            elif not pp:
                self.txt = '请输入物品属性'
            elif name in self.kinds:
                self.txt = '物品类型已存在'                
            else:
                for i in range(0,len(pp)):
                    prop = prop + pp[i]+' text, '
                prop = prop[0:len(prop)-2]
                self.cur.execute('CREATE TABLE not exists %s(%s)'%(name,prop))
                self.conn.commit()

        def OK():
            self.root['height'] = 300
            self.labelA.destroy()  # 删除控件
            self.labelMessage.destroy()
            self.entryItem.destroy()
            self.labelB.destroy()
            self.entryproperty.destroy()
            self.buttonAddC.destroy()
            self.labelC.destroy()
            self.buttonOkk.destroy()

        self.labelMessage = tk.Label(self.root, text='新建物品类型', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
        self.labelMessage.place(x=0, y=200, width=600, height=30)
        self.root['height'] = 450

        self.labelA = tk.Label(self.root, text='请输入新物品类的名称：', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelA.place(x=90, y=250, width=160, height=30)
        self.varItem = tk.StringVar(self.root, value='')
        self.entryItem = tk.Entry(self.root, width=80, textvariable=self.varItem)
        self.entryItem.place(x=250, y=250, width=250, height=30)

        self.labelB = tk.Label(self.root, text='请输入新物品类的属性：', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelB.place(x=90, y=300, width=160, height=30)
        self.varproperty = tk.StringVar(self.root, value='')
        self.entryproperty = tk.Entry(self.root, width=80, textvariable=self.varproperty)
        self.entryproperty.place(x=250, y=300, width=250, height=30)       

        self.buttonAddC = tk.Button(self.root, text='添加', font=("微软雅黑", 14),activeforeground='#ff0000', command=Add)
        self.buttonAddC.place(x=200, y=350, width=80, height=30)

        self.buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        self.buttonOkk.place(x=500, y=350, width=80, height=30)

        self.labelC = tk.Label(self.root, text=self.txt, font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelC.place(x=90, y=350, width=200, height=30)



    def ChangeClass(self):
        def OK():
            self.root['height'] = 300
            self.labelA.destroy()  # 删除控件
            self.labelMessage.destroy()
            self.buttonOkk.destroy()

        self.labelMessage = tk.Label(self.root, text='Message', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
        self.labelMessage.place(x=0, y=200, width=600, height=30)
        self.root['height'] = 400

        self.labelA = tk.Label(self.root, text='功能尚在开发中', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelA.place(x=90, y=250, width=120, height=30)

        self.buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        self.buttonOkk.place(x=500, y=350, width=80, height=30)


