import math
import matplotlib.pyplot as plt

global m, grav, l, alph, B, A
grav = 9.8
B = 0.25
m = 0.1
l = 0.1
alph = 0.5
A = 1

# t = plt.xlabel('my data', fontsize=14, color='red')
#HELPER FUNCTIONS
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def rk4(q1, q2, h, t):
    global weight
    k1 = h * f(t, q2)
    l1 = h * g(t, q1, q2)
    k2 = h * f(t + (0.5*h), q2 + (0.5*l1))
    l2 = h * g(t + (0.5*h), q1 + (0.5*k1), q2 + (0.5*l1))
    k3 = h * f(t + (0.5*h), q2 + (0.5*l2))
    l3 = h * g(t + (0.5*h), q1 + (0.5*k2), q2 + (0.5*l2))
    k4 = h * f(t + h, q2 + l3)
    l4 = h * g(t + h, q1 + k3, q2 + l3)
    theta = q1 + (k1 + 2.0*(k2 + k3) + k4)/6.0
    omega = q2 + (l1 + 2.0*(l2 + l3) + l4)/6.0
    return theta, omega


def f(t, omega):
    return omega

def g(t, theta, omega):
    return 1.0/(m*l)*((A*math.cos(alph*t))-(B*l*omega)-m*grav*math.sin(theta))

def state_portrait(points):
    for theta, omega in points:
        h = 0.005
        t = 0.0
        thetas = [theta]
        omegas = [omega]
        ts = [t]

        while t <= 3:
            theta, omega = rk4(theta, omega, h, t)
            thetas.append(theta % (math.pi*2))
            omegas.append(omega)
            t += h
            ts.append(t)
        plt.plot(thetas, omegas, alpha=0.4)

def find_chaos(points):
    for theta, omega in points:
        h = 0.005
        t = 0.0
        thetas = [theta]
        omegas = [omega]
        ts = [t]

        while t <= 3:
            theta, omega = rk4(theta, omega, h, t)
            thetas.append(theta % (math.pi*2))
            omegas.append(omega)
            t += h
            ts.append(t)
        plt.plot(thetas, omegas, alpha=0.4)


def find_bifurcations(points, range_window=[7.0, 9]):
    global alph
    alpha_set = []      # x - axis in bifurcation plot
    point_set = []      # y - axis in bifuraction plot
    for a in frange(range_window[0], range_window[1], 0.001):
        alph = a
        print a
        omegas = []
        thetas = []
        for theta, omega in points:
            h = 0.05
            t = 0.0
            ts = [t]

            while t <= 60:
                theta, omega = rk4(theta, omega, h, t)
                thetas.append(theta)
                omegas.append(omega)
                t += h
                ts.append(t)

        omegas = omegas[100:]
        thetas = thetas[100:]

        alpha_set.append([alph for i in range(len(thetas))]) #add [[R0,R0,...], [R1,R2,...], [R3,R3...],...]
        point_set.append(omegas)

    return alpha_set, point_set



def plot_bifurcations(R_set, point_set):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(R_set, point_set, s=0.05, alpha = 0.5)
    plt.xlabel(r'$\alpha$', fontsize=24)
    plt.ylabel(r'$\omega$', fontsize=24)
    plt.show()

def main():
    h = 0.005
    theta = 2
    omega = 0.0
    t = 0
    n = 0
    thetas = [theta]
    omegas = [omega]
    ts = [t]
    '''
    while t <= 2000:
        theta, omega = rk4(theta, omega, h, t)
        thetas.append(theta)
        omegas.append(omega)
        t += h
        ts.append(t)
        n += 1
    '''
    '''
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(ts, thetas, label="Theta")
    ax1.plot(ts, omegas, label="Omega")
    ax1.legend(bbox_to_anchor=(0.8, 1), loc=2, borderaxespad=0.)
    ax2 = fig.add_subplot(212)
    ax2.plot(thetas, omegas, label="Omega")
    plt.show()'''

  
    '''plt.plot(thetas, omegas, label="\r'\theta'")'''
    '''
    samples_pts = [[3.14 - math.pi*4, 0.5] ,
     [3.13 + math.pi*6 - math.pi*4, -0.5] , 
     [2.2 - math.pi*4, 0.1],
     [1.1 - math.pi*4, 0.0], 
     [3.12 - math.pi*4, 20],
     [3.11 - math.pi*4, 40],
     [3.13 + math.pi*10 - math.pi*4, -20],
     [3.10 + math.pi*10 - math.pi*4, -40],
     [2.0 + math.pi*2 - math.pi*4, 0.1],
     [1.0 + math.pi*2 - math.pi*4, 0.0],
     [2.0 + math.pi*4 - math.pi*4, 0.1],
     [1.0 + math.pi*4 - math.pi*4, 0.0],
     [2.0 + math.pi*6 - math.pi*4, 0.1],
     [1.0 + math.pi*6 - math.pi*4, 0.0]]
    state_portrait(samples_pts)
    plt.xlabel(r'$\theta$', fontsize=24)
    plt.ylabel(r'$\omega$', fontsize=24)
    plt.show()'''

    
    samples_pts = [[3.14, 3]]

    print "finding bifuractions..."
    R_set, point_set = find_bifurcations(samples_pts)
    print "plotting bifuractions..."
    plot_bifurcations(R_set, point_set)
    
main()
