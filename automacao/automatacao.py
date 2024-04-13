import openpyxl
from docxtpl import DocxTemplate
import datetime

# Excel

caminho = 'automacao/student_data.xlsx' # Busca o arquivo
pasta_trabalho = openpyxl.load_workbook(caminho) # Abre o arquivo
sheet = pasta_trabalho.active # Define qual a aba

lista_valores = list(sheet.values)
print(lista_valores)

#word

doc = DocxTemplate('automacao/certificate.docx')

for x in lista_valores[1:]:
    doc.render({
        'nome':x[0],
        'curso':x[1],
        'data':x[2].strftime('%d/%m/%Y'),
        'instrutor':x[3]
    })
    doc_nome = f'Certificado {x[0]}.docx'
    doc.save(doc_nome)