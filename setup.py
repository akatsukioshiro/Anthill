import json
import unregister_devices
import clean_database

print("\n\n################################################\n")
print("##############   Initializing ... ##############\n")

try:
	print("######   Reading - configuration.json ... ######\n")

	with open("configuration.json","r") as cj:
		data=json.loads(str(cj.read()).replace("'","\""))
except FileNotFoundError as ef:
	print("\n"+str(ef))
	print("\n######   Execution Failed at Step 1 ... ########\n")
	exit()
	
print("###  Read Success - configuration.json ... #####\n")

try:
	print("#### Reading - flask_server_KD.template ... ####\n")

	with open("flask_server_KD.template","r") as ft:
		template=str(ft.read())
except FileNotFoundError as ef:
	print("\n"+str(ef))
	print("\n######   Execution Failed at Step 2 ... ########\n")
	exit()
	
print("#  Read Success - flask_server_KD.template ... #\n")
try:

	template=template.replace("*HOST*",data["flask_server_ip"])
	template=template.replace("*PORT*",data["flask_server_port"])

except KeyError as ke:
	print("\n"+str(ke))
	print("Bad configuration.json File")
	print("flask_server_ip, flask_server_port should be present")
	print("\n######   Execution Failed at Step 3 ... ########\n")
	exit()

print("####  All Success - flask_server_KD.py ... #####\n")

try:
	print("## Reading - arduino_esp32_agent.template ... ##\n")

	with open("arduino_esp32_agent.template","r") as ft:
		template2=str(ft.read())
except FileNotFoundError as ef:
	print("\n"+str(ef))
	print("\n######   Execution Failed at Step 4 ... ########\n")
	exit()
	
print("# Read Success - arduino_esp32_agent.template  #\n")

try:

	template2=template2.replace("*HOST*",data["flask_server_ip"])
	template2=template2.replace("*PORT*",data["flask_server_port"])
	template2=template2.replace("*WIFI_SSID*",data["wifi_ssid_esp32"])
	template2=template2.replace("*WIFI_PASS*",data["wifi_pass_esp32"])

except KeyError as ke:
	print("\n"+str(ke))
	print("Bad configuration.json File")
	print("wifi_ssid_esp32, wifi_pass_esp32 should be present")
	print("\n######   Execution Failed at Step 5 ... ########\n")
	exit()
	
	
print("##  All Success - arduino_esp32_agent.ino ... ##\n")

with open("flask_server_KD.py","w+") as fp:
	fp.write(template)

with open("arduino_esp32_agent.ino","w+") as fp:
	fp.write(template2)

with open("database.json","w+") as f:
	f.write("{}")

print("############  Finished Successfully  ###########")
print("\n################################################\n\n")
