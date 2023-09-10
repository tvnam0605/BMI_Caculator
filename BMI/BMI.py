from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Máy đo chỉ số cơ thể")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    h=float(Height.get())
    w = float(Weight.get())

    #convert height into meter
    m = h/100
    bmi = round(float(w/m**2),1)
    label1.config(text=bmi)
    # BANJ COS THEER DDOOIR GIAS TRI, BOI VI CAC NUOC THI CO CAC CHI SO KHAC NHAU
    if bmi <= 18.5:
        label2.config(text="Thiếu cân!")
        label3.config(text="Bạn có cân nặng thấp hơn cơ thể bình thường!")
    elif bmi> 18.5 and bmi <25:
        label2.config(text="Bình Thường!")
        label3.config(text="Nó chỉ ra rằng bạn có cơ thể khỏe mạnh!")
    elif bmi > 25 and bmi <= 30:
        label2.config(text="Thừa cân!")
        label3.config(text="nó chỉ ra rằng một người \n hơi thừa cân \n Bác sĩ có thể khuyên nên giảm một số \n cân vì lý do sức khỏe!")    
    else:
        label2.config(text="Béo phì!")
        label3.config(text="Sức khỏe có thể gặp nguy hiểm!")
 #icon
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

#top
top = PhotoImage(file="Images/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)


#bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

#two Boxes
box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y = 100)
Label(root, image=box).place(x=240, y = 100)

#scale
scale = PhotoImage(file="Images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y = 310)


################Slider1##################
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = (Image.open("Images/man.png"))
    resized_image=img.resize((50,10+size))
    photo2 =ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 -size)
    secondimage.image=photo2

#command to change background color of scale
style = ttk.Style()
style.configure("TSale", background = "white")
slider = ttk.Scale(root,from_ = 0, to = 220, orient='horizontal', style="TScale",
                   command=slider_changed, variable=current_value)
slider.place(x=88, y = 250)


#########################################

##@@@@@@@@@@@@@@Slider2@@@@@@@@@@@@@@@@##
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())

#command to change background color of scale
style2 = ttk.Style()
style2.configure("TSale", background = "white")
slider2 = ttk.Scale(root,from_ = 0, to = 200, orient='horizontal', style="TScale",
                   command=slider_changed2, variable=current_value2)
slider2.place(x=300, y = 250)


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##









#entry box
Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd = 0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd = 0, justify=CENTER)
weight.place(x=255, y=160)

Weight.set(get_current_value2())



#main image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y = 530)

Button(root, text="Xem kết quả", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y = 340)
label1 = Label(root, font= "arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y= 305)

label2 = Label(root, font= "arial 20 bold", bg="lightblue", fg="#3b3a4a")
label2.place(x=280, y= 430)


label3 = Label(root, font= "arial 10 bold", bg="lightblue")
label3.place(x=200, y= 500)




root.mainloop()