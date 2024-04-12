import os
from tkinter import PhotoImage, Label, messagebox, filedialog
import customtkinter as ctkn
import qrcode
from PIL import Image

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('blue')

janela = ctkn.CTk()
janela.title('QRCode Generator')
janela.minsize(600, 620)
janela.maxsize(700,620)
# janela.iconbitmap('icon.ico')

    
def gerador():
    global img
    nomeArquivo_texto = nomeArquivo.get()
    nome_texto = textoQr.get()
    # Gerando a imagem do QR Code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(nome_texto)
    qr.make()
    img = qr.make_image()
    img.save('' + str(nomeArquivo_texto) + '.png')
  
    # Redimensionar a imagem
    img = Image.open('' + str(nomeArquivo_texto) + '.png')
    new_size = (int(janela.winfo_width() * 0.5), int(janela.winfo_height() * 0.5))
    img = img.resize(new_size)
    img.save('/' + str(nomeArquivo_texto) + '.png')
    
    
    global image
    image = PhotoImage(file='' + str(nomeArquivo_texto) + '.png')
    image_view.config(image=image)
    image_view.image = image #   # Mantém uma referência para evitar a limpeza de memória

def salvar():
    filepath = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG files', '*.png')],
        title='Salvar QR Code como...')
    
    if filepath:
        try:
            img.save(filepath)
            messagebox.showinfo('Sucesso', 'QR Code salvo com sucesso!')
        except Exception as e:
            messagebox.showerror('Erro', f'Ocorreu um erro ao salvar o QR Code: {e}')

ctkn.CTkLabel(janela, text="Mateus Sanfer e Emanuel Santos", font=("verdana", 15, 'bold'), text_color="#9ea3a0", fg_color='transparent').pack(side='bottom', pady=10)

image_view = Label(janela)
image_view.pack(padx=10, pady=20, side='bottom')
# place(x=155, y=220)

titulo = ctkn.CTkLabel(janela, text='Gere seu QRCode', text_color='white', font=('verdana', 20, 'bold'))
titulo.pack(padx=10, pady=10)

nomeArquivo = ctkn.CTkEntry(janela, placeholder_text='Nome do arquivo', width=400, height=4)
nomeArquivo.pack(padx=10, pady=10)

textoQr = ctkn.CTkEntry(janela, placeholder_text='Digite o texto para gerar o QRCode', width=400, height=4)
textoQr.pack(padx=10, pady=10)

botao1 = ctkn.CTkButton(janela, text='Gerar', font=('verdana', 20, 'bold'), width=80, height=40, command=gerador)
botao1.place(x=173, y=142)

botao2 = ctkn.CTkButton(janela, text='Salvar', font=('verdana', 20, 'bold'), width=80, height=40, command=salvar)
botao2.place(x=343, y=142)



janela.mainloop()