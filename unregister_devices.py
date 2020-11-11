
def clean():

	data="""{
    	"devices": []
	}
	"""

	with open("registerred_devices.json","w+") as f:
		f.write(data)

clean()
