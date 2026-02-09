import time
import os
import sys

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
while True:
    choice1 = input("\n\n(Type follow/avoid) ").lower()

    if choice1 == "follow":
        clear_screen()
        print("\n\n\nYou follow the tracks and find a torn satchel.\n")
        wait_for_space()
        clear_screen()
        while True:
            choice2 = input("\n\n\nDo you want to open it?(y/n)\n")
            if choice2 == "y":
                clear_screen()
                print("\n\n\nThe torn satchel contains:\n\nStrange Tooth\nRusty Knife\n")
                wait_for_space()
                clear_screen()
                print("\n\n\nSuddenly you hear breathing behind you...")
                wait_for_space()
                clear_screen()                
                print("""
                X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
                |                           ,,'``````````````',,                            |
                X                        ,'`                   `',                          X
                |                      ,'                         ',                        |
                X                    ,'          ;       ;          ',                      X
                |       (           ;             ;     ;             ;     (               |
                X        )         ;              ;     ;              ;     )              X
                |       (         ;                ;   ;                ;   (               |
                X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
                |       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
                X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
                |       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
                X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
                | (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
                X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
                | (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
                X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
                | (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
                X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
                |",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
                X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
                || ) | \ |/ /#/ |#( \; ;     :               ;     ; ;/ )#| \#\ \| / | ( |) |
                X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
                | \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
                X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
                |####@,,'`                 `',               ,'`                 `',,@####| |
                X#,,'`                        `',         ,'`                        `',,###X
                |'  spb                          ~~-----~~                               `' |
                X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
                """)                
                print("\n\n\t...you turn around and see a 3 meter tall dark hairy figure behind you looking at you and growling...")
                wait_for_space()
                clear_screen()
                while True:
                    choice3 = input("\n\n\nWhat do you do? (run/use rusty knife/use strange tooth)").lower()
                    if choice3 == "run":
                        print("\n\n\nYou try to run away but the beast catches up to you, you feel a hot glistening pain and find yourself on the ground...")
                        print("\n\n...you pass out and never wake up...")
                        print("\n\n...GAME OVER...\n\n")
                        wait_for_space()
                        clear_screen()
                        sys.exit()
                    elif choice3 == "use rusty knife":
                        print("\n\n\nYou try to use the rusty knife to kill the beast and take a swing at it but its skin is of an unpiercable hard material and your knife breaks.")
                        print("\n\nWith an unnatural speed, the beast leaps strikes you with its massive claw. Everything turns black...")
                        print("\n\n...GAME OVER...\n\n")
                        wait_for_space()
                        clear_screen()
                        sys.exit()
                    elif choice3 == "use strange tooth":
                        print("\n\n\nAs you take the Strange Tooth out of the torn satchel the eyes of the beast widen and you notice its demeanor easing.")
                        print("\n\nIt patiently waits, expecting you to give it the tooth.")
                        print("\n\nYou put the Strange Tooth on the ground and as you do it the beast takes the Tooth and escapes into the jungle.")
                        wait_for_space()
                        clear_screen()
                        while True:
                            choice4 = input("\n\n\nYou follow the beast with your eyes and think of what to do next. (follow beast/look for others)").lower()
                            if choice4 == "follow beast":
                                print("\n\n\nYou follow the beast into the jungle and as you take a couple steps hear squirming and unhuman noises.")
                                print("\n\nThere are smaller versions of the beast playing with eachother next to a cave with the huge beast caringly watching them.")
                                print("\n\nWhile you're sneaking you accidentally snap a twig, and the sound echoes in the silence as they all freeze and look towards your direction.")
                                print("\n\nThe Beast notices you and charges at you full speed and kills by biting off your head...")
                                print("\n\n...GAME OVER...\n\n")
                                wait_for_space()
                                clear_screen()      
                                sys.exit()
                            elif choice4 == "look for others":
                                print("\n\n\nYou are a bit shaken up and follow the beach to look for others...")
                                print("\n\n...while you're walking down the beach you hear a faint noise of people talking and run towards it.")
                                wait_for_space()
                                clear_screen()      
                                print("\n\n\nIt's a group of somalian pirates with a small pirate ship and the captain notices you!")
                                print("\n\nHe angrily yells something to the others and they charge towards you!!!")
                                print("\n\n...you try to run away towards the jungle but they catch up to you fast. They hit you to the ground and tie you up with a rope.")
                                wait_for_space()
                                clear_screen()
                                print("\n\n\nAs you're on the ground, scared and not knowing what will happen next you suddenly hear rustling in the bushes from the jungle...")
                                print("\n\n...you can hear deep thumping footsteps as something is approaching you, with the time between the footsteps getting smaller and smaller...")
                                print("\n\n...the somali pirates also notice the sound and point their AK47's towards the Jungle,\n their voices are shaking while they scream at eachother and they are trembling with fear...")
                                wait_for_space()
                                clear_screen()
                                print("\n\n\n...with the frequence of the heavy footsteps becoming less and less you almost fainting of anxiety as suddenly the sound of the footsteps is gone...")
                                print("\n\n...you notice a big shadow over you, and as you look up you can see the BEAST again!\n\nIt charged and jumped towards you and lands on one of the pirates, turning him into a red goo...")
                                print("\n\n...within fractures of a second the beast totally annihilates everyone around you, then charges towards the captain and kills him on the spot with its huge fangs...")
                                wait_for_space()
                                clear_screen()
                                print("\n\n\n...you are helplessly watching the frenzy happening around you, trying to realize what is happening as suddenly the screams are turning into silence...")
                                print("\n\n...the beast is walking towards you, smears of blood all over its hairy body, pulsating with anger and giving off deep growls...")
                                print("\n\n...you are already saying your last words as it's approaching you, when it suddenly rips open the rope with an gentle ease...")
                                wait_for_space()
                                clear_screen()
                                print("\n\n\n...it stops in front of you, and gives you a deep soulpiercing look...")
                                print("\n\n...Its eyes show no friendship, only repayment — a silent message that your debt is paid, and your paths will never cross again. ...")
                                print(
                                    """
                                        \n          
                                    ,o0MMMMMMMMNMMMMM8888888888888888MMMMMM.88
                                    8888888888V'.o      OOO      OOO     o. V8
                                    8888LLLLl:      O     O ___ O       O    D88,
                                    8888888LLb        \____OOOOOO____/       '888
                                      8888888888booooooOlllllllllllOoooooood8888
                                    """
                                    )
                                wait_for_space()
                                clear_screen()
                                print("\n\n\n...trembling with fear, with only adrenaline keeping you conscious, you pass the bodies and walk towards the ship...")
                                wait_for_space()
                                clear_screen()
                                print("\n\n\n...as you enter the ship you can see a small door which leads below deck...")
                                print("\n\n...you follow the door and find a man with captains clothes tied up with a rope and blindfolded,\n\nscared stiff while sitting in a puddle of his own urine.")
                                print("\n\n...You untie the captain and he looks at you scared out of his mind as he screams: 'PLEASE DONT HURT ME'...")
                                wait_for_space()
                                clear_screen()
                                print("\n\n\n...You tell him that everything is alright and that you are only freeing him...")
                                print("\n\n...he begins to ease up and you ask him if he can get you out of this island...")
                                print("\n\n...he agrees and goes above deck, seeing all the dead bodies and blood his eyes widen looking at you...")
                                wait_for_space()
                                clear_screen()
                                print("\n\n\n...You tell him that he doesn't want to know because he wouldn't believe it anyways and he accepts your explanation in silence...")
                                print("\n\n...He starts the ship and rides it into the ocean together with you while your only wish is to forget...")
                                print("\n\n...GAME OVER...\n\n")
                                wait_for_space()
                                clear_screen()
                                sys.exit()
                            else:
                                print("\n\n\nWrong input. Try again.")
                    else:
                        print("\n\n\nWrong input. Try again.")
            elif choice2 == "n":
                clear_screen()
                print("\n\n\nSuddenly you hear breathing behind you...")
                print("\n\n...you turn around and see a 3 meter tall dark hairy figure behind you looking at you and growling...")
                print("\n\nWith an unnatural speed, the beast leaps strikes you with its massive claw. Everything turns black...")
                print("\n\n...GAME OVER...\n\n")
                sys.exit()

            else:
                    print("\n\n\nWrong input. Try again.")


    elif choice1 == "avoid":
        clear_screen()
        print("\n\n\nYou avoid the huge footsteps and walk towards the thick jungle...")
        print("\n\n...as you are walking through the jungle, climbing over old trees in its uneven ground you step on something soft...")
        print("\n\n...in the same moment you feel a sharp pain, you stepped on a venomous snake and it bit you and swiftly fled...")
        print("""
        \n
                
            ---_ ......._-_--.
            (|\ /      / /| \  |
            /  /     .'  -=-'   `.
            /  /    .'             )
        _/  /   .'        _.)   /
        / o   o        _.-' /  .'
        \          _.-'    / .'*|
        \______.-'//    .'.' \*|
            \|  \ | //   .'.' _ |*|
            `   \|//  .'.'_ _ _|*|
            .  .// .'.' | _ _ \*|
            \`-|\_/ /    \ _ _ \*|
            `/'\__/      \ _ _ \* 
            /^|            \ _ _ \*
            '  `             \ _ _ \      
                            
                """
                    )
        wait_for_space()
        clear_screen()
        print("\n\n\n...you feel your body swelling up, it's getting harder to breathe...")
        print("\n\n...white noise is getting louder and louder as you fall to the ground and suffocate from the toxin...")
        print("\n\n...GAME OVER...\n\n")
        sys.exit()



# if y/n schleife schließen
# alle ifs checken und auswahlmöglichkeiten
# conciseness checken