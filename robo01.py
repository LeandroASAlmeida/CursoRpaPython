import pyautogui as p               #importando a biblioteca e chamando a de "p"

#p.sleep(2)
#print(p.position())

#p.moveTo(x=101, y=138, duration=1)

#p.click(x=101, y=138)

def bot01():

    p.hotkey('win','r')
    p.sleep(1)
    p.typewrite('notepad')
    p.sleep(2)
    p.press('enter')
    p.sleep(2)

    p.typewrite('OI!!, eu sou um bOt ^^')
    p.sleep(2)
    valor = p.getActiveWindow()
    valor.close()
    p.press('right')
    p.sleep(2)
    p.press('right')
    p.sleep(2)
    p.press('enter')
    p.FAILSAFE = False   ### no modulo de schedule tem que colocar esse parametro.

