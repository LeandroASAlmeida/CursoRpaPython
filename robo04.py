import pyautogui as p

#p.sleep(2)        como conseguir a posição do item na tela X E Y
#print(p.position())

p.doubleClick(x=43, y=643)
p.sleep(4)
p.write('www.udemy.com')
p.press('enter')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(3)

#PESQUISAR , PRINTAR E SALVAR
local= p.locateOnScreen('Pesquisa.PNG', confidence= 0.9) #criar uma variavel para pegar a coordenada completa da imagem
localPesq= p.center(local) # criar outra variavel que vai pegar o centro da variavel anterior
xPesquisa,yPesquisa = localPesq
p.moveTo(xPesquisa,yPesquisa,duration=1)
p.click(xPesquisa,yPesquisa)
p.sleep(1)
p.write('Charles Lima')
p.press('enter')
p.sleep(3)
p.screenshot('cursos.png')
p.sleep(3)

#FECHAR A JANELA
close= p.locateOnScreen('Close.PNG', confidence= 0.9) #criar uma variavel para pegar a coordenada completa da imagem
local_close= p.center(close) # criar outra variavel que vai pegar o centro da variavel anterior
xClose,yClose = local_close
p.moveTo(xClose,yClose,duration=1)
p.click(xClose,yClose)

#print(local_pesq)


