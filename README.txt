Installation Steps:

1. Place all 9 Files in same folder.

2. Open configuration.json file and replace ipaddress with server ip, change port if required.

3. Set network password in configuration.json for esp32 to connect to.

4. Run setup.py to install using comand: py setup.py.

5. Take arduino_esp32_agent.ino and flash into esp32 device.

4. Start flask server using command: py flask_server_KD.py

5. Start esp32

6. Check database.json

Uninstallation Steps:

1. For Partial Unistallation run command: py uninstall.py soft

2. To delete the whole setup run command: py uninstall.py hard


Thank You
