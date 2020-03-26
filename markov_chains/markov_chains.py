import numpy as np
import matplotlib.pyplot as plt

class Flumph():
	def __init__(self):
		self.matrix = np.array([
			[0.6, 0.1, 0.1, 0.2],
			[0.4, 0.3, 0.2, 0.1],
			[0.6, 0.1, 0.1, 0.2],
			[0.1, 0.1, 0.3, 0.5]
		])
		self.states = ["Hungry", "Satisfied", "Scared", "Salty"]
		self.current_state = "Hungry"

	def next_state(self):
		if self.current_state == "Hungry":
			choice = np.random.choice(self.states, p=self.matrix[0])
		elif self.current_state == "Satisfied":
			choice = np.random.choice(self.states, p=self.matrix[1])
		elif self.current_state == "Scared":
			choice = np.random.choice(self.states, p=self.matrix[2])
		elif self.current_state == "Salty":
			choice = np.random.choice(self.states, p=self.matrix[3])

		self.current_state = choice

def simulate(f, steps):
	counts = {
		'Hungry':1,
		'Satisfied':0,
		'Scared':0,
		'Salty':0
	}
	for x in range(0,steps):
		f.next_state()
		counts[f.current_state] += 1

	counts['Hungry'] /= steps
	counts['Satisfied'] /= steps
	counts['Scared'] /= steps
	counts['Salty'] /= steps
	return counts

def mass_run(f, runs, steps):
	results = {
		'Hungry': [],
		'Satisfied': [],
		'Scared': [],
		'Salty': []
	}
	for run in range(0,runs):
		res = simulate(f, steps)
		results['Hungry'].append(res['Hungry'])
		results['Satisfied'].append(res['Satisfied'])
		results['Scared'].append(res['Scared'])
		results['Salty'].append(res['Salty'])

	return results

f = Flumph()

simulations = range(1,100)
mass_results = {
	'Hungry': [],
	'Satisfied': [],
	'Scared': [],
	'Salty': []
}
for simulation in simulations:
	results = mass_run(f, 10, simulation)
	avg_hungry = np.average(results['Hungry'])
	avg_satisfied = np.average(results['Satisfied'])
	avg_scared = np.average(results['Scared'])
	avg_salty = np.average(results['Salty'])
	mass_results['Hungry'].append(avg_hungry)
	mass_results['Satisfied'].append(avg_satisfied)
	mass_results['Scared'].append(avg_scared)
	mass_results['Salty'].append(avg_salty)

# print(results)
plt.plot(range(0,len(mass_results['Hungry'])), mass_results['Hungry'], label='Hungry')
plt.plot(range(0,len(mass_results['Satisfied'])), mass_results['Satisfied'], label='Satisfied')
plt.plot(range(0,len(mass_results['Scared'])), mass_results['Scared'], label='Scared')
plt.plot(range(0,len(mass_results['Salty'])), mass_results['Salty'], label='Salty')

plt.title("Probability of states after x steps")
plt.ylabel("Probability (%)")
plt.xlabel("Steps")
plt.ylim([0,1])
plt.xlim([0,len(simulations)+1])

plt.legend()
plt.grid()
plt.show()