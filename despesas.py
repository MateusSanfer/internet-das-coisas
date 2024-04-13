#Alunos: Artur Brasil, Mateus Fernandes

import customtkinter as ctkn
from tkinter import messagebox

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('green')

#Funções
def botao():  
    recei = int(receita.get())
    recei2 = int(receita1.get())
    desp = int(despesa.get())
    desp1 = int(despesa1.get())
    desp2 = int(despesa2.get())
    desp3 = int(despesa3.get())
    
    receitas1 = recei+recei2
    despesas1 = desp+desp1+desp2+desp3
    
    calculo = receitas1-despesas1
    
    resultado.configure(text=f'Valor restante R$: {calculo:.2f}')
#----------------------------------------------------------

janela = ctkn.CTk()
janela.geometry('400x500')
janela.title('Sistema Orçamento Financeiro')

texto = ctkn.CTkLabel(janela, text='Aplicativo para calcular Orçamento Financeiro', font= ('Arial', 16, 'bold'))
texto.pack(padx= 5, pady=10)

receitas = ctkn.CTkLabel(janela, text='Receitas',font= ('Arial', 16, 'bold'))
receitas.pack(pady=5)

receita = ctkn.CTkEntry(janela, placeholder_text='Digite a receita mensal', width=250)
receita.pack(padx= 10, pady=10)

receita1 = ctkn.CTkEntry(janela, placeholder_text='Outras receitas', width=250)
receita1.pack(padx= 10, pady=10)

despesas = ctkn.CTkLabel(janela, text='Despesa',font= ('Arial', 16, 'bold'))
despesas.pack(pady=5)

despesa = ctkn.CTkEntry(janela, placeholder_text='Digite a despesa mensal', width=250)
despesa.pack(padx=10, pady=10)

despesa1 = ctkn.CTkEntry(janela, placeholder_text='Digite a despesa mensal', width=250)
despesa1.pack(padx=10, pady=10)

despesa2 = ctkn.CTkEntry(janela, placeholder_text='Digite a despesa mensal', width=250)
despesa2.pack(padx=10, pady=10)

despesa3 = ctkn.CTkEntry(janela, placeholder_text='Digite a despesa mensal', width=250)
despesa3.pack(padx=10, pady=10)

calculo = ctkn.CTkLabel(janela, text='', font=('Arial', 10,'bold'))

botao1 = ctkn.CTkButton(janela, text="clique",fg_color='darkgreen', hover_color='gray', command=botao)
botao1.pack(padx=10, pady=10)

resultado = ctkn.CTkLabel(janela, text='')
resultado.pack(padx=10, pady=10)

janela.mainloop()