#!/bin/python3
#PasswordMaker
#MrBurnt
import random
from colorama import Fore,init
import os
from time import sleep 

os.system('clear')

#Colors
init()
c1 = Fore.WHITE
c2 = Fore.GREEN
c3 = Fore.CYAN
c4 = Fore.RED
c5 = Fore.YELLOW
c6 = Fore.MAGENTA
c7 = Fore.BLUE
c8 = Fore.LIGHTBLACK_EX

def bio():
	print(c5+f"""

                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 	
                  ▇▇▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 
                 
                       {c2}MasterBurnt
                      {c1}t.me/TheBurnt
                    {c4}PasswordListMaker
                 
        {c3}The probability of having the password 
        you want in the list password is +90%!!
        
                                                
{c1}[1]{c2}Create List Password 
{c1}[0]{c2}Exit
""")

bio()
			
while 1:
    bet = input(f"{c1}[?]{c8}Select an option to continue 1 or 0 ×>{c1} ")
    if bet == '1':
        break 
    elif bet == '0':
        print(c7+'Best wishes')
        sleep(2)
        os.system('clear')
        exit(0)
    else:
        print(c1+f'[!]{c5}You have only two options {c4}build {c5}or{c4} Exit')
        sleep(1.5)
        os.system('clear')
        bio()
def banner():
    os.system('clear')
    print(c6+f"""
     ____                __  __       _
     |  _ \ __ _ ___ ___|  \/  | __ _| | _____ _ __
     | |_) / _` / __/ __| |\/| |/ _` | |/ / _ \ '__|
     |  __/ (_| \__ \__ \ |  | | (_| |   <  __/ |
     |_|   \__,_|___/___/_|  |_|\__,_|_|\_\___|_|      
             
              {c3} 
      {c3}Provide Available Information Of The {c4}Target!
                {c4}Enter {c3}to get the output""")
banner()


list1 = [] 
out =[]

status = 1
print(c8+"\tIdentify 10 items of target information!")
for x in range(1,11):    
    list = input(c2+f"""
┌─[root ~@Word]
└──╼ {c5}""")
    list1.append(list)
    if list =="": 
        break 
    else:
       continue 
os.system('clear')     
print(c4+f"""

                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 	
                  ▇▇▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 
                 
             {c3}Please{c4} Wait{c3} may take a while =) """)       
for i in range(1,20001):
            out1 = random.choice(list1) 
            out2 = random.choice(list1) 
            out3 = random.choice(list1) 
            out4 = random.choice(list1) 
            out5 = random.choice(list1)
            a = str(out1)+str(out2) 
            b = str(out1)+str(out2)+str(out3) 
            c = str(out1)+str(out2)+str(out3)+str(out4)
            d = str(out1)+str(out2)+str(out3)+str(out4)+str(out5) 
            
            if a not in out:
                out.append(a)
            elif b not in out:
                out.append(b)
            elif c not in out:
                out.append(c)
            elif d not in out:
                out.append(d)
            else:
                pass
os.system('clear')              
file_name = input(c4+f"""

                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 	
                  ▇▇▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 
                 
   {c3}   Enter file name to save{c4}  example ~>{c2} PassList \n
┌─[root ~@FileName]
└──╼ {c5}""")

 
#SaveFile              
f = open(file_name+'.txt', 'a')
for hit in out:
    f.write(hit+'\n') 
f.close()
os.system('clear')
print(c2+f"""

                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 	
                  ▇▇▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇▇▇▇ 
                  ▇▇▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇▇▇▇ 
                  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 
                 
{c3}\n\t\t     Saved as {c4}{file_name}.txt""")
sleep(3)
os.system('clear')
