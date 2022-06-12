import requests, time, os
from colorama import Fore
os.system('title federal')
print(f'''\n 
            
                             

				███████╗███████╗██████╗ ███████╗██████╗  █████╗ ██╗     
				██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██║     
				█████╗  █████╗  ██║  ██║█████╗  ██████╔╝███████║██║     
				██╔══╝  ██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██╔══██║██║     
				██║     ███████╗██████╔╝███████╗██║  ██║██║  ██║███████╗
				╚═╝     ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                        
                                           federal#1337 {Fore.LIGHTBLUE_EX}+{Fore.RESET} https://grief.lol
				{Fore.LIGHTBLUE_EX}════════════════════════════════════════════════════════{Fore.RESET}''')

		
		
		
		


		
print(f"[{Fore.LIGHTBLACK_EX}>{Fore.RESET}] webhook link ")
link = input(" > ")
print(f"[{Fore.LIGHTBLACK_EX}>{Fore.RESET}] message you want to spam ")
message = input(" > ")
print(f"[{Fore.LIGHTBLACK_EX}>{Fore.RESET}] webhook name ")
name = input(" > ")

payload = {
  'content': message,
  'username': name
}

while True:
  try:
    time.sleep(0.5)
    r = requests.post(link, json=payload)
    f = open('log.txt', 'a+') 
    if 'You are being rate limited.' in r.text:
      f.write('Ratelimited\n')
    else:
      f.write(f"Spammed {message}\n")  
    f.close()
    if r.status_code == 204:
      print(f"[{Fore.LIGHTBLUE_EX}+{Fore.RESET}] message sent")
    else:
      print(f"[{Fore.RED}-{Fore.RESET}] ratelimited")
  except requests.exceptions.MissingSchema:
     print(f"[{Fore.RED}-{Fore.RESET}] not a real webhook, please try agaian");break