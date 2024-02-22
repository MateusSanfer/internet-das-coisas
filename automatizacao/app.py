import openpyxl
import pyperclip
import pyautogui
from time import sleep

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

for linha in sheet_produtos.iter_rows(min_row=2):
  nome_produto = linha[0].value
  pyperclip.copy(nome_produto)
  pyautogui.click(1399,364, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  descricao = linha[1].value
  pyperclip.copy(descricao)
  pyautogui.click(1365,447, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  
  categoria = linha[2].value
  pyperclip.copy(categoria)
  pyautogui.click(1370,588, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  codigo_produto = linha[3].value
  pyperclip.copy(codigo_produto)
  pyautogui.click(1380,675, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  peso = linha[4].value
  pyperclip.copy(peso)
  pyautogui.click(1451,757, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  dimensoes = linha[5].value
  pyperclip.copy(dimensoes)
  pyautogui.click(1366,844, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  pyautogui.click(1396,912, duration=1)
  sleep(3)
  
  preco = linha[6].value
  pyperclip.copy(preco)
  pyautogui.click(1391,390, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  quantidade_em_estoque = linha[7].value
  pyperclip.copy(quantidade_em_estoque)
  pyautogui.click(1447,479, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  data_de_validade = linha[8].value
  pyperclip.copy(data_de_validade)
  pyautogui.click(1361,563, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  cor = linha[9].value
  pyperclip.copy(cor)
  pyautogui.click(1385,645, duration=1)
  pyautogui.hotkey('ctrl', 'v')
  
  tamanho= linha[10].value
  pyautogui.click(1418,727, duration=1)
  if tamanho == 'Pequeno':
    pyautogui.click(1364,752, duration=1)
  elif tamanho == 'Médio':
    pyautogui.click(1381,786, duration=1)
  else:
    pyautogui.click(1385,808, duration=1)
  
  
  material = linha[11].value
  pyperclip.copy(material)
  pyautogui.click(1378,816,duration=1)
  pyautogui.hotkey('ctrl','v')
  
  pyautogui.click(1383,874, duration=1)
  sleep(2)
  
  fabricante = linha[12].value
  pyperclip.copy(fabricante)
  pyautogui.click(1359,405,duration=1)
  pyautogui.hotkey('ctrl','v')
  
  pais_origem = linha[13].value
  pyperclip.copy(pais_origem)
  pyautogui.click(1362,487,duration=1)
  pyautogui.hotkey('ctrl','v')
  
  observacoes = linha[14].value
  pyperclip.copy(observacoes)
  pyautogui.click(1364,579,duration=1)
  pyautogui.hotkey('ctrl','v')
  
  codigo_de_barras = linha[15].value
  pyperclip.copy(codigo_de_barras)
  pyautogui.click(1368,714,duration=1)
  pyautogui.hotkey('ctrl','v')
  
  localizacao_armazem = linha[16].value
  pyperclip.copy(localizacao_armazem)
  pyautogui.click(1367,800,duration=1)
  pyautogui.hotkey('ctrl','v')
  
  pyautogui.click(1385,860, duration=1)
  
  pyautogui.click(1771,189, duration=1)
  
  pyautogui.click(1608,625, duration=1)
  
  