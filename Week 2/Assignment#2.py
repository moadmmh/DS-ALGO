from collections import OrderedDict as od


phoneRELEASED = {
		"Iphone" : 2007,
		"Iphone 3G" : 2008,
		"Iphone 3GS" : 2009,
		"Iphone 4" : 2010,
		"Iphone 4S" : 2011,
		"Iphone 5" : 2012,
                "Iphone 6" : 2014,
                "Iphone X" : 2017,
                "Iphone XS" : 2018
	}
#Checking the length
print("The length of the phoneRELEASED dictionary is :",len(phoneRELEASED))

#Assigning new values
phoneRELEASED["Galaxy J5"]=2017
phoneRELEASED["Galaxy A8"]=2016
phoneRELEASED["Galaxy C5"]=2016
phoneRELEASED["Gear sport"]=2017
phoneRELEASED["Z4"]=2017

#printing with items() method

for key,value in phoneRELEASED.items():
    print(key,"==>",value)

#replacing keys and values 

phoneRELEASED["Lenovo A3600"]=phoneRELEASED.pop("Iphone 6")
phoneRELEASED["Nokia 3310"]=phoneRELEASED.pop("Galaxy A8")
phoneRELEASED["Nokia 3310"]=2000
phoneRELEASED["Lenovo A3600"]=2014

#sorting the items 
newdict=sorted(phoneRELEASED.items())

print("\n")

#printing the sorted items 
print(newdict)

