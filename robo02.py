import rpa as r
import pyautogui as p

r.init()
r.url('https://www.google.com.br')
janela = p.getActiveWindow()
janela.maximize()
r.wait(2.0)
r.type('//*[@name="q"]', 'RPA[enter]')
r.wait(2.0)
r.snap('page','rpa_page.png')
r.wait(2.0)
r.close()