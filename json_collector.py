import urllib.request
import json
from datetime import datetime

def ping_esp32():

	with open("registerred_devices.json","r") as rd:
		data_rd=json.loads(str(rd.read()).replace("'","\""))
	
	for ip in data_rd["devices"]:
		esp32_url="http://"+ip
	
		try:
		
			data = urllib.request.urlopen(esp32_url,timeout=5).read()

			if isinstance(data,bytes) == True:
				data=str(data,"utf-8")
				data=json.loads(data.replace("'","\""))

			with open("database.json","r") as f:
				db=json.loads(f.read())
		
			data["client_id"]=ip

			wnames=[]
			for wn in data["wifi_names"]:
				if wn.strip() == "":
					continue
				wnames.append(wn)

			data["wifi_names"]=wnames

			wids=[]
		
			for wi in data["wifi_ids"]:
				if wi.strip() == "":
					continue
				wids.append(wi)

			data["wifi_ids"]=wids

		
			db[datetime.now().strftime("%Y-%m-%d %H:%M:%S")]=data

			pretty=json.dumps(db, sort_keys=True, indent=4)

			with open("database.json","w+") as f:
				f.write(pretty)

			print(data)

		except urllib.error.URLError:
			print(ip+" - Not Transmitting Anymore/Request Timed Out (Threshhold: 5sec)")

