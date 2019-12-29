# PostgreSQL
# json
# pyqt5 - UI - qt.io

# github

import random

class Scene(object):

    def enter(self):
        pass

    def analyseText(self, choice, objectList):
        # Define the various lists of available actions (verbs):
        move_action = ["move", "go to", "walk", "run", "jump", "stroll", "slide"]
        attack_action = ["attack", "shoot", "stab", "bite", "punch", "kick", "headbutt", "tackle", "wresle", "hit", "pull", "kill"]
        take_action = ["take", "grab", "loot", "pick up"]
        investigate_action = ["look", "search", "scan", "investigate", "examine", "explore", "probe", "check"]
        interact_action = ["touch", "activate", "interact", "use", "tricker", "hold", "hide"]
        # Assemble all lists into a single list so that I can iterate through them
        action_lists = [move_action, attack_action, take_action, investigate_action, interact_action]

        choice = choice.strip() # Remove any whitespace from input
        choice = choice.lower() # Turn all characters to lowercase

        # Check if the user has specified any of the objects passed from the Scene in the objectList variable
        object = None
        if choice:
            for word in objectList:
                if word in choice:
                    object = word
                    break
                else:
                    pass
        else:
            return(0, None) # For all Scenes, a return of 0 means that the user left input blank.

        # for each action list, search for their members in the user input
        # All Scenes understand the return values as:
        # (the following are based on the action lists created above)
        # 1 = move action
        # 2 = attack action
        # 3 = take action
        # 4 = investigate action
        # 5 = interact action

        # 9 means that no action has been found
        for i in range(0, len(action_lists)):
            for word in action_lists[i]:
                if word in choice:
                    return ((i + 1), object)
                else:
                    pass

        return(9, object)

    # This function is called-upon if the user submitted an empty responce
    # The fuction prints a random responce urging him to take action before it's too late
    def noChoice(self):
        random_Messages = [
        "This is not time to freeze! Get a hold of yourself!!!",
        "...They do say pantience is a virtue... but you might want to do something.",
        "Tick tock tick tock tick tock...",
        "So... you want to do nothig?!",
        'A bit indecisive ha??? Not to worry you, but time\'s running out.',
        "...",
        "Remember that time you went out to that dumpy bar and met that blonde? Good times, good times... Well, this might not be a good time for nostalgia. Get a move on!!!"
        ]
        # for presentation purposes, [', '], [" and "] are removed from the selected string before printing it.
        print(str(random.sample(random_Messages, 1)).replace("['", "").replace("']", "").replace('["', "").replace('"]', ""))

    # if the user specifies no action
    def noSense(self, object):
        if object:
            print(f"What about the \"{object}\"..? Try again!")
        else:
            print("You are not making any sense! Try again!")





class Death(Scene):
    # This class is called when the player dies. It prints the skeleton and a message taken as a parameter in the enter() function.
    def enter(self, description):
        print("""
                       ______
                    .-"      "-.
                   /            \\
       _          |              |          _
      ( \\         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \\__)( |     _.=" <
      (_/"=._"=._ |/     /\\     \\| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\\__|IIIIII|__/="
                _.="| \\IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \\_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \\_)

        """)
        print(description)
        exit(0)





