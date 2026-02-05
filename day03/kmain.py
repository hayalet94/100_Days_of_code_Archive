import time
import os

def clear_screen():
    print("\033[H\033[J", end="")

def wait_for_space():
        while True:
            if input("\n\n\n(Press SPACE then Enter to continue...)") == " ":
                return
'''
    ,o0MMMMMMMMNMMMMM8888888888888888MMMMMM.88
  8888888888V'.o      OOO      OOO     o. V8
  8888LLLLl:      O     O ___ O       O    D88,
   8888888LLb        \____OOOOOO____/       '8888
    8888888888booooooOlllllllllllOoooooood8888
      
    ,o0MMMMMMMMNMMMMM8888888888888888MMMMMM.88
  8888888888V'.o    OOO        OOO     o. V8
  8888LLLLl:     X     O  !!  O       X   D88,
   8888888LLb    \___OOOOOOOOOOOO___/    '8888
    8888888888booooooOlllllllllllOoooooood8888'''


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
time.sleep(1)
clear_screen()

print("\n\n\nAfter a long period of work you decided to take some time off and went on a cruiseship to travel the world.")
print("\n\nThe cruise will go from the Netherlands over the atlantic ocean and is headed towards Guyana in Southamerica.")
wait_for_space()
clear_screen()

print("\n\n\nWhile you're in the cabins to get some sleep you feel heavy rumbling and loud noises in the middle of the night and get out of your bed...")
print("\n\n...you hear screaming and open your door, people are panicking and the ship is tilting...")
wait_for_space()
clear_screen()

print("\n\n\n...You run down the hall and try to get outside, just as you reach the corner you hear a sharp hiss from a pipe when it suddenly bursts...")
print("\n\n...for a split-second you have a tinnitus and then everything turned white, you fainted...")
wait_for_space()
clear_screen()

print("\n\n\nWhen you finally wake up, you cough up loads of water and appear to be at a beach, next to debris from the cruisheship you were on.")

print("""\n\n
                    #####
                   #### = =
                   ##C    >
                    _)' _( .' ,
                 __/ |_/\   " *. o
                /` \_\ \/     %`= '_  .
               /  )   \/|      .^',*. ,
              /' /-   o/       - " % '_
             /\_/     <       = , ^ ~ .
             )_o|----'|          .`  '
         ___// (_  -   (
        ///-(  #\_ \   \ 
    """
)
wait_for_space()
clear_screen()

print("\n\n\nIt looks like there is noone else than you...")
print("\n\nYou walk down the beach trying to find someone else or any signs of society...")
wait_for_space()
clear_screen()


print("\n\n\nAfter what feels like hours of walking you suddenly spot MASSIVE footprints in the wet sand...")
print("""
\n\n
                          .----.
                 ______.  |    | 
   _ _ _      _o'       \ `----'
  o     `-- -'           o .---. 
  o                      o `---' 
  o                      o .--.
  o                      o `--'
  o      __ _            o .--.
   - - -'    ` -o_      /  `--'
                  `----' .--.
                         `--''
                         
        """
            )
wait_for_space()
clear_screen()


print("\n\n\nWhat do you want to do?")
choice1 = input("\n\n(Type Follow/Avoid/Cover Tracks) ").lower()

if choice1 == "follow":
    clear_screen()
    print("\n\n\nYou follow the tracks and find a torn satchel.\n")
    wait_for_space()
    clear_screen()
    choice2 = input("\n\n\nDo you want to open it?(y/n)\n")
    if choice2 == "y":
        clear_screen()
        print("\n\n\nThe torn satchel contains:\n\nHalf-map\nStrange Tooth\nRusty Knife\n")
        wait_for_space()
        clear_screen()

     
# if choice1 == "Avoid":

# if choice1 == "Cover Tracks":
     

# wait_for_space()
# clear_screen()
