import math
import matplotlib.pyplot as plt
import random
import sys
import numpy as np

xpairs = []
ypairs = []

def rotate(x, y, a):
    rot_x = x*math.cos(a) - y*math.sin(a)
    rot_y = x*math.sin(a) + y*math.cos(a)
    return rot_x, rot_y

def make_branch(n, prev_x, prev_y, curr_x, curr_y, a_left, a_right, ratio_left, ratio_right):
    if n > 0:
        #left
        new_x = ratio_left*(curr_x - prev_x)
        new_y = ratio_left*(curr_y - prev_y)
        new_x, new_y = rotate(new_x, new_y, a_left)
        new_x += curr_x
        new_y += curr_y
        xpairs.append(curr_x)
        xpairs.append(new_x)
        xpairs.append(None)
        ypairs.append(curr_y)
        ypairs.append(new_y)
        ypairs.append(None)
        #recurse on branches
        make_branch(n-1, curr_x, curr_y, new_x, new_y, a_left, a_right, ratio_left, ratio_right)
        #right
        new_x = ratio_right*(curr_x - prev_x)
        new_y = ratio_right*(curr_y - prev_y)
        new_x, new_y = rotate(new_x, new_y, - a_right) #negate!
        new_x += curr_x
        new_y += curr_y
        xpairs.append(curr_x)
        xpairs.append(new_x)
        xpairs.append(None)
        ypairs.append(curr_y)
        ypairs.append(new_y)
        ypairs.append(None)
        #recurse on branches
        make_branch(n-1, curr_x, curr_y, new_x, new_y, a_left, a_right, ratio_left, ratio_right)
    else:
        return

def make_branch_random(n, prev_x, prev_y, curr_x, curr_y, a_left, a_right, ratio_left, ratio_right):
    if n > 0:
        #left
        ratio_left1 = np.random.normal(ratio_left, 1.2, 1)[0]
        a_left = np.random.normal(a_left, 0.5, 1)[0]
        new_x = ratio_left1*(curr_x - prev_x)
        new_y = ratio_left1*(curr_y - prev_y)
        new_x, new_y = rotate(new_x, new_y, a_left)
        new_x += curr_x
        new_y += curr_y
        xpairs.append(curr_x)
        xpairs.append(new_x)
        xpairs.append(None)
        ypairs.append(curr_y)
        ypairs.append(new_y)
        ypairs.append(None)
        #recurse on branches
        make_branch(n-1, curr_x, curr_y, new_x, new_y, a_left, a_right, ratio_left, ratio_right)
        #right
        ratio_right1 = np.random.normal(ratio_right, 0.5, 1)[0]
        a_right = np.random.normal(a_right, 0.3, 1)[0]
        new_x = ratio_right1*(curr_x - prev_x)
        new_y = ratio_right1*(curr_y - prev_y)
        new_x, new_y = rotate(new_x, new_y, - a_right) #negate!
        new_x += curr_x
        new_y += curr_y
        xpairs.append(curr_x)
        xpairs.append(new_x)
        xpairs.append(None)
        ypairs.append(curr_y)
        ypairs.append(new_y)
        ypairs.append(None)
        #recurse on branches
        make_branch(n-1, curr_x, curr_y, new_x, new_y, a_left, a_right, ratio_left, ratio_right)
    else:
        return

def make_branch_angle(n, prev_x, prev_y, curr_x, curr_y, a_left, a_right, ratio_left, ratio_right):
    if n > 0:
        #left
        a_left1 = int(np.random.normal(a_left, 0.7, 1)[0])
        number = int(np.random.normal(5, 1, 1)[0])
        for i in range(number):
            a_left1 += a_left/number
            new_x = ratio_left*(curr_x - prev_x)
            new_y = ratio_left*(curr_y - prev_y)
            new_x, new_y = rotate(new_x, new_y, a_left1)
            new_x += curr_x
            new_y += curr_y
            xpairs.append(curr_x)
            xpairs.append(new_x)
            xpairs.append(None)
            ypairs.append(curr_y)
            ypairs.append(new_y)
            ypairs.append(None)
            #recurse on branches
            make_branch(n-1, curr_x, curr_y, new_x, new_y, a_left1, a_right, ratio_left, ratio_right)
    else:
        return

if __name__ == '__main__':
    n = 12
    prev_x = 10
    prev_y = 0
    curr_x = 10
    curr_y = 10 #l = 10
    xpairs.append(prev_x)
    xpairs.append(curr_x)
    xpairs.append(None)
    ypairs.append(prev_y)
    ypairs.append(curr_y)
    ypairs.append(None)

    a_left = math.pi/6
    a_right = math.pi/4.5
    ratio_left = 0.6
    ratio_right = 0.8
    make_branch(n, prev_x, prev_y, curr_x, curr_y, a_left, a_right, ratio_left, ratio_right)
    #make_branch_random(n, prev_x, prev_y, curr_x, curr_y, a_left, a_right, ratio_left, ratio_right)
    #make_branch_angle(n, prev_x, prev_y, curr_x, curr_y, a_left, a_right, ratio_left, ratio_right)
    fig = plt.figure()
    #plt.style.use('ggplot')
    plt.plot(xpairs,ypairs,'k-',alpha=1, linewidth=0.6)
    plt.show()