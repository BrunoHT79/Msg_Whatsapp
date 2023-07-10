import pywhatkit as pwk 
import keyboard 
import time 
from datetime import datetime

contatos = #inserir os contatos a enviar a msg#

while len(contatos) >= 1: 
  pwk.sendwhatmsg(contatos[0],'#Inserir a msg a enviar#', datetime.now().hour, datetime.now().minute+1) 
  del contatos[0] 
  time.sleep(30) 
  keyboard.press_and_release('enter') 
  time.sleep(30) 
  keyboard.press_and_release('ctrl + w') 
  keyboard.press_and_release('enter')
