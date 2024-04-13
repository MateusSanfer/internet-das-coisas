# import tkinter

# janela = tkinter.Tk()
# janela.geometry('400x300')
# janela.title("Jaca")

# def ola():
#     print('Oi tudo bem! ')
   

# titulo = tkinter.Label(janela, text='Bem vindo ao APP! ')
# titulo.pack(padx=10, pady=10)
# botao = tkinter.Button(janela, text='Calcular', command=ola)
# botao.pack(padx=10, pady=10)

# janela.mainloop()

import customtkinter as ctkn # as para passar

ctkn.set_appearance_mode('dark')
def Clique():
    print('Vaca')

janela = ctkn.CTk()
janela.title("Já vai!")
janela.geometry('400x300')

titulo = ctkn.CTkLabel(janela, text="Bem vindo ao App!", text_color="red", font=('verdana', 28))
titulo.pack(padx=10, pady=10)

senha =  ctkn.CTkEntry(janela, placeholder_text="Digite seu Login", width=250)
senha.pack(padx=10, pady=10)

senha =  ctkn.CTkEntry(janela, placeholder_text="Digite sua senha", width=250, show='•')
senha.pack(padx=10, pady=10)


botao = ctkn.CTkButton(janela, text= "Entrar", command=Clique)
botao.pack(padx=10, pady=10)



janela.mainloop()