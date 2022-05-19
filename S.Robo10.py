from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

navegador=Chrome()
navegador.get("https://consultacnpj.com/cnpj/")
navegador.maximize_window()
t.sleep(3)

cnpjs = ["45997418000153", "72273196001090", "33000167000101"]

for cnpj in cnpjs: #  vai passar um por um  dos cnpjs da lista
    input= navegador.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div/div/div[2]/div/div/input') # xpath traz aspas duplas ,, muito cuidado com as aspas "" e ''
    input.clear()
    input.send_keys(cnpj)
    #input.send_keys(Keys.ENTER) - ESSE SITE DA ENTER AUTOMATICO, CASO PRECISASSE DAR ENTER TERIA QUE USAR ESSE METODO, IMPORTANDO O KEYS LA ENCIMA
    t.sleep(1)
    dados = navegador.find_element_by_xpath('//*[@id="company-data"]')
    with open(f'{str(cnpj)}.csv', 'w', encoding="utf-8") as csv:
        csv.write(dados.text)
    t.sleep(2)
navegador.quit()