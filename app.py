# libraries

import pywhatkit
import keyboard
import time
import datetime
from datetime import datetime

# contact

contato = ['+5511970714099']

# message (it may take a few minutes to be sent)

pywhatkit.sendwhatmsg(contato[0], 'Hello! This message was sent by a bot! 🤖',datetime.now().hour, datetime.now().minute + 2)
del contato[0]
time.sleep(60)
keyboard.press_and_release('ctrl + w')

# before testing, keep WhatsApp Web openin your brownser
