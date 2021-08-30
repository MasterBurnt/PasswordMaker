import os
import random
from concurrent.futures import ThreadPoolExecutor

os.system('clear')

#Colors
c1 = '\033[0m' #white
c2 = '\033[92m' #green
c3 = '\033[96m' #cyan
c4 = '\033[91m' #red
c5 = '\033[93m' #yellow 
c6 = '\033[94m' #blue

list = [] 
out =[]

print(c1+f"""  
             
      ____                __  __       _   
      |  _ \ __ _ ___ ___|  \/  | __ _| | _____ _ __
      | |_) / _` / __/ __| |\/| |/ _` | |/ / _ \ '__|
      |  __/ (_| \__ \__ \ |  | | (_| |   <  __/ |
      |_|   \__,_|___/___/_|  |_|\__,_|_|\_\___|_|      
                         {c6}ᵐᵃˢᵗᵉʳvᵇᵘʳⁿᵗ 
      
      {c5}Provide Available {c4}Information{c5} Of The Target!
           You Can {c4}'Enter'{c5} to get the output
              """)
for x in range(1,101):    
    i = input(c2+f"""
┌─[root ~@Word]
└──╼ {c1}""")
    list.append(i)
    if i == "": 
        break 
    else:
       continue        
      
def task():
    for i in range(1,50):
            out1 = random.choice(list) 
            out2 = random.choice(list) 
            out3 = random.choice(list) 
            out4 = random.choice(list) 
            out5 = random.choice(list)
            a = str(out1)+str(out2) 
            b = str(out1)+str(out2)+str(out3) 
            c = str(out1)+str(out2)+str(out3)+str(out4)
            d = str(out1)+str(out2)+str(out3)+str(out4)+str(out5)
            if a not in out and len(a) >= 4:
                out.append(a)
            elif b not in out and len(b) >= 4:
                out.append(b)
            elif c not in out and len(c) >= 4:
                out.append(c)
            elif d not in out and len(d) >= 4:
                out.append(d)
            else:
                pass
                


def main():
 with ThreadPoolExecutor(max_workers=30) as executor:
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)
   future = executor.submit(task)

os.system('clear') 
main()
file = input(c2+f'Select The File Name To Save :{c1} ')

f = open(f'{file}.txt', 'a')
for hit in out:
    f.write(hit+'\n')
f.close()         
print(c2+f'Number : {c1}{len(out)}\n{c2}Saved as : {c1}{file}.txt')  



