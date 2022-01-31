from tkinter import *

app = Tk()
app.title('CROP')
#jaka rozdzielczość??
app.geometry('500x700')
title = Label(app,text='CROP THE IMAGE', front='arial 30 bold', fg='#068481')
title.pack()

image_area = Canvas(app, width=490, height=500, bg='#C8C8C8')
image_area.pack(pady=(10,0))

open_image = Button(app, width=20, text='OPEN VIDEO FILE', front='none 12')
open_image.pack(pady=(10,5))

open_image = Button(app, width=20, text='SELECT COORDINATES', front='none 12')
open_image.pack(pady=(10,5))

open_image = Button(app, width=20, text='OPEN VIDEO FILE', front='none 12')
open_image.pack(pady=(10,5))

open_image = Button(app, width=20, text='OPEN VIDEO FILE', front='none 12')
open_image.pack(pady=(10,5))