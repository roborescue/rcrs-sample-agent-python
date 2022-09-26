from rcrs_core.agents.agent import Agent
from rcrs_core.connection import URN


class AmbulanceCenterAgent(Agent):
    def __init__(self, pre):
        Agent.__init__(self, pre)
        self.name = 'AmbulanceCenterAgent'

    def precompute(self):
        self.Log.info('precompute finshed')

    def get_requested_entities(self):
        return [URN.Entity.AMBULANCE_CENTRE]

    def think(self, timestep, change_set, heard):
        pass
