from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image
def generateQRCode():
    #ดึงข้อมูล link มาสร้าง QRCode
    link_name=name_entry.get()
    link=like_entry.get()
    file_name = link_name+"png"
    #สร้าง QRCode
    url=pyqrcode.create(link)
    url.png(file_name,scale=5)
    #เเสดงภาพQRCode
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image=image
    canvas.create_window(200,370,window=image_label)

root = Tk()
root.title("QRCode Generator")
canvas=Canvas(root,width=400,height=500)
canvas.pack()
#ชื่อโปรเเกรม
app_label=Label(root,text = "QRCode Generator",font=("Arial",20,"bold"))
canvas.create_window(200,50,window=app_label)
#ระบุชื่อพร้อมกับลิงค์ --> QRCode
name_label = Label(root,text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200,100,window=name_label)

like_label = Label(root,text=("URL"))
canvas.create_window(200,160,window=like_label)

#สร้าง textbox
name_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)

like_entry=Entry(root)
canvas.create_window(200,180,window=like_entry)
#ปุ่มสร้าง QRCode
button = Button(text="สร้างคิวอาร์โค้ด",command=generateQRCode)
canvas.create_window(200,230,window=button)

root.mainloop()