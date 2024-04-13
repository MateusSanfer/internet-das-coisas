import customtkinter as ctkn

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('green')

janela = ctkn.CTk()
janela.geometry('550x400')
janela.iconbitmap('icon.ico')
janela.title('Combustível APP 2024')

# Funções

def calcular():
    d = float(distacia.get())
    c = float(consumo.get())
    p = float(preco.get())
    
    valor = (d/c)*p
    resultado.configure(text=f'O gasto total da viagem foi R$ {valor:.2f}')
    
    
    

texto = ctkn.CTkLabel(janela, text="APP Calcular consumo em Viagem", text_color='white', font=("Arial", 20, 'bold'))
texto.pack(padx=10, pady=10)

distacia = ctkn.CTkEntry(janela, placeholder_text='Digite a distância', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray')
distacia.pack(padx=10, pady=10)

consumo = ctkn.CTkEntry(janela, placeholder_text='Digite o consumo da viagem', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray', font=('Times New Roman', 15))
consumo.pack(padx=10, pady=10)

preco = ctkn.CTkEntry(janela, placeholder_text='Digite o preço', width=300, height=40, fg_color='white',text_color='black', placeholder_text_color='gray', font=('Times New Roman', 15))
preco.pack(padx=10, pady=10)

botao = ctkn.CTkButton(janela, text='Calcular viagem', font=('verdana', 20, 'bold'), fg_color='darkgreen', hover_color='#5298de', height=50, command=calcular)
botao.pack(padx=10, pady=10)

resultado = ctkn.CTkLabel(janela, text='', text_color='yellow', font=('verdana', 18, 'bold'), width=300, height=40)

resultado.pack(padx=10, pady=10)

janela.mainloop()