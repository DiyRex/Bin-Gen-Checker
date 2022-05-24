import random
import time


name = """  

               ██████╗ ██╗███╗  ██╗      ██╗  ██╗
               ██╔══██╗██║████╗ ██║      ╚██╗██╔╝
               ██████╦╝██║██╔██╗██║█████╗ ╚███╔╝ 
               ██╔══██╗██║██║╚████║       ██╔██╗ 
               ██████╦╝██║██║  ███║      ██╔╝╚██╗
               ╚═════╝ ╚═╝╚═╝  ╚══╝      ╚═╝  ╚═╝

                 ---|| Bincode Generator ||---

                                 Script By -DiyRex- :)
"""

print(name, "\n")

print("""
        ----- Card Types -----

      [1]   Visa Card
      [2]   Master Card
      [3]   American Express

""")


print("...................................."+'\n')
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
crd_type = input(">>> Input Card Type : ")
print("")
count = input(">>> Enter Count : ")
print("")
save = input(">>> Do you want to save bincodes in text file ? (y/n) : ")
print("")


TR = open('Bincodes.txt','w')

        
    


for k in range (int(count)):
    bin = ''.join((random.choice(num) for i in range(5)))
    if (crd_type =="1"):
        data = "4" + bin
        print(data)
        if (save == "y"):
            TR.writelines(data + '\n')
        elif (save == "Y"):
            TR.writelines(data + '\n')
        else:
            pass 
    
    if (crd_type == "2"):
        data = "5" + bin
        print(data)
        if (save == "y"):
            TR.writelines(data + '\n')
        elif (save == "Y"):
            TR.writelines(data + '\n')
        else:
            pass
    
    if (crd_type == "3"):
        data = "3" + bin
        print(data)
        if (save == "y"):
            TR.writelines(data + '\n')
        elif (save == "Y"):
            TR.writelines(data + '\n')
        else:
            pass
    

