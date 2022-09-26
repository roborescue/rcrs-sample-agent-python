from rcrs_core.agents.agent import Agent
from rcrs_core.connection import URN


class PoliceOfficeAgent(Agent):
    def __init__(self, pre):
        Agent.__init__(self, pre)
        self.name = 'PoliceOfficeAgent'

    def precompute(self):
        self.Log.info('precompute finshed')

    def get_requested_entities(self):
        return [URN.Entity.POLICE_OFFICE]

    def think(self, timestep, change_set, heard):
        pass