class CentralCorridor(Scene):

    def enter(self):
        # set up variables we will need later
        self.alien_conscious = True
        self.wound_counter = 0

        #print title
        print("""
 sdSSSSSSSbs    sSSs_sSSs     .S_sSSs     .S    S.
 YSSSSSSSS%S   d%%SP~YS%%b   .SS~YS%%b   .SS    SS.
        S%S   d%S'     `S%b  S%S   `S%b  S%S    S&S
       S&S    S%S       S%S  S%S    S%S  S%S    d*S
      S&S     S&S       S&S  S%S    d*S  S&S   .S*S
      S&S     S&S       S&S  S&S   .S*S  S&S_sdSSS
     S&S      S&S       S&S  S&S_sdSSS   S&S~YSSY%b
    S*S       S&S       S&S  S&S~YSY%b   S&S    `S%
   S*S        S*b       d*S  S*S   `S%b  S*S     S%
 .s*S         S*S.     .S*S  S*S    S%S  S*S     S&
 sY*SSSSSSSP   SSSbs_sdSSS   S*S    S&S  S*S     S&
sY*SSSSSSSSP    YSSP~YSSY    S*S    SSS  S*S     SS
                             SP          SP
                             Y           Y
                         _                     _
                        (_)                   (_)
                     _   _ _ ____   ____ _ ___ _  ___  _ __
                    |_| | | '_ \\ \\ / / _` / __| |/ _ \\| '_ \\
                     _  | | | | \\ V / (_| \\__ \\ | (_) | | | |
                    |_| |_|_| |_|\\_/ \\__,_|___/_|\\___/|_| |_|

        """)

        # print opening scene description
        print("""
        \rYou wake up in a daze...
        \rIt takes you a couple of seconds to get your bearing but you realise you are in the Central Corridor of the ship.
        \rWhat happened?
        \rWhy does your head hurt?
        \rLast thing you remember is being in your room learning the new powerful Python 72.
        \rIt comes with a build in A.I.. It will be so cool to...
        \r...
        \r...
        \rYou freeze. There is an alien standing right there!
        \rIt all comes back to you, the ship was boarded. You rushed to the Bridge when...!
        \rOh God! You got shot!
        \rYou check yourself and see a laser hole in your abdomen. It looks bad... probably why the aliens thought you were dead.
        \rYou have to get out of here! You have to get down to the nearest planet and contact Command.
        \rYou should probably also damage the ship as much as possible so that these a-holes don't get to figuring human technology out.
        \rThe alien does not seem to have noticed you moving around yet...
        """)

        # create list of objects the user can interact with in this Scene.
        # this list can be modified by the choices of the user. Some more options can be unlocked while others can be removed
        object_List = ["alien", "room", "door", "bridge", "armory", "corridor", "area", "around"]

        # define any special actions the user can takes
        # these should be different from the actions listed in the action_lists of the Scene class
        special_Actions = []

        # This is the inventory of the player
        # it starts empty and items can be added as the player collects them.
        # some items need to be in the user's inventory in order to be used
        # items will be removed if they have been used up
        inventory = []

        while True:
            # the player starts off wounded in this scene
            # he should act quickly to get healed. If not he will die.
            if self.wound_counter == "healed":
                pass
            elif self.wound_counter >= 5:
                Death().enter("Most people would prioritise the gaping wound in the middle of their body.\nI guess you are not most people... \nYou bled to death!")
            else:
                self.wound_counter += 1

            # ask for the users input and store it the choice variable
            choice = input("\nWhat do you do?\n> ")

            # using unpacking we assign values to two variables by calling the analyseText method
            # special_Actions and inventory have not yet been implemented
            action, object = self.analyseText(choice, object_List)

            # having decoded what action the user wishes to do and to what object we can decide on our feedback:

            # if input was blank
            if action == 0:
                self.noChoice()

            # if input made no sense at all
            elif action == 9:
                self.noSense(object)
                self.rewind_wound()

            # if the user decided to take a move action
            elif action == 1:
                if object:
                    # if we know what object the user wants to move towards to:
                    if object == 'alien':
                        print("You attempt to close the distance to the alien...")
                        if random.random() > 0.75:
                            print("You somehow managed to get close to the alien without him noticing you.")
                        else:
                            Death().enter("The alien hears the scaffle, turns to you and shoots you in the face")
                    elif object in ["bridge", "armory"]:
                        if self.alien_conscious == True:
                            Death().enter("The alien notices you moving around. Shoots to imobilise and prepares for a feast.")
                        else:
                            # if the alien is unconsious, the player can move on to the next room
                            return(object)
                    else:
                        pass
                else:
                    print(f"I don't understand where you want to go...")
                    self.rewind_wound()

            # if the user decided to take an attack option
            elif action == 2:
                if object:
                    if object == 'alien':
                        print("You charge the alien with your bare hands...")
                        if random.randint(1,101) > 80:
                            print("After a brutal, yet weirdly silent fight, you emerge victorius. The alien's purple blood is all over you and mixes with your own blood gashing though your wound.")
                            self.alien_conscious = False
                            object_List.append('gun')
                            if self.wound_counter == 'healed':
                                pass
                            else:
                                self.wound_counter += 1
                        else:
                            Death().enter("He freezes for a moment and you see an opening. Unfortunately it was him opening his huge mouth.\nHe bites your face off!")
                    else:
                        print("You can't attack that.")
                else:
                    print("I know you are trying to attack something.... not sure what it is though...")
                    self.rewind_wound()

            # if the user decided to pick something up
            elif action == 3:
                if object:
                    if object in ['medkit', 'info-slate', 'knife', 'gun']:
                        print("The item has been added to your inventory.")
                        inventory.append(object)
                    else:
                        print("You can't do that.")
                else:
                    print("Please be clearer on what you are trying to get.")
                    self.rewind_wound()

            # if the user decided to investigate
            elif action == 4:
                if object in ["room", "around", "corridor"]:
                    print("""
                    \rYou scan the room for anything useful.

                    \rYou see the familiar central corridor, now blackened by fire and stained with blood.
                    \rOne of your coworkers lies at alien's feet... motionless...

                    \rThere are three doors leading out of the room.
                    \rAt the front lies the door to the Bridge. There are bloody drag marks, as if from a body, leading to the door.

                    \rAt your right you see the door to the Armory. The aliens seem to have unsuccessfuly tried breaking through it.
                    \rThe Armory door seems damaged but you should be able to wedge it open after unlocking it.

                    \rOn the left you see the door to the Crew Quarters. That's where you will find the escape pods.
                    \rUnfortunately, after the "Bingo Incident" last month, the pods have been deactivated and you will need to unlock them from the Bridge.

                    \rA couple of feet to your right you see your Info-slate and your knife. Your pistol is nowhere to be found.
                    \rAt the med-station above you there is a lone medkit. You thank your lucky stars...
                    """)
                    # add the newly discovered items in the object_List and make them interactive
                    object_List.append('info-slate')
                    object_List.append('knife')
                    object_List.append('medkit')
                elif object == 'alien':
                    print("""
                    \rThe alien stands two meters tall.
                    \rEight legs clad in leather armor, leading to a bulgy torso.
                    \rTwo muscular arms and a large hound-like head complete the horrid picture.

                    \rFrom its clothing and the large, yet cheap looking, rifle, you summise that the ship has been boarded by mercenaries...
                    \ror pirates maybe? Either way, this is no soldier.

                    \rYou have not seen this particular species before.
                    \rWith its scaly hide and arachnide body, its seems to be the result of an experiment gone wrong.
                    \rMaybe you can find a Wikipedia entry on your Info-slate.
                    """)
                    if 'info-slate' in object_List:
                        pass
                    else:
                        print("You should probably search the room for it...")
            else:
                pass

    # It would be unfair to misunderstand the user and punish him for loosing a turn. Reset the counter 1 point
    # This method is called whenever the input is not fully understood
    def rewind_wound(self):
        if self.wound_counter == 'healed':
            pass
        else:
            self.wound_counter -= 1



class LaserWeaponArmory(Scene):

    def enter(self):
        print("\nThis is all i coded for now... I guess you win! :)")
        exit(0)





class TheBridge(Scene):

    def enter(self):
        print("\nThis is all i coded for now... I guess you win! :)")
        exit(0)





class EscapePod(Scene):

    def enter(self):
        pass
