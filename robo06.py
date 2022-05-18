import rpa as r
import pyautogui as p
import pandas as pd
import os as o

r.init()
r.url('https://rpachallengeocr.azurewebsites.net/')
janela = p.getActiveWindow() #maximizar janela
janela.maximize()
p.sleep(8)
conta_pagina =1 
while conta_pagina <= 3: # Enquanto o contador for menor que   3 execute abaixo:
    if conta_pagina == 1: #se o contador for igual a 1
        r.table('//*[@id="tableSandbox"]','Temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=True)# imprimia com o cabecalho
        r.click('//*[@id="tableSandbox_next"]')
        conta_pagina = conta_pagina + 1
    else:                                                 #senão
        r.table('//*[@id="tableSandbox"]','Temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=False) # pode impimir sem o cabecalho
        r.click('//*[@id="tableSandbox_next"]')
        conta_pagina = conta_pagina + 1

r.close()
o.remove('Temp.csv') # removendo arquivo temporario
csv_xlsx = pd.read_csv(r'WebTable.csv') # tranformando o csv em excel
csv_xlsx.to_excel(r'WebTable02.xlsx')