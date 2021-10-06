from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","新建文档")

def printSelection():
    print(var.get())
    
root =Tk()
root.title("光谱仪通讯") # 窗口标题

# 窗口位置及大小
screenWith = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
w = 800
h = 600
x = (screenWith - w) / 2
y = (screenHeight - h ) / 2
root.geometry("%dx%d+%d+%d" % (w,h,x,y))

root.configure(bg='white')

#菜单
menubar = Menu(root)
filemenu = Menu(menubar)
menubar.add_cascade(label="文件",menu=filemenu,underline=0)

filemenu.add_command(label="New File",command=newFile, # 子菜单
                    accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="Eixt!",command=root.destroy,underline=0)
root.config(menu=menubar)
root.bind("<Control-N>",
          lambda event:messagebox.showinfo("New File","新建文档"))

#下拉菜单
var = StringVar()
cb = Combobox(root,textvariable=var)       #创建combobox
cb["value"] = ("选项1","选项2","选项3")
cb.current(0)
cb.pack(pady=10)

btn = Button(root,text="OK",command=printSelection) #创建按钮
btn.pack(pady=10,anchor=S,side="top")

#面板
pw = PanedWindow(orient=HORIZONTAL)
leftframe = LabelFrame(pw,text="left",width=120,height=50)
pw.add(leftframe,weight=5)
rightframe = LabelFrame(pw,text="right",width=120,height=50)
pw.add(rightframe,weight=5)
pw.pack(fill=BOTH,expand=True,padx=10,pady=10)

#选项卡
notebook = Notebook(root)
frame1 = Frame()
frame2 = Frame()

label=Label(frame1,text="光谱仪",relief="raised")
label.pack(padx=5,pady=10)
btn=Button(frame2,text="光谱仪")
btn.pack(padx=10,pady=10)

notebook.add(frame1,text="第一页")
notebook.add(frame2,text="第二页")
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)


root.mainloop()
