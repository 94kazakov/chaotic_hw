import math
import matplotlib.pyplot as plt

global m, grav, l, alpha, B, A
grav = 9.8
B = 0.25    
m = 0.1
l = 0.1
alpha = 7.73051559600005
A = 1

def rk4(q1, q2, h, t):
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
    return 1.0/(m*l)*((A*math.cos(alpha*t))-(B*l*omega)-m*grav*math.sin(theta))

def state_portrait(points):
    for theta, omega in points:
        h = 0.005
        t = 0.0
        thetas = [theta]
        omegas = [omega]
        ts = [t]

        while t <= 100:
            theta, omega = rk4(theta, omega, h, t)
            thetas.append(theta)
            omegas.append(omega)
            t += h
            ts.append(t)
        plt.plot(thetas, omegas)

def main():
    h = 3
    theta = 2
    omega = 0.0

    t = 0
    n = 0

    thetas = [theta]
    omegas = [omega]
    ts = [t]


    while t <= 100:
        theta, omega = rk4(theta, omega, h, t)
        thetas.append(theta)
        omegas.append(omega)
        t += h
        ts.append(t)
        n += 1

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
    samples_pts = [[3.14, 0.2], [3.14001, 0.2]]
    state_portrait(samples_pts)
    plt.xlabel(r'$\theta$', fontsize=24)
    plt.ylabel(r'$\omega$', fontsize=24)
    plt.show()

main()