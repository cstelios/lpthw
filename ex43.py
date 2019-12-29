import random

class Scene(object):

    def enter(self):
        pass

    def getChoice(self):
        input("> ")

    def analyseText(self, choice, objectList):
        move_action = ["move", "go to", "walk", "run", "jump", "stroll", "slide"]
        attack_action = ["attack", "shoot", "stab", "bite", "punch", "kick", "headbutt", "tackle", "wresle", "hit", "pull"]
        take_action = ["take", "grab", "loot"]
        investigate_action = ["look", "search", "scan", "investigate", "examine", "explore", "probe", "check"]
        interact_action = ["touch", "activate", "interact", "use", "tricker", "hold", "hide"]
        action_lists = [move_action, attack_action, take_action, investigate_action, interact_action]

        choice = choice.strip()
        choice = choice.lower()
        if choice:
            for word in objectList:
                if word in choice:
                    object = word
                    break
                else:
                    object = None
        else:
            return(0, None)

        for i in range(0, len(action_lists)):
            for word in action_lists[i]:
                if word in choice:
                    return ((i + 1), object)
                else:
                    pass

    def noChoice(self):
        random_Messages = []
        random_Messages.append("This is not time to freeze! Get a hold of yourself!!!")
        random_Messages.append("...They do say pantience is a virtue... but you might want to do something.")
        random_Messages.append("Tick tock tick tock tick tock...")
        random_Messages.append("So... you want to do nothig?!")
        random_Messages.append('A bit indecisive ha??? Not to worry you, but time\'s running out.')
        random_Messages.append("...")
        print(str(random.sample(random_Messages, 1)).replace("['", "").replace("']", "").replace('["', "").replace('"]', ""))

class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map

    def play(self):
        destination = self.map.opening_scene()
        while True:
            self.map.next_scene(destination)

class Death(Scene):

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
        self.alien_conscious = True
        self.wound_counter = 0

        print(
        "\nYou wake up in a daze...",
        "\nIt takes you a couple of seconds to get your bearing but you realise you are in the Central Corridor of the ship.",
        "\nWhat happened?",
        "\nWhy does your head hurt?",
        "\nLast thing you remember is being in your room learning the new powerful Python 72.",
        "\nIt comes with a build in A.I.. It will be so cool to...",
        "\n...",
        "\nYou freeze. There is an alien standing right there!",
        "\nIt all comes back to you, the ship was boarded. You rushed to the Bridge when...!",
        "\nOh God! You got shot!",
        "\nYou check yourself and see a laser hole in your abdomen. It looks bad... probably why the aliens thought you were dead.",
        "\nYou have to get out of here! You have to get down to the nearest planet and contact Command.",
        "\nYou should probably also damage the ship as much as possible so that these a-holes don't get to figuring human technology out.",
        "\nThe alien does not seem to have noticed you moving around yet...",
        )

        object_List = ["alien", "room", "door", "bridge", "armory", "corridor", "area"]
        special_Actions = []
        inventory = []

        while True:
            if self.wound_counter == "healed":
                pass
            elif self.wound_counter >= 5:
                Death().enter("Most people would prioritise the gaping wound in the middle of their body.\nI guess you are not most people... \nYou bled to death!")
            else:
                self.wound_counter += 1

            choice = input("\nWhat do you do?\n> ")
            action, object = self.analyseText(choice, object_List)

            if action == 0:
                self.noChoice()

            elif action == 1:
                if object:
                    if object == 'alien':
                        print("You attempt to close the distance to the alien...")
                        if random.random() > 0.75:
                            print("You somehow managed to get close to the alien without him noticing you. What now?")
                        else:
                            Death().enter("The alien hears the scaffle, turns to you and shoots you in the face")
                    elif object == 'bridge' or 'armory':
                        if self.alien_conscious == True:
                            Death().enter("The alien notices you moving around. Shoots to imobilise and prepares for a feast.")
                        else:
                            return(object)
                    else:
                        pass
                else:
                    print(f"I don't understand where you want to go... ({object}??)")
                    if self.wound_counter == 'healed':
                        pass
                    else:
                        self.wound_counter -= 1

            elif action == 2:
                if object:
                    if object == 'alien':
                        print("You charge the alien with your bare hands...")
                        if random.randint(1,101) > 80:
                            print("After a brutal, yet weirdly silent fight, you emerge victorius. The alien's purple blood is all over you and mixes with your own blood gashing though your wound.")
                            self.wound_counter += 1
                            self.alien_conscious = False
                            object_List.append('gun')
                        else:
                            Death().enter("He freezes for a moment and you see an opening. Unfortunately it was him opening his huge mouth.\nHe bites your face off!")
                    else:
                        print("You can't attack that.")
                else:
                    print("I know you are trying to attack something.... not sure what it is though... :/")
                    if self.wound_counter == 'healed':
                        pass
                    else:
                        self.wound_counter -= 1
            elif action == 3:
                if object:
                    if object == 'medkit':
                        print("You pickup the medkit.")
                    else:
                        print("You can't do that.")
                else:
                    print("Please be clearer on what you are trying to get.")
                    if self.wound_counter == 'healed':
                        pass
                    else:
                        self.wound_counter -= 1

            elif action == 4:
                if object == 'room':
                    print("You scan the room for anything useful.")
                    print("You see your trusty Info-slate and your knife a couple of feet next to you.")
                    print("Luckily you see a medkit up on the wall next to you. That should come in handy.")
                    object_List.append('info-slate')
                    object_List.append('knife')
                    object_List.append('medkit')
                elif object == 'alien':
                    print('You have not seen this particular species before. Maybe you can find a Wikipedia entry on your Info-slate.')
                    if 'info-slate' in object_List:
                        pass
                    else:
                        print("You should probably search the room for it...")
            else:
                pass

class LaserWeaponArmory(Scene):

    def enter(self):
        print("This is it for now. I guess you win! :)")
        exit(0)

class TheBridge(Scene):

    def enter(self):
        print("This is it for now. I guess you win! :)")
        exit(0)

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        self.current_scene = start_scene

    def next_scene(self, scene_name):
        if scene_name == 'bridge':
            TheBridge().enter()
        elif scene_name == 'armory':
            LaserWeaponArmory().enter()
        else:
            pass

    def opening_scene(self):
        CentralCorridor().enter()

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
