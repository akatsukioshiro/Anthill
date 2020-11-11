import os
import sys

def base():
	try:
		os.remove("flask_server_KD.py")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("arduino_esp32_agent.ino")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("database.json")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("registerred_devices.json")
	except FileNotFoundError as f:
		print(f)
		pass
def all():
	base()
	try:
		os.remove("arduino_esp32_agent.template")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("clean_database.py")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("configuration.json")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("flask_server_KD.template")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("json_collector.py")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("setup.py")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("unregister_devices.py")
	except FileNotFoundError as f:
		print(f)
		pass
	try:
		os.remove("uninstall.py")
	except FileNotFoundError as f:
		print(f)
		pass
	


if sys.argv[1] == "soft":
	base()
elif sys.argv[1] == "hard":
	all()
else:
	print("Windows Usage:\npy uninstall.py soft")
	print("Windows Usage:\npy uninstall.py hard")
	print("Linux Usage:\npython uninstall.py soft")
	print("Linux Usage:\npython uninstall.py hard")
	
