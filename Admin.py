import tkinter as tk
import sqlite3
import os

class AdminPage():
    def __init__(self):
        self.out = '^-^'        
        self.root = tk.Tk()
        self.root.title('欢迎用户')
        self.root['height'] = 200
        self.root['width'] = 800

        self.conn = sqlite3.connect('helping.db')
        self.cur = self.conn.cursor()

        #获取所有物品类别信息，储存为self.kinds
        self.cur.execute("select name from sqlite_master where type='table'")
        self.kinds = self.cur.fetchall()
        self.kinds=[line[0] for line in self.kinds]
        self.kindl = ''
        for i in range(0,len(self.kinds)-1):
            self.kindl = self.kindl + self.kinds[i] +','
        self.kindl = self.kindl + self.kinds[len(self.kinds)-1]

        self.lb_putout = tk.Label(self.root,text=self.out,font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.lb_putout.place(x=50, y=150, width=500, height=30)  

        self.bn_add = tk.Button(self.root,text='添加',command=self.add)
        self.bn_add.place(x=50, y=50, width=150, height=30)

        self.bn_delete = tk.Button(self.root,text='删除',command=self.off)
        self.bn_delete.place(x=250, y=50, width=150, height=30)    

        self.bn_search = tk.Button(self.root,text='搜索',command=self.find)
        self.bn_search.place(x=50, y=100, width=150, height=30)
        
        self.bn_list = tk.Button(self.root,text='显示物品列表',command=self.lst)
        self.bn_list.place(x=250, y=100, width=150, height=30)      

        self.root.mainloop()

    #添加物品
    def add(self):
        def commit():
            self.out = ''  
            kd = self.entrykd.get()
            if kd in self.kinds:
                self.cur.execute('pragma table_info({})'.format(kd))
                attribute = self.cur.fetchall()
                attribute = [x[1] for x in attribute]
                txt_attribute = ''
                for i in range(0,len(attribute)):
                    txt_attribute = txt_attribute +'，'+attribute[i]
                txt_attribute = txt_attribute[1:len(txt_attribute)]
                self.labelattri.config(text=txt_attribute+'属性间请用逗号隔开')
            else:
                self.lb_putout.config(text = '请输入正确的物品类型')

        def AddItem():
            self.out = ''            
            kd = self.entrykd.get()
            if kd in self.kinds:
                attri = self.entryattri.get()            
                if attri == '':
                    self.lb_putout.config(text= '请输入物品属性') 
                else:
                    d = str(attri).split("，")
                    txt_s = ''
                    txt_v = ''
                    for i in range(0,len(d)-1):
                        txt_v = txt_v + '"'+ d[i] + ' ",'
                    txt_v = txt_v + '"'+ d[len(d)-1]+'"'

                    self.cur.execute('insert into %s values(%s)' %(kd,txt_v))
                    self.conn.commit()
                    self.lb_putout.config(text = '添加成功')
            else:
                self.out = '物品种类不存在！'


        def OK():
            self.root['height'] = 200
            self.labelChoices.destroy()  # 删除控件
            self.labelChoose.destroy()
            self.entrykd.destroy()
            self.buttoncommit.destroy()
            self.labelMessage.destroy()
            self.buttonOkk.destroy()
            self.labelattri.destroy()
            self.entryattri.destroy()
            self.buttonAddItem.destroy()
        

        self.labelMessage = tk.Label(self.root, text='添加', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
        self.labelMessage.place(x=0, y=200, width=800, height=30)
        self.root['height'] = 500

        self.labelChoices = tk.Label (self.root, text='物品种类有：'+ self.kindl ,font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoices.place(x=50, y=250, width=160, height=30)
        self.labelChoose = tk.Label (self.root, text='请输入想添加物品的类别',font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoose.place(x=50, y=300, width=160, height=30)
        self.varkd = tk.StringVar(self.root, value='')
        self.entrykd = tk.Entry(self.root, width=80, textvariable=self.varkd)
        self.entrykd.place(x=250, y=300, width=160, height=30)
        self.buttoncommit = tk.Button(self.root, text='确认', command=commit)
        self.buttoncommit.place(x=450, y=300, width=100, height=30)
        
        self.labelattri = tk.Label (self.root, text='请依次输入物品属性' ,font=("微软雅黑", 14), justify=tk.RIGHT, anchor='w', width=80)
        self.labelattri.place(x=50, y=350, width=700, height=30)        
        self.varattri = tk.StringVar(self.root, value='')
        self.entryattri = tk.Entry(self.root, width=80, textvariable=self.varattri)
        self.entryattri.place(x=50, y=400, width=500, height=30) 

        self.buttonAddItem = tk.Button(self.root, text='添加', command=AddItem)
        self.buttonAddItem.place(x=50, y=450, width=100, height=30)
        self.buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        self.buttonOkk.place(x=180, y=450, width=80, height=30)


    #删除物品                           
    def off(self):
        def commit():
            self.out = ''
            kd = self.entrykd.get()
            ID = self.entryid.get()
            if kd == '':
                self.lb_putout.config(text= '请输入物品种类')
            elif kd not in self.kinds:
                self.lb_putout.config(text= '物品种类不存在！')
            elif ID == '':
                self.lb_putout.config(text= '请输入用户名!')
            else:
                self.cur.execute('select * from %s where id like "%s"' %(kd,ID)) 
                for record in self.cur.fetchall():self.out = self.out + str(record) + '\n' 
                self.labellist.config(text=self.out) 


        def DeItem():
            it = self.entryDelete.get()
            kd = self.entrykd.get()
            ID = self.entryid.get()
            if it == '':
                self.lb_putout.config(text='请输入物品名')
            else:
                self.cur.execute('select * from %s where name like "%s"' %(kd,it))
                if (fetch:=self.cur.fetchone()) is None:
                    self.lb_putout.config(text = '物品不存在')
                else:
                    self.cur.execute('delete from %s where name = "%s" and id= "%s"' %(kd,it,ID))
                    self.conn.commit()
                    self.lb_putout.config(text = '删除成功')
                        
        def OK():
            self.root['height'] = 200
            self.labelChoices.destroy()  # 删除控件
            self.labelChoose.destroy()
            self.entrykd.destroy()
            self.buttoncommit.destroy()
            self.labelMessage.destroy()
            self.buttonOkk.destroy()
            self.labelDelete.destroy()
            self.entryDelete.destroy()
            self.buttonDeleteItem.destroy()
            self.labellist.destroy()
            self.entryid.destroy()
            self.labelid.destroy()

        self.labelMessage = tk.Label(self.root, text='删除', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
        self.labelMessage.place(x=0, y=200, width=800, height=30)
        self.root['height'] = 600

        self.labelChoices = tk.Label (self.root, text='物品种类有：'+ self.kindl ,font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoices.place(x=50, y=250, width=160, height=30)
        self.labelChoose = tk.Label (self.root, text='请输入想删除物品的类别',font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoose.place(x=50, y=300, width=160, height=30)
        self.varkd = tk.StringVar(self.root, value='')
        self.entrykd = tk.Entry(self.root, width=80, textvariable=self.varkd)
        self.entrykd.place(x=230, y=300, width=120, height=30)
        
        self.labelid = tk.Label (self.root, text='请输入您的用户名' ,font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelid.place(x=50, y=350, width=160, height=30)        
        self.varid = tk.StringVar(self.root, value='')
        self.entryid = tk.Entry(self.root, width=80, textvariable=self.varid)
        self.entryid.place(x=230, y=350, width=120, height=30) 
        self.buttoncommit = tk.Button(self.root, text='确认', command=commit)
        self.buttoncommit.place(x=390, y=350, width=100, height=30)

        self.labelDelete = tk.Label (self.root, text='想删除物品的名称',font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelDelete.place(x=50, y=400, width=160, height=30)
        self.varDelete = tk.StringVar(self.root, value='')
        self.entryDelete = tk.Entry(self.root, width=80, textvariable=self.varDelete)
        self.entryDelete.place(x=230, y=400, width=160, height=30)

        self.labellist = tk.Label (self.root, text='list', justify=tk.RIGHT, anchor='w', width=80)
        self.labellist.place(x=100, y=500, width=600, height=100)  
        
        self.buttonDeleteItem = tk.Button(self.root, text='删除', command=DeItem)
        self.buttonDeleteItem.place(x=50, y=450, width=100, height=30)
        self.buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        self.buttonOkk.place(x=300, y=450, width=80, height=30)
                 
    #查找物品
    def find(self):
        def search():
            self.out = ''
            kd = self.entrykd.get()
            if kd in self.kinds:
                it = self.entrykey.get()
                if it == '':
                    self.lb_putout.config(text = '请输入物品名')
                else:
                    self.out=''
                    self.cur.execute('select * from %s where name like "%%%s%%"' %(kd,it)) #如何同时在说明中匹配？
                    for record in self.cur.fetchall():self.out = self.out + str(record) + '\n' 
                    self.lb_putout.config(text=self.out) 
            else:
                self.lb_putout.config(text = '物品种类不存在！')


        def OK():
            self.root['height'] = 200
            self.labelChoices.destroy()  # 删除控件
            self.labelChoose.destroy()
            self.entrykd.destroy()
            self.labelkey.destroy()
            self.entrykey.destroy()
            self.buttonVisit.destroy()
            self.labelMessage.destroy()
            self.buttonOkk.destroy()
        
        self.labelMessage = tk.Label(self.root, text='查找', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
        self.labelMessage.place(x=0, y=200, width=800, height=30)
        self.root['height'] = 450

        self.labelChoices = tk.Label (self.root, text='物品种类有：'+ self.kindl  ,font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoices.place(x=50, y=250, width=160, height=30)
        self.labelChoose = tk.Label (self.root, text='请输入想查询的物品类别',font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoose.place(x=50, y=300, width=160, height=30)
        self.varkd = tk.StringVar(self.root, value='')
        self.entrykd = tk.Entry(self.root, width=80, textvariable=self.varkd)
        self.entrykd.place(x=250, y=300, width=160, height=30)
        
        self.labelkey = tk.Label (self.root, text='请输入关键词:',font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelkey.place(x=50, y=350, width=160, height=30)        
        self.varkey = tk.StringVar(self.root, value='')
        self.entrykey = tk.Entry(self.root, width=80, textvariable=self.varkey)
        self.entrykey.place(x=250, y=350, width=160, height=30) 

        self.buttonVisit = tk.Button(self.root, text='查找', command=search)
        self.buttonVisit.place(x=50, y=400, width=100, height=30)
        self.buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        self.buttonOkk.place(x=180, y=400, width=80, height=30)


    #显示物品清单
    def lst(self):
        def list():
            self.out = ''
            kd = self.entrykd.get()
            if kd in self.kinds:
                self.cur.execute('select * from %s' %kd)
                for record in self.cur.fetchall():self.out = self.out + str(record) + '\n' 
                self.lb_putout.config(text='物品清单已显示') 
                self.labellist.config(text=self.out) 
            else:
                self.lb_putout.config(text='物品种类不存在！') 


        def OK():
            self.root['height'] = 200
            self.labelChoices.destroy()  # 删除控件
            self.labelChoose.destroy()
            self.entrykd.destroy()
            self.buttonVisit.destroy()
            self.labelMessage.destroy()
            self.buttonOkk.destroy()
            self.labellist.destroy()
        

        self.labelMessage = tk.Label(self.root, text='显示列表', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
        self.labelMessage.place(x=0, y=200, width=800, height=30)
        self.root['height'] = 450

        self.labelChoices = tk.Label (self.root, text='物品种类有：'+ self.kindl ,font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoices.place(x=50, y=250, width=160, height=30)
        self.labelChoose = tk.Label (self.root, text='请输入想查询的物品类别',font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labelChoose.place(x=50, y=300, width=160, height=30)
        self.varkd = tk.StringVar(self.root, value='')
        self.entrykd = tk.Entry(self.root, width=80, textvariable=self.varkd)
        self.entrykd.place(x=50, y=350, width=160, height=30)
        self.buttonVisit = tk.Button(self.root, text='显示物品清单', command=list)
        self.buttonVisit.place(x=50, y=400, width=100, height=30)

        self.labellist = tk.Label (self.root, text='list', justify=tk.RIGHT, anchor='e', width=80)
        self.labellist.place(x=280, y=300, width=500, height=150)   

        self.buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        self.buttonOkk.place(x=180, y=400, width=80, height=30)


