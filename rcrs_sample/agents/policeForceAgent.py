from rcrs_core.agents.agent import Agent
from rcrs_core.constants import kernel_constants
from rcrs_core.connection import URN
from rcrs_core.entities.blockade import Blockade
from rcrs_core.entities.road import Road
import math
import sys

class PoliceForceAgent(Agent):
    def __init__(self, pre):
        Agent.__init__(self, pre)
        self.name = 'PoliceForceAgent'
    
    def precompute(self):
        self.Log.info('precompute finshed')

    def get_requested_entities(self):
        return [URN.Entity.POLICE_FORCE]

    def think(self, time_step, change_set, heard):
        self.Log.info(time_step)
        if time_step == self.config.get_value(kernel_constants.IGNORE_AGENT_COMMANDS_KEY):
            self.send_subscribe(time_step, [1, 2])

        my_path = self.random_walk()
        if isinstance(self.location(), Road):
            target = self.get_nearest_blockade()
            if target:
                self.send_clear(time_step, target)
                return
                  
        # self.send_say(time_step, 'HELP')
        # self.send_speak(time_step, 'HELP meeeee police', 1)
        self.send_move(time_step, my_path)
        # self.send_rest(time_step)

    def get_nearest_blockade(self):
        best_distance = sys.maxsize
        best = None
        area = self.location()
        x = self.me().get_x()
        y = self.me().get_y()
        for en in self.world_model.get_entities():
            if isinstance(en, Road):
                for b in en.get_blockades():
                    blockade = self.world_model.get_entity(b)
                    if blockade:
                        dx = abs(blockade.get_x() - x)
                        dy = abs(blockade.get_y() - y)
                        distance = math.hypot(dx, dy)
                        if distance < best_distance and distance < float(self.config.get_value('clear.repair.distance')):
                            best_distance = distance
                            best = blockade.get_id()
        
        return best
