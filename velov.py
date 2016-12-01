import glob, json #/home/fabrice/Documents/M1/ecoles/
files = glob.glob("velov/*")
files.sort()

csv = open("velov.csv", 'w')
true, false = True, False
counter = 0

for url in files:
	f = open(url)
	dateTmp = url.split('/')[-1].split('.')[0].split('_')
	[year, month, day] = dateTmp[0].split('-')[2:5]
	[hour, minute] = dateTmp[1].split('-')
	date = "{},{},{},{},{}".format(year, month, day, hour, minute)
	#print(f.read())

	#print(url)
	content = json.loads(str(f.read()))
	for line in content:
		number = line['number']
		bikes = line['available_bikes']
		stands = line['available_bike_stands']

		counter += csv.write("{},{},{},{}\n".format(date, number, bikes, stands))
	f.close()

csv.close()
print(counter)