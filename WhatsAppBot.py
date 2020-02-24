from selenium import webdriver
import time 

class whatsappbot:
    def __init__(self):
        self.mensagem = " Bom dia pessoal, vejam o que esse bot de automaçao pode fazer"
        self.grupos = ["ROANA Academy","Roana"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
    
    def EnviarMensagens(self):