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

	def get_chances(self, steps=1):
		timeline = np.array([self.vector])
		for x in range(steps):
			self.vector = np.sum(self.matrix.T * self.vector, axis=1)
			timeline = np.concatenate((timeline, [self.vector]))

		print("Result after", steps, "steps")
		print("-"*30)
		for i, x in enumerate(self.vector):
			print(self.state_names[i],":", round(x,3), "%")

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
f.get_chances(100)