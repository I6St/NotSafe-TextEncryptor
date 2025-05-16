import tkinter as tk
from tkinter import ttk, messagebox


# 史山代码千万别改

def encrypt():
    chars = []
    asciis = []
    key = ety2.get()
    text = ety1.get('1.0', 'end')
    # text += '此字段由ApartKP文本加密器加密。不保证其安全性。'  # 水印
    if ety3.get()[0] + ety3.get()[1] + ety3.get()[2] in text:
        messagebox.showerror('错误', '明文内不能包含替换字符！(可以换顺序)')
        return
    try:
        for i in text:
            chars.append(i)
            asciis.append(ord(i) * int(key))
    except:
        messagebox.showerror('错误', '密钥只能是数字!')
        return
    # 先把列表的每个项转成2进制，然后替换
    try:
        for i in range(len(asciis)):
            asciis[i] = bin(asciis[i])
            asciis[i] = asciis[i][2:]
        for i in range(len(asciis)):
            asciis[i] = asciis[i].replace('1', ety3.get()[0])
        for i in range(len(asciis)):
            asciis[i] = asciis[i].replace('0', ety3.get()[1])
        result_str = ''
        for i in asciis:
            result_str += i
            result_str += ety3.get()[2]
        res.delete('1.0', 'end')
        res.insert('insert', result_str)
    except:
        messagebox.showerror('错误', '请输入完整的替换字符！')


def decrypt():
    asciis = []
    chars = []
    key = ety2.get()
    origin_str = ety1.get('1.0', 'end')
    asciis = origin_str.split(ety3.get()[2])
    res.delete('1.0', 'end')
    try:
        # 将替换字转为1和0
        for i in range(len(asciis)):
            asciis[i] = asciis[i].replace(ety3.get()[0], '1')
        for i in range(len(asciis)):
            asciis[i] = asciis[i].replace(ety3.get()[1], '0')
        # 忽略换行符
        for i in asciis:
            if i == '\n':
                continue
            # 将替换字按Unicode码转换为文字
            chars.append(chr(int(int(i, 2) / int(key))))
            origin_str += chr(int(int(i, 2) / int(key)))
        # 清除替换字
        origin_str = origin_str.replace(ety3.get()[0], '')
        origin_str = origin_str.replace(ety3.get()[1], '')
        origin_str = origin_str.replace(ety3.get()[2], '')
        res.insert('insert', origin_str)
    except Exception as err:
        messagebox.showerror('错误', '出现错误，请检查所有选项是否填写正确')


# GUI部分


root = tk.Tk()
root.title('文本加密器')
root.geometry('500x800')
root.resizable(False, False)

txt1 = ttk.Label(root, text='欢迎使用文本加密器')
txt1.pack()
txt2 = ttk.Label(root, text='请输入文字')
txt2.pack()
ety1 = tk.Text(root, width=40, height=10)
ety1.pack()
txt3 = ttk.Label(root, text='请输入密钥(数字)')
txt3.pack()
ety2 = ttk.Entry(root)
ety2.pack()
ety2.insert('insert', '1')
ety3 = ttk.Entry(root)
txt5 = ttk.Label(root, text='请输入替换字符(3个，写多了没用)')
txt5.pack()
ety3.pack()
ety3.insert('insert', '哈基米')
btn1 = ttk.Button(root, text='加密文本', width=30, command=encrypt)
btn1.pack()
btn2 = ttk.Button(root, text='解密文本', width=30, command=decrypt)
btn2.pack()
txt4 = ttk.Label(root, text='结果区')
txt4.pack()
res = tk.Text(root, width=40, height=30)
res.pack()
btn3 = ttk.Button(root, text='关于程序', width=30, command=lambda: messagebox.showinfo('提示', '程序作者: ApartKP'))
btn3.pack()

# 窗口主循环
root.mainloop()
