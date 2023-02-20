from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI=Tk()
GUI.title('โปรแกรมบันทึกคะแนน MFT 2023')
GUI.geometry('800x800')

L1=Label(GUI,text='MFT 2023 total score', font=('Angsana New',30), fg='red')
L1.place(x=30, y=20)
label_width = L1.winfo_reqwidth()
label_height = L1.winfo_reqheight()
screen_width = GUI.winfo_screenwidth()
screen_height = GUI.winfo_screenheight()
x = (screen_width/2) - (label_width/2)
y = 20
L1.place(x=x, y=y)
#############################################
def Button1():
    text='44'
    messagebox.showinfo('คะแนนรีน่า',text)

FB1=Frame(GUI)
FB1.place(x=50,y=80)

global img_rina
img_rina=PhotoImage(file="rina.pgm")
image_label=Label(FB1,image=img_rina)
image_label.pack(side=LEFT)


B1=ttk.Button(FB1,text='รีน่า MFT01',command=Button1)
B1.pack(ipadx=20,ipady=20)

######################################################
def Button2():
    text='14'
    messagebox.showinfo('คะแนนบลอสซั่ม',text)

FB2=Frame(GUI)
FB2.place(x=50,y=200)

global img_blossom
img_blossom=PhotoImage(file="blossom.pgm")
image_label=Label(FB2,image=img_blossom)
image_label.pack(side=LEFT)


B2=ttk.Button(FB2,text='บลอสซั่ม MFT02',command=Button2)
B2.pack(ipadx=20,ipady=20)

######################################################
def Button3():
    text='26'
    messagebox.showinfo('คะแนนลักกี้',text)

FB3=Frame(GUI)
FB3.place(x=50,y=300)

global img_lucky
img_lucky=PhotoImage(file="lucky.pgm")
image_label=Label(FB3,image=img_lucky)
image_label.pack(side=LEFT)


B3=ttk.Button(FB3,text='ลัคกี้ MFT03',command=Button3)
B3.pack(ipadx=20,ipady=20)
######################################################
def Button4():
    text='39'
    messagebox.showinfo('คะแนนนอรี่',text)

FB4=Frame(GUI)
FB4.place(x=50,y=400)

global img_noory
img_noory=PhotoImage(file="noory.pgm")
image_label=Label(FB4,image=img_noory)
image_label.pack(side=LEFT)


B4=ttk.Button(FB4,text='นอรี่ MFT04',command=Button4)
B4.pack(ipadx=20,ipady=20)
######################################################
def Button5():
    text='33'
    messagebox.showinfo('คะแนนเมญ่า',text)

FB5=Frame(GUI)
FB5.place(x=400,y=80)

global img_maeya
img_maeya=PhotoImage(file="maeya.pgm")
image_label=Label(FB5,image=img_maeya)
image_label.pack(side=LEFT)


B5=ttk.Button(FB5,text='เมญ่า MFT05',command=Button5)
B5.pack(ipadx=20,ipady=20)
######################################################
def Button6():
    text='32'
    messagebox.showinfo('คะแนนกะทิ',text)

FB6=Frame(GUI)
FB6.place(x=400,y=200)

global img_kati
img_kati=PhotoImage(file="kati.pgm")
image_label=Label(FB6,image=img_kati)
image_label.pack(side=LEFT)


B6=ttk.Button(FB6,text='กะทิ MFT06',command=Button6)
B6.pack(ipadx=20,ipady=20)
######################################################
def Button7():
    text='37'
    messagebox.showinfo('คะแนนโซเฟีย',text)

FB7=Frame(GUI)
FB7.place(x=400,y=300)

global img_sofia
img_sofia=PhotoImage(file="sofia.pgm")
image_label=Label(FB7,image=img_sofia)
image_label.pack(side=LEFT)


B7=ttk.Button(FB7,text='โซเฟีย MFT07',command=Button7)
B7.pack(ipadx=20,ipady=20)
######################################################
def Button8():
    text='48'
    messagebox.showinfo('คะแนนเซีย',text)

FB8=Frame(GUI)
FB8.place(x=400,y=400)

global img_sia
img_sia=PhotoImage(file="sia.pgm")
image_label=Label(FB8,image=img_sia)
image_label.pack(side=LEFT)


B8=ttk.Button(FB8,text='เซีย MFT08',command=Button8)
B8.pack(ipadx=20,ipady=20)
######################################################
def Button9():
    text='24'
    messagebox.showinfo('คะแนนมิ้น',text)

FB9=Frame(GUI)
FB9.place(x=800,y=80)

global img_mint
img_mint=PhotoImage(file="mint.pgm")
image_label=Label(FB9,image=img_mint)
image_label.pack(side=LEFT)


B9=ttk.Button(FB9,text='มิ้น MFT09',command=Button9)
B9.pack(ipadx=20,ipady=20)
######################################################
def Button10():
    text='22'
    messagebox.showinfo('คะแนนขุนแผน',text)

FB10=Frame(GUI)
FB10.place(x=800,y=200)

global img_khunpan
img_khunpan=PhotoImage(file="khunpan.pgm")
image_label=Label(FB10,image=img_khunpan)
image_label.pack(side=LEFT)


B10=ttk.Button(FB10,text='ขุนแผน MFT10',command=Button10)
B10.pack(ipadx=20,ipady=20)
######################################################
def Button11():
    text='34'
    messagebox.showinfo('คะแนนฝ้ายนา',text)

FB11=Frame(GUI)
FB11.place(x=800,y=320)

global img_fainah
img_fainah=PhotoImage(file="fainah.pgm")
image_label=Label(FB11,image=img_fainah)
image_label.pack(side=LEFT)


B11=ttk.Button(FB11,text='ฝ้ายนา MFT11',command=Button11)
B11.pack(ipadx=20,ipady=20)
######################################################
def Button12():
    text='37'
    messagebox.showinfo('คะแนนมะเดี่ยว',text)

FB12=Frame(GUI)
FB12.place(x=800,y=420)

global img_madeaw
img_madeaw=PhotoImage(file="madeaw.pgm")
image_label=Label(FB12,image=img_madeaw)
image_label.pack(side=LEFT)


B12=ttk.Button(FB12,text='มะเดี่ยว MFT12',command=Button12)
B12.pack(ipadx=20,ipady=20)

GUI.mainloop()
