"""
Written by Ryan Skeele
Robot Decision Making Laboratory
Oregon State University

"""
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d
import random

i=0


while (i <= 3):

	fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
	N = 100
	X, Y = np.meshgrid(range(N), range(N))
	heights = 0 #np.sin(np.pi*np.sqrt(X**2+Y**2)/N)+np.cos(np.sqrt(X**2+Y**2))
	
	print X, Y
	colors = []
	for y in range(N):
		colors.append([])

		for x in range(N):
			samples=['#228B22', '#7CFC00', '#32CD32']
			# samples = [0.5]
			colors[y].append(random.choice(samples))


	print (colors)
	t1= random.randint(0,N-1)
	t2= random.randint(0,N-1)
	print t1
	print t2
	colors[t1][t2] = 'r'

			
	#for y in range(N):
	#	for x in range(N):
	#		if colors[x][y] is 'r':
	#			colors[x][y]= 'r'
	#		else:
	#			colors[x][y]= colors[x][y]
	
	


	ax.plot_surface(X, Y, heights, rstride=1, cstride=1, facecolors= colors)
	plt.show()
	#print colors
	i=4

