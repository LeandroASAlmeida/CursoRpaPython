import  rpa as r
import pyautogui as p
import pandas as pd

r.init()
r.url('https://rpachallenge.com') # abrir navegador, site e maximizar.
janela = p.getActiveWindow()
janela.maximize()
p.sleep(10)


cont = 0
downloadExcel = None                                                # como achar e clicar em certo campo pelo print do campo. FACIL
while (downloadExcel == None) and (cont < 20):
    downloadExcel = p.locateCenterOnScreen('C:\\Users\\aprde\\Desktop\\CursoRpaPython\\downloadExcel.png', confidence=0.9) # donwload do excel
    p.sleep(1)
    cont += 1
if (downloadExcel != None):
    p.click(downloadExcel)

p.sleep(1)

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1') # pegar o arquivo , e o cabecalho dele
df = pd.DataFrame(dados, columns=["First Name",	"Last Name ", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])

r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')  #clique no start * lembrar de ja deixar tudo pronto abaixo antes. # ESSE CLIQUE DEVE SER FEITO POR ULTIMO

for row in df.itertuples(): # para cada coluna pegar os dados e transformar em uma tupla.
    r.type('//*[@ng-reflect-name="labelFirstName"]',row[1]) # pegar as info da primeira coluna , no html pegar a tag ng-reflect-name="labelFirstName  e colocar ela dentro de //*[@ tag ]
    r.type('//*[@ng-reflect-name="labelLastName"]',row[2])
    r.type('//*[@ng-reflect-name="labelCompanyName"]',row[3])
    r.type('//*[@ng-reflect-name="labelRole"]',row[4])
    r.type('//*[@ng-reflect-name="labelAddress"]',row[5])  # ira preencher até acabar , não precisa por contador pois o próprio site tem um limite de 10 paginas para preencher
    r.type('//*[@ng-reflect-name="labelEmail"]',row[6])
    r.type('//*[@ng-reflect-name="labelPhone"]',str(row[7]))
    r.click('/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
p.sleep(3)
p.screenshot('score.png') # tira print no final e salva na pasta
r.close()