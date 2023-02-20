from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI=Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อของโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดของโปรแกรม

B1=ttk.Button(GUI,text='เงินมีอยู่กี่บาท')#customปุ่มกด
B1.pack(ipadx=20, ipady=20) #ขนาดbutton


L1=Label(GUI,text='โปรแกรมบันทึกความรู้', font=('Angsana New',30), fg='green')
L1.place(x=30, y=20)

################
def Button2():
    text='ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1=LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=100, y=80)
B2=ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)#customปุ่มกด
B2.pack(ipadx=20, ipady=20,padx=30,pady=30)

############################
def Button3():
    text2='Python 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่่ 10-20 ก.พ.',text2)




FB2=LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB2.place(x=100, y=180)
B3=ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)#customปุ่มกด
B3.pack(ipadx=20, ipady=20,padx=30,pady=30)

#B2.place(x=50, y=200) #location of button





GUI.mainloop()
