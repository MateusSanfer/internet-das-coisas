from tkinter import *
from tkinter import ttk

# Cores

cor1 = "#3b3b3b"  #preta
cor2 = "#feffff"  #white
cor3 = "#38576b"  #blue charge
cor4 = "#ECEFF1"  # gray
cor5 = "#FFAB40"  #Orange

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13q bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4)
b_2.place(x=90, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4)
b_4.place(x=0, y=50)
b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4)
b_4.place(x=45, y=50)
b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4)
b_4.place(x=90, y=50)
b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4)
b_4.place(x=140, y=50)


janela.mainloop()