import tkinter as tk

class SignUpPage():
    def __init__(self,master=None):
        self.root = master
        self.createPage()
     
        
    def createPage (self):  
        self.page = tk.Tk()
        self.page.title('注册')
        self.page['height'] = 300
        self.page['width'] = 600

        self.labeName = tk.Label(self.page, text='用户名:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=50, width=125, height=30)

        self.varName = tk.StringVar(self.page, value='')
        self.entryName = tk.Entry(self.page, width=80, textvariable=self.varName)
        self.entryName.place(x=200, y=50, width=250, height=30)

        self.labeName = tk.Label(self.page, text='密码:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=90, width=125, height=30)

        self.varPwd = tk.StringVar(self.page, value='')
        self.entryPwd = tk.Entry(self.page, show='*', width=80, textvariable=self.varPwd)
        self.entryPwd.place(x=200, y=90, width=250, height=30)

        self.labeName = tk.Label(self.page, text='住址:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=130, width=125, height=30)

        self.varAdd = tk.StringVar(self.page, value='')
        self.entryAdd = tk.Entry(self.page, width=80, textvariable=self.varAdd)
        self.entryAdd.place(x=200, y=130, width=250, height=30)
        
        self.labeName = tk.Label(self.page, text='联系方式:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=170, width=125, height=30)

        self.varConnect = tk.StringVar(self.page, value='')
        self.entryConnect = tk.Entry(self.page, width=80, textvariable=self.varConnect)
        self.entryConnect.place(x=200, y=170, width=250, height=30)

        # 创建按钮组件，同时设置按钮事件处理函数
        self.buttonsignup = tk.Button(self.page, text='注册', command=self.signup)
        self.buttonsignup.place(x=200, y=200, width=80, height=30)      

        self.page.mainloop()

        # 注册按钮事件处理函数
    def signup(self):
        # 获取用户名/密码/个人信息
        self.name = self.entryName.get()
        self.pwd = self.entryPwd.get()
        self.add = self.entryAdd.get()
        self.con = self.entryConnect.get()
        
        # 获取已注册用户信息
        f = open('info.txt', 'r', encoding='utf-8')
        fi = f.readlines()
        dic = {}

        # OK按钮事件处理函数
        def Re():
            self.page['height'] = 300
            self.labelPrompt.destroy()  # 删除控件
            self.labelMessage.destroy()

        def OK():
            self.page.destroy()

        if self.name in dic :
            self.labelMessage = tk.Label(self.page, text='Message', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
            self.labelMessage.place(x=0, y=200, width=600, height=30)
            self.page['height'] = 350
            self.labelPrompt = tk.Label(self.page, text='用户名已存在', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
            self.labelPrompt.place(x=90, y=250, width=90, height=30)
            self.buttonOkk = tk.Button(self.page, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=Re)
            self.buttonOkk.place(x=500, y=300, width=80, height=30)


        else:
            g = open('apply.txt', 'r', encoding='utf-8')
            gi = g.readlines()
            dic_g = {}
            g.close()
            if (self.name in dic_g)==0 :
                g = open('apply.txt','a')
                newline = self.name + ',' + self.pwd +','+self.add+','+self.con+'\n'
                g.write( newline )
                g.close()


            self.labelMessage = tk.Label(self.page, text="Message                                                              "
                                                    "                                X       ", fg='white', bg='blue',
                                        font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=600)
            self.labelMessage.place(x=0, y=200, width=600, height=30)
            self.page['height'] = 350
            self.labelPrompt = tk.Label(self.page, text='请等待管理员审核', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='w',
                                        width=100)
            self.labelPrompt.place(x=90, y=250, width=180, height=30)
            self.buttonOkk = tk.Button(self.page, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
            self.buttonOkk.place(x=500, y=300, width=80, height=30)






