from Command import commandPage
from SignUpPage import SignUpPage
from Admin import AdminPage
import tkinter as tk
import sqlite3

class Login ():
    def __init__(self):
        # 设置窗口
        self.root = tk.Tk()
        self.root.title('用户登录')
        self.root['height'] = 300
        self.root['width'] = 600

        self.labelTitle = tk.Label(self.root, text='请输入用户名和密码', font=("微软雅黑", 14), justify=tk.CENTER, anchor='center',width=200)
        self.labelTitle.place(x=210, y=15, width=200, height=30)
        self.labeName = tk.Label(self.root, text='用户名:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=50, width=125, height=30)

        self.varName = tk.StringVar(self.root, value='')
        self.entryName = tk.Entry(self.root, width=80, textvariable=self.varName)
        self.entryName.place(x=200, y=50, width=250, height=30)

        self.labeName = tk.Label(self.root, text='密码:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        self.labeName.place(x=50, y=90, width=125, height=30)

        self.varPwd = tk.StringVar(self.root, value='')
        self.entryPwd = tk.Entry(self.root, show='*', width=80, textvariable=self.varPwd)
        self.entryPwd.place(x=200, y=90, width=250, height=30)

        # 创建按钮组件，同时设置按钮事件处理函数
        self.buttonsign = tk.Button(self.root, text='注册', command=self.signup)
        self.buttonsign.place(x=100, y=135, width=80, height=30)
        
        self.buttonOk = tk.Button(self.root, text='用户登录', command=self.login_user)
        self.buttonOk.place(x=200, y=135, width=80, height=30)

        self.buttonOk_ = tk.Button(self.root, text='管理员登录', command=self.login_command)
        self.buttonOk_.place(x=300, y=135, width=80, height=30)

        self.buttonCancel = tk.Button(self.root, text='取消', command=self.cancel)
        self.buttonCancel.place(x=400, y=135, width=80, height=30)

        self.root.mainloop() 


    # 注册按钮事件处理函数
    def signup(self):
        SignUpPage()

    # 登录按钮事件处理函数
    def login_user(self):
        # 获取用户名和密码
        self.buttonCancel['state'] = 'disable'
        self.buttonOk['state'] = 'disable'
        name = self.entryName.get()
        pwd = self.entryPwd.get()

        f = open('apply.txt', 'r', encoding='utf-8')
        fi = f.readlines()
        dic_unview = {}
        for lst in fi:
            d = str(lst).strip('\n').split(",")
            print(d)
            dic_unview[d[0]] = d[1]  
        f.close()

        f = open('info.txt', 'r', encoding='utf-8')
        fi = f.readlines()
        dic = {}
        for lst in fi:
            d = str(lst).strip('\n').split(",")
            print(d)
            dic[d[0]] = d[1] 
            
        # OK按钮事件处理函数
        def OK():
            self.root['height'] = 300
            labelPrompt.destroy()  # 删除控件
            labelMessage.destroy()
            self.buttonOk['state'] = 'active'  # 将按钮改为可用状态
            self.buttonCancel['state'] = 'active'

        def Log():
            self.root.destroy()
            AdminPage()

        if name in dic and dic[name] == pwd:
            labelMessage = tk.Label(self.root, text='Message', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
            labelMessage.place(x=0, y=200, width=600, height=30)
            self.root['height'] = 350
            labelPrompt = tk.Label(self.root, text='登陆成功', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
            labelPrompt.place(x=90, y=250, width=90, height=30)
            buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=Log)
            buttonOkk.place(x=500, y=300, width=80, height=30)
        elif name in dic_unview:
            labelMessage = tk.Label(self.root, text="Message                                                              "
                                                    "                                X       ", fg='white', bg='blue',
                                        font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=600)
            labelMessage.place(x=0, y=200, width=600, height=30)
            self.root['height'] = 350
            labelPrompt = tk.Label(self.root, text='管理员未审核', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='w',
                                        width=100)
            labelPrompt.place(x=90, y=250, width=180, height=30)
            buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
            buttonOkk.place(x=500, y=300, width=80, height=30)
        else:
            labelMessage = tk.Label(self.root, text="Message                                                              "
                                                    "                                X       ", fg='white', bg='blue',
                                        font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=600)
            labelMessage.place(x=0, y=200, width=600, height=30)
            self.root['height'] = 350
            labelPrompt = tk.Label(self.root, text='用户名和密码不匹配', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='w',
                                        width=100)
            labelPrompt.place(x=90, y=250, width=180, height=30)
            buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
            buttonOkk.place(x=500, y=300, width=80, height=30)


    # 管理员登录按钮事件处理函数
    def login_command(self):
        # 获取用户名和密码
        self.buttonCancel['state'] = 'disable'
        self.buttonOk['state'] = 'disable'
        self.buttonOk_ ['state'] = 'disable'
        name = self.entryName.get()
        pwd = self.entryPwd.get()

        # OK按钮事件处理函数
        def OK():
            self.root['height'] = 300
            labelPrompt.destroy()  # 删除控件
            labelMessage.destroy()
            self.buttonOk['state'] = 'active'  # 将按钮改为可用状态
            self.buttonCancel['state'] = 'active'
            self.buttonOk_ ['state'] = 'active'

        def Log():
            self.root.destroy()
            commandPage()

        if name=='gly' and pwd=='11227788':
            labelMessage = tk.Label(self.root, text='Message', fg='white', bg='blue', font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=80)
            labelMessage.place(x=0, y=200, width=600, height=30)
            self.root['height'] = 350
            labelPrompt = tk.Label(self.root, text='登陆成功', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
            labelPrompt.place(x=90, y=250, width=90, height=30)
            buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=Log)
            buttonOkk.place(x=500, y=300, width=80, height=30)


        else:
            labelMessage = tk.Label(self.root, text="Message                                                              "
                                                    "                                X       ", fg='white', bg='blue',
                                        font=("Times New Roman", 16),
                                        justify=tk.RIGHT, anchor='w', width=600)
            labelMessage.place(x=0, y=200, width=600, height=30)
            self.root['height'] = 350
            labelPrompt = tk.Label(self.root, text='用户名和密码不匹配', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='w',
                                        width=100)
            labelPrompt.place(x=90, y=250, width=180, height=30)
            buttonOkk = tk.Button(self.root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
            buttonOkk.place(x=500, y=300, width=80, height=30)




    # 取消按钮的事件处理函数
    def cancel(self):
        # 清空用户输入的用户名和密码
        self.varName.set('')
        self.varPwd.set('')

Login = Login ()