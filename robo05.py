import pyautogui as p


p.hotkey('win','r')
p.sleep(1)
p.write(r'C:\Users\aprde\Desktop\CursoRpaPython\RPA.pbix') #SyntaxError unicode error unicodeescape codec cant decode bytes in position 2 3  truncated UXXXXXXXX escape (Coloque o r)
p.sleep(1)
p.press('enter')
p.sleep(20)
p.click(x=712, y=104)
p.sleep(6)
p.click(x=1901, y=10)
p.sleep(3)
p.click(x=974, y=555)

#p.sleep(3)
#print(p.position())