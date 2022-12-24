import tkinter as tk
import sqlite3

f = open('info.txt', 'r', encoding='utf-8')
fi = f.readlines()
dic = {}
for lst in fi:
    d = str(lst).strip('\n').split(",")
    print(d)
    dic[d[0]] = d[1]

# 创建应用程序
root = tk.Tk()

# 设置窗口
root.title('用户登录')
root['height'] = 300
root['width'] = 600

labelTitle = tk.Label(root, text='请输入用户名和密码', font=("微软雅黑", 14), justify=tk.CENTER, anchor='center',width=200)
labelTitle.place(x=210, y=15, width=200, height=30)
labeName = tk.Label(root, text='用户名:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
labeName.place(x=50, y=50, width=125, height=30)

varName = tk.StringVar(root, value='')
entryName = tk.Entry(root, width=80, textvariable=varName)
entryName.place(x=200, y=50, width=250, height=30)

labeName = tk.Label(root, text='密码:', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
labeName.place(x=50, y=90, width=125, height=30)

varPwd = tk.StringVar(root, value='')
entryPwd = tk.Entry(root, show='*', width=80, textvariable=varPwd)
entryPwd.place(x=200, y=90, width=250, height=30)

# 注册按钮事件处理函数
def signup(self):
    self.page.destroy()
    SignUpPage(self.root)

# 创建按钮组件，同时设置按钮事件处理函数
buttonsign = tk.Button(root, text='注册', command=signup)
buttonsign.place(x=100, y=135, width=80, height=30)

# 登录按钮事件处理函数
def login_user():
    # 获取用户名和密码
    buttonCancel['state'] = 'disable'
    buttonOk['state'] = 'disable'
    name = entryName.get()
    pwd = entryPwd.get()

    # OK按钮事件处理函数
    def OK():
        root['height'] = 300
        labelPrompt.destroy()  # 删除控件
        labelMessage.destroy()
        buttonOk['state'] = 'active'  # 将按钮改为可用状态
        buttonCancel['state'] = 'active'

    if name in dic and dic[name] == pwd:
        labelMessage = tk.Label(root, text='Message', fg='white', bg='blue', font=("Times New Roman", 16),
                                     justify=tk.RIGHT, anchor='w', width=80)
        labelMessage.place(x=0, y=200, width=600, height=30)
        root['height'] = 350
        labelPrompt = tk.Label(root, text='登陆成功', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        labelPrompt.place(x=90, y=250, width=90, height=30)
        buttonOkk = tk.Button(root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        buttonOkk.place(x=500, y=300, width=80, height=30)


    else:
        labelMessage = tk.Label(root, text="Message                                                              "
                                                "                                X       ", fg='white', bg='blue',
                                     font=("Times New Roman", 16),
                                     justify=tk.RIGHT, anchor='w', width=600)
        labelMessage.place(x=0, y=200, width=600, height=30)
        root['height'] = 350
        labelPrompt = tk.Label(root, text='用户名和密码不匹配', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='w',
                                    width=100)
        labelPrompt.place(x=90, y=250, width=180, height=30)
        buttonOkk = tk.Button(root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        buttonOkk.place(x=500, y=300, width=80, height=30)


# 创建按钮组件，同时设置按钮事件处理函数
buttonOk = tk.Button(root, text='用户登录', command=login_user)
buttonOk.place(x=200, y=135, width=80, height=30)

# 管理员登录按钮事件处理函数
def login_command():
    # 获取用户名和密码
    buttonCancel['state'] = 'disable'
    buttonOk['state'] = 'disable'
    buttonOk_ ['state'] = 'disable'
    name = entryName.get()
    pwd = entryPwd.get()

    # OK按钮事件处理函数
    def OK():
        root['height'] = 300
        labelPrompt.destroy()  # 删除控件
        labelMessage.destroy()
        buttonOk['state'] = 'active'  # 将按钮改为可用状态
        buttonCancel['state'] = 'active'
        buttonOk_ ['state'] = 'active'

    if name=='gly' and pwd=='11227788':
        labelMessage = tk.Label(root, text='Message', fg='white', bg='blue', font=("Times New Roman", 16),
                                     justify=tk.RIGHT, anchor='w', width=80)
        labelMessage.place(x=0, y=200, width=600, height=30)
        root['height'] = 350
        labelPrompt = tk.Label(root, text='登陆成功', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='e', width=80)
        labelPrompt.place(x=90, y=250, width=90, height=30)
        buttonOkk = tk.Button(root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        buttonOkk.place(x=500, y=300, width=80, height=30)


    else:
        labelMessage = tk.Label(root, text="Message                                                              "
                                                "                                X       ", fg='white', bg='blue',
                                     font=("Times New Roman", 16),
                                     justify=tk.RIGHT, anchor='w', width=600)
        labelMessage.place(x=0, y=200, width=600, height=30)
        root['height'] = 350
        labelPrompt = tk.Label(root, text='用户名和密码不匹配', font=("微软雅黑", 14), justify=tk.RIGHT, anchor='w',
                                    width=100)
        labelPrompt.place(x=90, y=250, width=180, height=30)
        buttonOkk = tk.Button(root, text='ok', font=("微软雅黑", 14), activeforeground='#ff0000', command=OK)
        buttonOkk.place(x=500, y=300, width=80, height=30)


# 创建按钮组件，同时设置按钮事件处理函数
buttonOk_ = tk.Button(root, text='管理员登录', command=login_command)
buttonOk_.place(x=300, y=135, width=80, height=30)


# 取消按钮的事件处理函数
def cancel():
    # 清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')


buttonCancel = tk.Button(root, text='取消', command=cancel)
buttonCancel.place(x=400, y=135, width=80, height=30)

# 启动消息循环
root.mainloop() 
