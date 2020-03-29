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
		self.state_names = ["Hungry", "Satisfied", "Scared", "Salty"]
		self.vector = [0.7,0.1,0.1,0.1]

	def get_chances(self, steps=1, vebose=True):
		for x in range(steps):
			self.vector = np.sum(self.matrix.T * self.vector, axis=1)

		if vebose:
			print("Result after", steps, "steps")
			print("-"*30)
			for i, x in enumerate(self.vector):
				print(self.state_names[i],":", round(x,3), "%")

		return self.vector

f = Flumph()
f.get_chances(10)