# Aula 1 - Automação de tarefas com pyautogui
# Criar passo a passo do projeto
# Passo 1: Entrar no sistema da da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos

# instalalar as bibliotecas 
# pip install pyautogui
import pyautogui
import time

# pyautogui.click -> clicar  com mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)
# pyautogui.press("win")

pyautogui.PAUSE = 1

# abrir o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar o site carrega
time.sleep(4)

#passo 2 fazer login
#pyautogui.click(x=425, y=394)  # clicar no campo e-mail
pyautogui.press("tab")   # passar para campo email
pyautogui.write("teste@teste.com")
pyautogui.press("tab")   # passar para campo senha
pyautogui.write("senha")
pyautogui.press("tab")  # passar para botão senha
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de dados de produtos
# pandas - manipulador de banco de dados
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# repetição de todos dados da tabela
for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto
    #pyautogui.press("tab")   # passar para campo Codigo
    pyautogui.click(x=407, y=278)
    codigo = tabela.loc[linha,"codigo"]

    #preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
   
    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    # retornar ao topo da tela
    pyautogui.scroll(50000)
