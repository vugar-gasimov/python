print("=================>Welcome to Treasure Island<===================")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("=>To Win the game find the treasure!")
in_lake = ""
in_island = ""

in_croad = input("You are at cross road. Where do you want to go? Type right or left ")

if in_croad == "right":
    in_lake = input('You come to a lake. There is on island in the middle of the lake. Type "wait" to wait for a boat. Or Type "swim" to swim across.')
elif in_croad == "left":
    print('You found another journey get married and when you come back there was no treasure left in the castle.')
if in_lake == "swim":
        print(''' ______
    ,-' ;  ! `-.
   / :  !  :  . \
  |_ ;   __:  ;  |
  )| .  :)(.  !  |
  |"    (##)  _  |
  |  :  ;`'  (_) (
  |  :  :  .     |
  )_ !  ,  ;  ;  |
  || .  .  :  :  |
  |" .  |  :  .  |
  |____------.___|''') 
        in_island = input("You arrived at the island unharmed. There is a castle with 3 doors. One red, one yellow and one blue. Which color do you choose? Type red, yellow, or blue ") 
elif in_lake == "wait":
        print('Pirates come and stole your treasure')
if in_island == "red":
            print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"''')
            in_beats = print("Congratulations you entered a room of beasts. Game Over")
elif in_island == "yellow":
            print('''       _____________.-'________________
                         /         _.-' O                /|
                        /  i====_======O      __________/ /
                       /  / _.-'      O      /     _   /|/
                      /  / | p       o      /     (   / /
                     /  /           O      /_________/ /
                    /  L===========O                /|/
                   /______________O________________/ /
                   |________________________________|/''')
            in_beats = print("Congratulations you entered a room of traps. Game Over")
elif in_island == "blue":
            in_treasure = print("You found the treasure Congratulations'Imagine now going back;//'")