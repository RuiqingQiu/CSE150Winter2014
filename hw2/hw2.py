f= open ('zipcode.txt','r')
print "opening file ..."
print f
zipcodes = []
population = []
with open ('zipcode.txt') as openfileobject:
    for line in openfileobject:
	tmp = line.split()
	zipcodes.append(tmp[0])
	population.append(tmp[1])
index = 0
for zipcode, pop in zip(zipcodes, population):
    print "#%d, zip: " % index + zipcode + " pop: " + pop
    index += 1

