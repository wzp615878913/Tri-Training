import numpy as np 
import matplotlib.pyplot as plt


class Graphic:
	""" 结果可视化 """

	def __init__(self, data):		
		self.Data = data
		self.x = range(len(data))

	def display(self):
		plt.xticks(self.x)
		plt.xlabel("(round)")
		plt.ylabel('(accuracy rate)')
		plt.title('Tri-Training')
		plt.plot(self.Data,'b-o')
		plt.grid()
		plt.show()


if __name__ == "__main__":

	G = Graphic([0.72, 0.772, 0.89,0.89])
	G.display()