#estou importando o pyatogui e apilidando ele de aut
import pyautogui as aut
#pressiono a tecla de atalho
aut.hotkey('win')
#espera 1 segundo
aut.sleep(1)
#entrando no navegador
aut.write('chrome', interval=0.1)
aut.press('Enter')
aut.sleep(0.7)
#digitei o url do video que quero por
aut.write('https://youtu.be/LJAUzKGVX2I?si=MXQ_7b9pZ54GTN_O')
aut.press('Enter')
aut.sleep(0.7)
aut.press("f")