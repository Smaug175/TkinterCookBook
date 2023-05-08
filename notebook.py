#用tkinter创建一个桌面应用程序
# -*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import tkinter.scrolledtext
import os
import shutil

#创建窗口
root=Tk()
root.title('coilpot')
root.geometry('800x600')

#创建菜单栏
menubar=Menu(root)
#创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='Open',command=lambda:open_file())
filemenu.add_command(label='Save',command=lambda:save_file())
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)

#创建下拉菜单Edit
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label='Cut',command=lambda:cut_file())
editmenu.add_command(label='Copy',command=lambda:copy_file())
editmenu.add_command(label='Paste',command=lambda:paste_file())
menubar.add_cascade(label='Edit',menu=editmenu)

#创建下拉菜单Help
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label='About',command=lambda:about())
menubar.add_cascade(label='Help',menu=helpmenu)

#显示菜单
root.config(menu=menubar)

#创建文本框
text=tkinter.scrolledtext.ScrolledText(root,font=('微软雅黑',10))
text.pack(fill=BOTH,expand=True)

#打开文件
def open_file():
    #清空文本框
    text.delete(1.0,END)
    #选择打开文件
    file_path=tkinter.filedialog.askopenfilename()
    if file_path!='':
        #打开文件
        with open(file_path,'r') as file:
            content=file.read()
        #显示到文本框
        text.insert(INSERT,content)

#保存文件
def save_file():
    #选择保存文件路径
    file_path=tkinter.filedialog.asksaveasfilename()
    if file_path!='':
        #获取文本框内容
        content=text.get(1.0,END)
        #保存文件
        with open(file_path,'w') as file:
            file.write(content)

#剪切文件
def cut_file():
    #获取文本框内容
    content=text.get(SEL_FIRST,SEL_LAST)
    #删除文本框内容
    text.delete(SEL_FIRST,SEL_LAST)
    #剪切板内容清空
    root.clipboard_clear()
    #剪切板赋值
    root.clipboard_append(content)
    
#复制文件
def copy_file():
    #获取文本框内容
    content=text.get(SEL_FIRST,SEL_LAST)
    #剪切板内容清空
    root.clipboard_clear()
    #剪切板赋值
    root.clipboard_append(content)

#粘贴文件
def paste_file():
    #获取剪切板内容
    content=root.clipboard_get()
    #删除文本框内容
    text.delete(SEL_FIRST,SEL_LAST)
    #插入文本框
    text.insert(INSERT,content)

#关于
def about():
    tkinter.messagebox.showinfo('About','coilpot\n\n')

#主消息循环
root.mainloop()

                                