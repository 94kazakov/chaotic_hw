import math
import matplotlib.pyplot as plt
import random
import numpy
import sys

# t = plt.xlabel('my data', fontsize=14, color='red')
#HELPER FUNCTIONS
def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step


#INPUT: x0 - initial ratio
#		R - multiplying factor
#		n - number of point to predict
#		k - number of point to throw away
def get_rabbit_growth(x_0, R, n, k=0):
	#print "Rabbit Population creation"
	if (x_0 <= 1):
		x_n = x_0
	else:
		print('\n x_0 is a ratio, it lies within [0,1]')
		sys.exit(0)
	t = [] #time array
	X = [] #point predicted
	#array formation:
	for i in range(n):
		t.append(i)
		X.append(x_n)
		x_n = R*x_n*(1-x_n)
	return t[k:], X[k:]

def get_henon_map(x_old = 0.2, y_old = 0.2, a=0.2, b=0.3, n=100, k=0):
	X = [] #point predicted
	Y = []
	#array formation:
	for i in range(n):
		x_new = y_old + 1 - a*x_old**2
		y_new = b*x_old
		Y.append(y_new)
		X.append(x_new)
		x_old = x_new
		y_old = y_new
	return Y[k:], X[k:]

def plot_xn_vs_n(X, t, R):
	print "plotting xn_vs_n"

	plt.subplot(221)
	plt.scatter(t, X,label="R="+str(R))
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.ylabel('x_n')
	plt.xlabel('n')
	plt.title(r'$x_n$ vs. $n$')

#plot X[i+offset]  vs. X[i]
def plot_xnplus1_vs_xn(X, offset):
	print "plotting xnplus1_vs_xn"
	X_plus_offset = []
	for i in range(len(X) - offset):
		X_plus_offset.append(X[i + offset])
	X = X[:-offset] #cut out the offset
	#subplotting routine
	id = 221 + offset
	plt.subplot(id)
	#setting boundaries
	axes = plt.gca()
	#axes.set_xlim([0,1])
	#axes.set_ylim([0,1])
	#making y=x line
	x = numpy.linspace(0,1,10) # 100 linearly spaced numbers
	y = x
	plt.plot(x, y, '#ED5377')
	plt.scatter(X, X_plus_offset)
	#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.ylabel(r"$x_{n+" + str(offset) + "}$")
	plt.xlabel(r'$x_n$')
	plt.title(r"$x_{n+" + str(offset) + "}$ vs. ${x_n}$")

def show_chaos(R=3.6, n=100, k=0):
	t, X1 = get_rabbit_growth(0.2, R, n, k=0)
	t, X2 = get_rabbit_growth(0.20001, R, n, k=0)
	
	plt.plot(t, X1, 'r^',label="x_0 = 0.2")
	plt.plot(t, X2, 'bs', label="x_0 = 0.20001")
	plt.legend(bbox_to_anchor=(1., 1), loc=2, borderaxespad=0.)
	plt.ylabel('x_n')
	plt.xlabel('n')
	plt.title(r'Chaotic System (sensitive to initial conditions)')
	plt.show()

def find_feigenbaum(R_set, point_set):
	R_array = []
	exp_array = [] # store (R_value, exp_sum)
	for i in range(len(R_set)):
		current_R_set = point_set[i]
		R_value = R_set[i][0]
		exp_sum = 0
		for element in current_R_set:
			exp_sum += math.exp(element/8)
		#appending resulting coordinates
		R_array.append(R_value)
		exp_array.append(exp_sum)
	return R_array, exp_array

def plot_feigenbaum(R_array, exp_array):
	plt.scatter(R_array, exp_array, s=0.5, alpha = 0.5)
	plt.xlabel('R', fontsize=18)
	plt.title('Moment Generation Function', fontsize=18)
	plt.show()


def find_bifurcations(range_window=[2.8, 4], step_size=0.0001, m=50, n=100, x_0=0.2, type='rabbit'):
	R_set = []		# x - axis in bifurcation plot
	point_set = [] 	# y-axis in bifuraction plot
	for R in frange(range_window[0], range_window[1], step_size):
		if type == 'rabbit':
			t, X = get_rabbit_growth(x_0, R, n, n-m)
		elif type == 'henon':
			Y, X = get_henon_map(x_0, 0.2, R,0.3,n,n-m)
		R_set.append([R for i in range(m)]) #add [[R0,R0,...], [R1,R2,...], [R3,R3...],...]
		point_set.append(X)
	return R_set, point_set

def plot_bifurcations(R_set, point_set):
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	ax1.scatter(R_set, point_set, s=0.05, alpha = 0.5)
	plt.show()

def find_feigenbaum_limit(fein_arr):
	old_fein = fein_arr[1]-fein_arr[0]
	average = 0
	print "distance is:{}".format(old_fein)
	for i in range(1, len(fein_arr)-1):
		print "locatin is {}".format(fein_arr[i])
		print str(old_fein/(fein_arr[i+1]-fein_arr[i])) + '\n'
		average += old_fein/(fein_arr[i+1]-fein_arr[i])
		old_fein = fein_arr[i+1]-fein_arr[i]
		print "distance is:{}".format(old_fein)
	print 'AVERAGE:{} \n\n'.format(average/(len(fein_arr)-2))

if __name__ == '__main__':
	x_0 = 0.7223
	R = 4.1
	n = 100
	k = 0

	#Homework 1:
	#plot all graphs on the same figure
	'''
	t, X = get_rabbit_growth(x_0, R, n, k)
	plt.figure(1)
	plot_xn_vs_n(X, t, R)
	plot_xnplus1_vs_xn(X, 1)
	plot_xnplus1_vs_xn(X, 2)
	plot_xnplus1_vs_xn(X, 3)
	plt.show()

	#show_chaos()
	'''

	#Homework 2:
	print "finding bifuractions..."
	R_set, point_set = find_bifurcations()
	print "plotting bifuractions..."
	plot_bifurcations(R_set, point_set)
	print "find_feigenbaum..."
	#R_array, exp_array = find_feigenbaum(R_set, point_set)
	print "plot_feigenbaum..."
	#plot_feigenbaum(R_array, exp_array)
	print "finding henon bifuractions..."
	a_set, point_set = find_bifurcations([0, 1.4], type='henon')
	print "plotting henon bifuractions..."
	plot_bifurcations(a_set, point_set)
	print "find henon feigenbaum..."
	#a_array, exp_array = find_feigenbaum(a_set, point_set)
	print "plot henon feigenbaum..."
	#plot_feigenbaum(a_array, exp_array)
	print "fein limit"
	find_feigenbaum_limit([2.94,3.429,3.54,3.561])
	find_feigenbaum_limit([0.27,0.880,1.015,1.0445])