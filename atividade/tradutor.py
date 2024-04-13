import customtkinter as ctkn
from deep_translator import GoogleTranslator

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('blue')

# Funções ---------------

def traduzir():
    texto_para_traduzir = user_text.get()
    linguagem = lang_to_var.get()
    
    resultado = GoogleTranslator(source='auto', target=linguagem).translate(texto_para_traduzir)
    
    translated_text.configure(state='normal')
    translated_text.delete(0,'end')
    translated_text.insert(0, resultado)
#------------------------
janela = ctkn.CTk()
janela.minsize(500, 400)
janela.maxsize(600, 400)
janela.title('Tradutor Universal V1.0')
# janela.iconbitmap('python/cov.ico')

ctkn.CTkLabel(janela, text= 'Tradutor  Universal V1.0', font=('Arial', 25, 'bold') , text_color='green').pack(anchor=ctkn.CENTER, pady=5)

app_frame = ctkn.CTkFrame(janela, width=500, height=500, fg_color='transparent')
app_frame.pack(fill=ctkn.X, padx=20, pady=10)

ctkn.CTkLabel(app_frame, text='Texto para traduzir🕺🤾', font=('arial', 18 ,'bold')).pack(fill=ctkn.X)

user_text = ctkn.CTkEntry(app_frame, placeholder_text='Digite o texto para traduzir', height=50)
user_text.pack(fill=ctkn.X)

ctkn.CTkLabel(app_frame, text='Escolha o idioma a traduzir 😒👌').pack(pady=5)

lang_to_var = ctkn.StringVar(value='english')

lang_list = GoogleTranslator().get_supported_languages()

lang_to = ctkn.CTkOptionMenu(app_frame, values=lang_list, variable=lang_to_var, dropdown_hover_color='#0c8f94')
lang_to.set('english')
lang_to.pack(pady=5)

ctkn.CTkLabel(app_frame, text='Texto traduzido🌪️', font=('Arial', 18 ,'bold')).pack(fill=ctkn.X)

translated_text = ctkn.CTkEntry(app_frame, placeholder_text='O texto traduzido será mostrado aqui', height=100, placeholder_text_color='gray')
translated_text.pack(fill=ctkn.X)

translated_btn = ctkn.CTkButton(app_frame, text='Traduza', font=('Arial', 14, 'bold'), command=traduzir)
translated_btn.pack(fill=ctkn.X, pady=20)

janela.mainloop()
