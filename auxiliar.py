import pyautogui
import time
import pandas

time.sleep(5)
print(pyautogui.position())

# pyautogui.scroll(50000)


tabela = pandas.read_csv("produtos.csv")
print(tabela)
