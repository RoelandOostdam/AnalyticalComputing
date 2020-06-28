import sys
import json

# arg_file = str(sys.argv[1]) # Command line input ophalen
# arg_file = 'example.json'
arg_file = 'example-2layer.json'
precision = 1 # Precisie van het aantal decimalen (in de voorbeelden altijd 1)

with open(arg_file) as json_file:
	data = json.load(json_file) # Bestand lezen
	first_layer = 1 # Wordt gebruikt om lege lijsten te initialiseren
	for layer in data:
		size_in = data[layer]['size_in'] # Aantal input nodes lezen
		size_out = data[layer]['size_out'] # Aantal output nodes lezen

		if(first_layer==1): # Lege input en output lijsten definiëren
			I = [1]*(int(size_in)+1)
			O = {}
		else:
			I = O # Output van vorige laag wordt de input van de volgende
		L = {} # Lane gewichten dict voor print onderaan

		for node in data[layer]['weights']: # Voor elke node
			l = 0.0 # Alle gewichten gecombineerd teller
			for lane in data[layer]['weights'][node]: # Voor elke lane
				l+=float(data[layer]['weights'][node][lane]) # Alle gewichten combineren
			O[int(node)] = round(I[int(node)]*l,precision) # Output van lane wordt input * gecombineerd gewicht
			L[int(node)] = round(l,precision)

		first_layer = 0 # Zorgt ervoor dat de input lijst niet opnieuw leeg gemaakt word.
		# Print statements
		print(layer)
		print("-"*30)
		for x in sorted(O):
			# print("L"+str(x),":",I[x],"----[*",L[x],"]---->",O[x])
			print("L" + str(x),"-->",O[x])
		print("-"*30)ghj