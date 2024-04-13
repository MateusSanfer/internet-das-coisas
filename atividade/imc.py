import customtkinter as ctkn

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('green')

def calcular():
    n = str(cx_nome.get())
    p = float(cx_peso.get())
    a = float(cx_altura.get())
    imc = p/(a * a)
 
    
    if(imc <= 16.9):
        situacao = 'Muito abaixo do peso'
    elif imc >= 17 and imc <= 18.4:
        situacao = 'Abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        situacao = 'Peso normal'
    elif imc >= 25 and imc <= 29.9:
        situacao = 'Acima do peso'
    elif imc >= 30 and imc <= 34.9:
        situacao = 'Obsidade grau I'
    elif imc >= 35 and imc <= 39.9:
        situacao = 'Obsidade grau II'
    else:
        situacao = 'Obsidade Grau III'
    resultado.configure(text=f'{n} seu IMC é {imc:.2f} \n você está {situacao}')

janela = ctkn.CTk()
janela.geometry('550x400')
janela.title('Calculadora IMC')
janela.iconbitmap('python/cov.ico')

nome = ctkn.CTkLabel(janela, text='Nome', font=('arial', 20, 'bold'))
nome.place(x=15, y=10)

cx_nome = ctkn.CTkEntry(janela, placeholder_text='Digite o consumo da viagem', width=200, height=40, fg_color='white',text_color='black', placeholder_text_color='gray', font=('Times New Roman', 15))
cx_nome.place(x=15, y=40)

peso = ctkn.CTkLabel(janela, text='Peso',font=('arial', 20, 'bold'))
peso.place(x=15, y=80)

cx_peso = ctkn.CTkEntry(janela, placeholder_text='Digite o consumo da viagem', width=200, height=40, fg_color='white',text_color='black', placeholder_text_color='gray', font=('Times New Roman', 15))
cx_peso.place(x=15, y=110) 

altura = ctkn.CTkLabel(janela, text='Altura',font=('arial', 20, 'bold'))
altura.place(x=15, y=150)

cx_altura = ctkn.CTkEntry(janela, placeholder_text='Digite o consumo da viagem', width=200, height=40, fg_color='white',text_color='black', placeholder_text_color='gray', font=('Times New Roman', 15))
cx_altura.place(x=15, y=180)

botao = ctkn.CTkButton(janela, text='Calcular viagem', font=('verdana', 20, 'bold'), fg_color='darkgreen', hover_color='#5298de', height=50, command=calcular)
botao.place(x=15, y=240)

resultado = ctkn.CTkLabel(janela, text='', text_color='yellow', font=('verdana', 16, 'bold'), width=200, height=40)
resultado.place(x=220, y=80)
janela.mainloop()
