Install prerequisites using the following commands:
sudo apt install python3-pip
sudo apt-get install -y python3-rtree
sudo pip install --upgrade protobuf

OR
pip install -r requirements.txt

Run server:
https://github.com/roborescue/rcrs-server
cd rcrs-server/scripts
./start.sh -m ../maps/test/map -c ../maps/test/config

Run python sample agents:
https://github.com/roborescue/rcrs-sample-agent-python
cd rcrs-sample-agent-python
python3 launcher.py -fb -1 -pf -1 -at -1

-fb  {number of Firebrigade agents (-1 to run all)}
-fs  {number of FireStation agents (-1 to run all)}
-pf  {number of PoliceForce agents (-1 to run all)}
-po  {number of PoliceOffice agents (-1 to run all)}
-at  {number of AmbulanceTeam agents (-1 to run all)}
-ac  {number of AmbulanceCenter agents (-1 to run all)}
-pre {precompute flag. default is false}
-p   {RCRS server port number}
-h   {RCRS server host IP}