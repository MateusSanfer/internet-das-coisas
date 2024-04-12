import customtkinter as ctkn
from tkinter import messagebox

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('blue')

janela = ctkn.CTk()
janela.geometry('500x350')
janela.title('APP Posto Gasolina')
janela.iconbitmap('dist/icon.ico')

def Calcpedagio():
    d = float(distanciaP.get())
    t = float(taxa.get())

    total = d * t

    resultadoP.configure(text=f'O gasto total de pedagio foi R$ {total:.2f}')
def calcular():
    d = float(distancia.get())
    c = float(consumo.get())
    p = float(preco.get())

    valor = (d/c)*p
    resultado.configure(text=f'O gasto total da viagem foi R$ {valor:.2f}')

    # LAMBDA é uma palavra-chave usada para criar funções anônimas, ou seja,
    # funções que não têm um nome específico associado a elas. As funções lambda são
    # úteis quando você precisa de uma função temporária e simples.
    janela.after(1500, lambda: messagebox.showinfo('Até a proxima', f'Obrigado por usar nosso serviço!'))

def mostrar_frame(frame):
    janela.raise_frame(frame)

texto = ctkn.CTkLabel(janela, text='APP Cálculo de consumo em viagem', text_color='white', font=('Arial', 20, 'bold'))
texto.pack(padx=10, pady=10)

distancia = ctkn.CTkEntry(janela, placeholder_text='Digite a distância', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray')
distancia.pack(padx=10, pady=10)

consumo = ctkn.CTkEntry(janela, placeholder_text='Digite o consumo da viagem', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray', font=('Times New Roman', 15))
consumo.pack(padx=10, pady=10)

preco = ctkn.CTkEntry(janela, placeholder_text='Digite o preço', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray', font=('Times New Roman', 15))
preco.pack(padx=10, pady=10)

botao = ctkn.CTkButton(janela, text='Calcular viagem', font=('verdana', 20, 'bold'), fg_color='#d96736', hover_color='#5298de', height=50, command=calcular)
botao.pack(padx=10, pady=10)
botaoProximo = ctkn.CTkButton(janela, text='Proximo', font=('verdana', 20, 'bold'), fg_color='#d96736', hover_color='#5298de', height=50, command=lambda: mostrar_frame(pedagio))
botaoProximo.pack(padx=10, pady=10)

resultado = ctkn.CTkLabel(janela, text='', text_color='yellow', font=('verdana', 18, 'bold'), width=300, height=40)
resultado.pack(padx=10, pady=10)

pedagio = ctkn.CTkFrame(janela)
pedagio.pack(fill='both', expand=True)

texto = ctkn.CTkLabel(pedagio, text='APP Cálculo de consumo em viagem', text_color='white', font=('Arial', 20, 'bold'))
texto.pack(padx=10, pady=10)

distanciaP = ctkn.CTkEntry(pedagio, placeholder_text='Digite a distância', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray')
distanciaP.pack(padx=10, pady=10)

taxa = ctkn.CTkEntry(pedagio, placeholder_text='Digite a distância', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray')
taxa.pack(padx=10, pady=10)

calc = ctkn.CTkButton(pedagio, text='Calcular viagem', font=('verdana', 20, 'bold'), fg_color='#d96736', hover_color='#5298de', height=50, command=Calcpedagio)
calc.pack(padx=10, pady=10)
botaoVoltar = ctkn.CTkButton(pedagio, text='Voltar', font=('verdana', 20, 'bold'), fg_color='#d96736', hover_color='#5298de', height=50, command=lambda: mostrar_frame(janela))
botaoVoltar.pack(padx=10, pady=10)

resultadoP = ctkn.CTkLabel(pedagio, text='', text_color='yellow', font=('verdana', 18, 'bold'), width=300, height=40)
resultadoP.pack(padx=10, pady=10)

janela.mainloop()