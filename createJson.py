import json
import csv
from random import randint

with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

data = {}

statePops = {}

totalPop = 0

for ele in your_list:
	[location, pop] = ele
	[county, state] = location.split(", ")
	pop = pop.replace(",","")
	pop = int(pop)
	# print county + "\t" + state + "\t" + pop
	
	if state not in data:
		data[state] = {}

	if state not in statePops:
		statePops[state] = 0

	data[state][county] = pop
	statePops[state] += pop
	totalPop += pop



maxData = {}

jsonData = []

for state in data:
	stateData = data[state]

	# create a function which returns the value of a dictionary
	def keyfunction(k):
	    return stateData[k]

	maxData[state] = {}

	countyData = []

	# sort by dictionary by the values and print top 3 {key, value} pairs

	toKeep = statePops[state] * 200 / totalPop + 1

	for key in sorted(stateData, key=keyfunction, reverse=True)[:toKeep]:
		# print state, key, stateData[key]
		# maxData[state][key] = stateData[key]
		countyData.append({"name": key, "size": stateData[key]})

	jsonData.append({"name": state, "children": countyData})

    # print "%s: %i" % (key, virginiaData[key])


# filteredData = {}

# countyData = data["Virginia"]

# for ele in maxData:
# 	print ele + str(maxData[ele])

# print json.dumps(maxData)


master = []
master.append({"name": "United States", "children": jsonData})

f = open("jsonOut.json", "w")
# print json.dumps(jsonData)

json.dump(master[0], f, sort_keys=False, indent=4, separators=(',', ': '))

f.close()

# f.write(str(jsonData))
# f.close()

# for ele in jsonData:
# 	print ele