def play_again():
    print("Would you like to play again? Yes (y) or no (n).")
    answer = input(">").lower()
    if "y" in answer:
        print("Ok!")
        start_game()
    if "n" in answer:
        print("D:")
def game_over():
    print("You got killed. Game over...")
    play_again()
def guards_fight():
    print("What do you do? Fight (f) or Run (r).")
    answer = input(">").lower()
    if "f" in answer:
        print("You punch a guard, but you get bodyslammed by a guard behind you!")
        game_over()
    elif "r" in answer:
        print("You try to run, but a guard decks you.")
        game_over()
    else:
        print("Dont you know how to type f or r?")
        game_over()
def diamond_room():
    print("You make it into a room with a diamond it in, but it is surrounded by a glass case, what do you do? \nLeave the dungeon without the diamond (l) or take it and leave the dungeon (t)?")
    answer = input(">").lower()
    if "l" in answer:
        print("You leave the dungeon safely. You escaped!")
        play_again()
    elif "t" in answer:
        print("You go and smash the glass. Oh no! Sires go off and guards come out.")
        guards_fight()
    else:
        print("Dont you know how to type l or t?")
        game_over()
def fight_room():
    print("It leads you into a room full of gladiators, what do you do? Run (r) or Fight (f)")
    answer = input(">").lower()
    if "r" in answer:
        print("You try to run but you get shot in the back by a gladiator.")
        game_over()
    elif "f" in answer:
        print ("You manage to fight one off but another comes behind you and stabs you.")
        game_over()
    else:
        print("Dont you know how to type r or f?")
        game_over()

def monster_room():
    print("It lead you to a monster room! There is zombies and skeletons everywhere!\nThere is weapons behind you, what weapon do you choose? Shield (s) or Bow (b)")
    answer = input(">").lower()
    if "s" in answer:
        print("You block and arrow from a skeleton and hit it with the shield, and then you \npummel the zombie, you made it out alive.")
        diamond_room()
    elif "b" in answer:
        print("You shoot an arrow at the skeleton but it goes right between all of the bones. He shoots you in the chest. Game Over.")
        game_over()
    else:
        game_over("Dont you know how to type s or b?")
def bear_room():
    print("Oh no! It leads you into a room with bears in it, what do you do? \n Fight (f) or Run (r)?")
    answer = input(">").lower()
    if "f" in answer:
        print("You fight the bear and manage to wrestle it to the ground.")
        fight_room()
    elif "r" in answer:
        print("You try to run but the door is locked! You get mulled by the bear.")
        game_over()
    else:
        game_over("Dont you know how to type f or r?")

def start_game():
    print("You are standing in a dark room with two hallways, one left (l) and one right (r), \n which one do you choose?")
    answer = input(">").lower()

    if "l" in answer:
        bear_room()
    elif "r" in answer:
        monster_room()
    else:
        game_over("Dont you know how to the l or r?")

start_game()