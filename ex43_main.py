import random
from ex43_Scenes import *

class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map

    def play(self):
        destination = self.map.opening_scene()
        while True:
            destination = self.map.next_scene(destination)

class Map(object):

    def __init__(self, start_scene):
        self.current_scene = start_scene

    def next_scene(self, scene_name):
        if scene_name == 'bridge':
            return TheBridge().enter()
        elif scene_name == 'armory':
            return LaserWeaponArmory().enter()
        else:
            pass

    def opening_scene(self):
        return CentralCorridor().enter()

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
