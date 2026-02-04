import time
import os

def clear_screen():
    print("\033[H\033[J", end="")

def wait_for_space():
        while True:
            if input("\nPress SPACE then Enter to continue... ") == " ":
                return

print('''
      
88                                                   
88                                            ,d     
88                                            88     
88,dPPYba,   ,adPPYba, ,adPPYYba, ,adPPYba, MM88MMM  
88P'    "8a a8P_____88 ""     `Y8 I8[    ""   88     
88       d8 8PP""""""" ,adPPPPP88  `"Y8ba,    88     
88b,   ,a8" "8b,   ,aa 88,    ,88 aa    ]8I   88,    
8Y"Ybbd8"'   `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'   "Y888  

               
   ,o0MMMMMMMMNMMMMM8888888888888888MMMMMM.88
  8888888888V'.o   """VoooooooooV"""   o. V8
  8888LLLLl:  O , ,O    ``VlV''    O,  ,O  D88,
   8888888LLb `VooV',O.WooA AooW.O `VooV' '8888
    8888888888booooooOlllllIlllllOoooooood8888
      
''')

wait_for_space()
time.sleep(2)
clear_screen()

print("After a long period of work you decided to take some time off and went on a cruise to travel the world.")
wait_for_space()
clear_screen()

print("The cruise will go from the Netherlands over the atlantic ocean and is headed towards Guyana in Southamerica.")
wait_for_space()
clear_screen()

print("While you're in the cabins .")
wait_for_space()
clear_screen()