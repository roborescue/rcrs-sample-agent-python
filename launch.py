from random import sample
import time
import sys
import os
from typing import List
from multiprocessing import Process
import ipaddress

from rcrs_core.connection.componentLauncher import ComponentLauncher
from rcrs_sample.agents.policeForceAgent import PoliceForceAgent
from rcrs_sample.agents.ambulanceTeamAgent import AmbulanceTeamAgent
from rcrs_sample.agents.fireBrigadeAgent import FireBrigadeAgent
from rcrs_sample.agents.fireStationAgent import FireStationAgent
from rcrs_sample.agents.policeOfficeAgent import PoliceOfficeAgent
from rcrs_sample.agents.ambulanceCenterAgent import AmbulanceCenterAgent
from rcrs_core.constants.constants import DEFAULT_KERNEL_PORT_NUMBER
from rcrs_core.constants.constants import DEFAULT_KERNEL_HOST_NAME


class Launcher:
    def __init__(self, ):
        pass        

    def launch(self, agent, _request_id):
        self.component_launcher.connect(agent, _request_id)

    def run(self, kwargs):
        processes = []
        agents = {}
        self.component_launcher = ComponentLauncher(kwargs['port'], kwargs['host'])
        agents['FireBrigadeAgent'] = kwargs['fb'] if kwargs['fb'] >= 0 else 100
        agents['FireStationAgent'] = kwargs['fs'] if kwargs['fs'] >= 0 else 100
        agents['PoliceForceAgent'] = kwargs['pf'] if kwargs['pf'] >= 0 else 100
        agents['PoliceOfficeAgent'] = kwargs['po'] if kwargs['po'] >= 0 else 100
        agents['AmbulanceTeamAgent'] = kwargs['at'] if kwargs['at'] >= 0 else 100
        agents['AmbulanceCenterAgent'] = kwargs['ac'] if kwargs['ac'] >= 0 else 100
        precompute = True if str(kwargs['precompute']).lower() == 'true' else False

        for agn, num in agents.items():
            for _ in range(num):
                request_id = self.component_launcher.generate_request_ID()
                process = Process(target=self.launch, args=(eval(agn)(precompute), request_id))
                process.start()
                processes.append(process)
                time.sleep(1/100)
        
        for p in processes:
            p.join()

    def pars_args(self, sys_args: List[str]) -> dict:
        args = {}
        arg = sys_args.pop(0)

        while(arg is not None and len(sys_args) >= 2):
            arg = sys_args.pop(0)
            value = sys_args.pop(0)
            args[arg] = value

        if(len(sys_args) > 0):
            print('Usage: python3 launcher.py')
            print('[options]')
            print('-p    RCRS server port number')
            print('-h    RCRS server host IP')
            print('-fb   number of Firebrigade       (-1 to run all)')
            print('-fs   number of FireStation       (-1 to run all)')
            print('-pf   number of PoliceForce       (-1 to run all)')
            print('-po   number of PoliceOffice      (-1 to run all)')
            print('-at   number of AmbulanceTeam     (-1 to run all)')
            print('-ac   number of AmbulanceCenter   (-1 to run all)')
            print('-pre  precompute flag. default is false')
            sys.exit(0)
        
        elements = {}
        try:
            host = args.get('-h') if '-h' in args else DEFAULT_KERNEL_HOST_NAME
            if host != 'localhost':
                ipaddress.ip_address(host)
            elements['host'] = host
        except ValueError as err:
            print(err)
            sys.exit(0)
        
        try:
            elements['port'] = int(args.get('-p')) if '-p' in args else int(DEFAULT_KERNEL_PORT_NUMBER)
            elements['precompute'] = args.get('-pre') if '-pre' in args else 'False' 
            elements['fb'] = int(args.get('-fb')) if '-fb' in args else 0
            elements['fs'] = int(args.get('-fs')) if '-fs' in args else 0
            elements['pf'] = int(args.get('-pf')) if '-pf' in args else 0
            elements['po'] = int(args.get('-po')) if '-po' in args else 0
            elements['at'] = int(args.get('-at')) if '-at' in args else 0
            elements['ac'] = int(args.get('-ac')) if '-ac' in args else 0
        except ValueError as err:
            print(err)
            sys.exit(0)

        return elements


def main(sys_args: List[str]):
    if not os.path.exists('logs'):
        os.makedirs('logs')

    filelist = [f for f in os.listdir('logs') if f.endswith(".log")]
    for f in filelist:
        os.remove(os.path.join('logs', f))

    print("start launcher...")
    l = Launcher()
    l.run(l.pars_args(sys_args))
    
    while True:
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            sys.exit(1)
    print("launcher exited...")

if __name__ == '__main__':
    main(sys.argv)
    
