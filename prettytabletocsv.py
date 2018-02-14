import csv
f = open('table.txt')
for x in f.readlines():
	if (x.startswith('|')):
		z = x[:-1].split("|")
		z.pop(0)
		with open('table.csv', 'ab') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow(z)
			myfile.close()
	else:
		pass
