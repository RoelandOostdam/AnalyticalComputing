import numpy as np
import matplotlib.pyplot as plt


class Flumph():
	def __init__(self):
		self.matrix = np.array([ # Aanmaken van de kansentabel
			[0.8, 0.1, 0.1], # Vandaag hongerig
			[0.4, 0.5, 0.1], # Vandaag tevreden
			[0.6, 0.2, 0.2], # Vandaag Opgejaagd
		])
		self.state_names = ["Hungry", "Satisfied", "Scared"] # Naam van states
		self.vector = [0.7,0.1,0.2] # Begin vector/kansen

	def get_chances(self, steps=1):
		timeline = np.array([self.vector]) # Array om kansen bij te houden voor het plotten
		for x in range(steps): # Voor elke stap
			self.vector = np.sum(self.matrix.T * self.vector, axis=1) # Vector updaten
			timeline = np.concatenate((timeline, [self.vector])) # Toevoegen aan timeline

		print("Result after", steps, "steps")
		print("-"*30)
		for i, x in enumerate(self.vector):
			print(self.state_names[i],":", round(x,3), "%") # Kansen per staat na x steps

		for x in range(0,len(self.state_names)):
			plt.plot(range(0,steps+1),timeline.take(x,axis=1), label=self.state_names[x])
		plt.title("Markov Chain State Probability")
		plt.xlabel("Step")
		plt.ylabel("Probability (%)")

		plt.legend()
		plt.grid()
		plt.show()

		return self.vector

f = Flumph()
f.get_chances(10)