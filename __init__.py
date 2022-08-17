from apiTrello import trello

APITrello = trello()
a = str(APITrello.getCards())

values = ''.join(map(str, a))
print(f'\n{values}\n')
print('*a'*100)
print(values)
print('*mmm'*100)
dic1 = values
dic2 = str(values)
dic3 = eval(dic2)
print(dic3)

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

contatos=['INSERT NUMBERS OR NAMES THE GROUPS']
mensagem = 'ID -> ', dic3['id'], '\n', 'NOME DO CARD -> ', dic3['name']
#função responsável para fazer a busca dos contatos
def buscar_contato(contato):
    campo_pesquisa=driver.find_element(by=By.XPATH, value='//div[contains(@class,"INSERT CLASS")]') #FORMATO NOVO DO SELENIUM 4.3
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#função responsável para fazer o envio da mensagem
def enviarmensagem(mensagem):
    campo_mensagem=driver.find_element(by=By.XPATH, value='//div[contains(@class, "INSERT CLASS")]')
    campo_mensagem.click()
    time.sleep(3)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)
    
for contato in contatos:
    buscar_contato(contato)
    enviarmensagem(mensagem)

time.sleep(20) #fechará o navegador utilizado em 20 segundos
pyautogui.hotkey('ctrl', 'w')