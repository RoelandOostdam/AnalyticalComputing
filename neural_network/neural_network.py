import sys
import json

arg_file = str(sys.argv[1])
# arg_file = 'example-2layer.json'
precision = 1

with open(arg_file) as json_file:
	data = json.load(json_file)
	first_layer = 1
	for layer in data:
		size_in = data[layer]['size_in']
		size_out = data[layer]['size_out']

		if(first_layer==1):
			I = [1]*(int(size_in)+1) # Define input vector
			O = {} # Output vector
		else:
			I = O

		for node in data[layer]['weights']:
			l = 0.0 # All transition weights combined counter
			for target_node in data[layer]['weights'][node]:
				l+=float(data[layer]['weights'][node][target_node])
				O[int(node)] = round(I[int(node)]*l,precision)

		print(layer)
		print("-"*30)
		for x in O:
			print("L"+str(x),"-->",O[x])
		print("-"*30)
		first_layer = 0