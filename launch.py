import time
import sys
import os
from typing import List
from rcrs_core.launcher.launcher import Launcher

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
    
