
def clean():

	data="{}"

	with open("database.json","w+") as f:
		f.write(data)

clean()
