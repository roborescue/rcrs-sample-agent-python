from rcrs_core.agents.agent import Agent
from rcrs_core.connection import URN
from rcrs_core.constants import kernel_constants

class FireBrigadeAgent(Agent):
    def __init__(self, pre):
        Agent.__init__(self, pre)
        self.name = "firebrigadeAgent"
    
    def precompute(self):
        self.Log.info('precompute finshed')
    
    def get_requested_entities(self):
        return [URN.Entity.FIRE_BRIGADE]

    def think(self, time_step, change_set, heard):
        self.Log.info(time_step)
        if time_step == self.config.get_value(kernel_constants.IGNORE_AGENT_COMMANDS_KEY):
            self.send_subscribe(time_step, [1, 2])
        
        self.send_say(time_step, 'HELP')
        self.send_speak(time_step, 'HELP meeeee fire', 1)

        my_path = self.random_walk()

        # self.send_rescue(time_step, target)
        # self.send_say(time_step, 'HELP')
        # self.send_speak(time_step, 'HELP meeeee police', 1)
        self.send_move(time_step, my_path)
        # self.send_rest(time_step)
            


