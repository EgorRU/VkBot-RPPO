from turtle import *
from tkinter import *  
import turtle
from PIL import Image
#для установки необходимых библиотек вы можете использовать пакетный менеджер pip
#в командной строке необходимо выполнить команду "pip install <название модуля>"
#например, чтобы установить PIL, потребуется команда pip install Pillow

c = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
t = Pen()
s = 30
bgcolor('black')
t.pencolor('green')
t.write("Цифровые", align = "center", font = ("Comic Sans MS", 80, "normal"))
t.penup()
t.forward(-100)
t.right(90)
t.forward(120)
t.pendown()
t.write("кафедры", font = ("Comic Sans MS", 80, "normal"))
t.penup()
t.forward(80)
t.right(90)
t.forward(175)
for i in range(168):
	t.pendown()
	t.pencolor(c[i % 6])
	t.width(i / 100 + 1)
	t.forward(i)
	t.left(61)
	t.speed(20)

turtle.forward(100)
ts = turtle.getscreen()
ts.getcanvas().postscript(file = "logo.eps")
#если при выполнении следующих инструкций на вашей конфигурации возникнут ошибки, вероятно,
#у вас есть проблемы со шрифтами ghostscript. В таком случае вы получите только векторное
#изображение в формате eps.
im = Image.open("logo.eps")
im.save("logo.jpg", "JPEG")