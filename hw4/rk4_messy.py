import math
import matplotlib.pyplot as plt
import numpy as np
import random
# Denis Kazakov
# CSCI 4446

# RK4 with adaptie time stepper
# solves the given "equation" structure

# Lorenz system equation
# Input:    'pos'   - list    : current state of the system
#           'time'  - float   : current time of the system
# Output:   'dfdx'  - list    : derivative of the system at given "pos"
def equation(pos, time):
    #Parameters
    a = 16.0
    r = 45.0
    b = 4.0

    x = pos[0]
    y = pos[1]
    z = pos[2]

    dfdx = np.array([a*(y-x), r*x-y-x*z, x*y - b*z])
    return dfdx

# Take RK4 step
# Input:    'diffeq'    - function  : function with all equations
#           'h'         - int       : current step size
#           'x'         - list      : current position vector
#           't'         - int       : current time
# Output:   'x,t'                   : tuple of step calculation
def step(diffeq, h, x, t):
    k1 = h*diffeq(x, t)
    k2 = h*diffeq(x + (k1/2.0), t + (h/2.0))
    k3 = h*diffeq(x + (k2/2.0), t + (h/2.0))
    k4 = h*diffeq(x + k3, t+h)

    x = x + (k1 + 2*k2 +2*k3 + k4)/6
    t = t + h

    return x,t

# Find difference between RK4 taking a full step and two half steps
# Input:    'diffeq'            - function  : function with all equations
#           'h'                 - int       : current step size
#           'x'                 - list      : current position vector
#           't'                 - int       : current time
# Output:   'xs,ts, delta'                  : tuple of step calculation
def vary_step(diffeq, h, x, t):
    #full step
    xl, tl = step(diffeq, h, x, t)
    #two half steps
    xs, ts = step(diffeq, h/2, x, t)
    xs, ts = step(diffeq, h/2, xs, ts)
    #find delta between two step results
    delta = np.linalg.norm(xl - xs, np.inf)
    return xs, ts, delta


# Runner for adaptive RK4 method
# Control of step size
# Iterates over the system
# Input:    'diffeq'            - function  : function with all equations
#           'h'                 - int       : current step size
#           'x'                 - list      : current position vector
#           't'                 - int       : current time
# Output:   'points'            - np.array  : arrays of system coordinates
def adaptRK4(steps, diffeq, h, init):
    # desired accuracy
    TOL = 10**(-6) 
    # initialize system
    t = 0
    x = init
    xlist = []
    xlist.append(x)

    # take the first step
    x, t, delta = vary_step(diffeq, h, x, t)

    # Control step size
    for i in xrange(0, steps):

        # h step size is good as it is
        if (delta >= TOL - .05*TOL) and (delta <= TOL):
            x, t, delta = vary_step(diffeq, h, x, t)
            xlist.append(x)
            print "perfect"

        # h is too small
        if (delta < TOL - .05*TOL):
            h = h*2
            x, t, delta = vary_step(diffeq, h, x, t)
            xlist.append(x)
            print "too slow"

        while (delta > TOL) and (h > 10**(-10)):
            h = h/2
            # take the step, but don't record it until it's good
            x_trash, t_trash, delta = vary_step(diffeq, h, x, t)

        points = np.array(xlist)
        return points

if __name__ == '__main__':
    # initial conditinos
    init = np.array([-13.0, -12.0, 52.0])
    # calculate the system trajectory
    coordinates = adaptRK4(500, equation, .001, init)
    # plotting
    plt.plot(coordinates[:,0], coordinates[:,2], 'k.', markersize = 2)
    plt.title('Lorenz Attractor')
    plt.xlabel('x')
    plt.ylabel('z')
    plt.show()

