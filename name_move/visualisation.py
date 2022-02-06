from matplotlib import pyplot as plt
import numpy as np

#super non_optimized code

#reading values
values = []
for i in range(3) :
    tr = []
    with open('try'+str(i)+'.txt', 'r') as t:
        for l in t.readlines() :
            n = len(l)
            data = l[1:n-1].split(', ')
            if ']' in data[len(data)-1] :
                data[len(data)-1] = data[len(data)-1][:len(data[len(data)-1])-2]
            data.pop(len(data)-1)    
            tr.append(data)
    values.append(tr)

#filtering data
for i in range(3):
    for j in range(40) :
        for k in range(12) :
            values[i][j][k] = int(values[i][j][k])
        values[i][j] = np.array(values[i][j])    
for i in range(3):
    for j in range(1, 40) :
        values[i][j] = 0.55*values[i][j-1] +  0.45*values[i][j] 

#rearanging values
Plotting_values = []
for i in range(3) :
    l1 = [values[i][k][0] for k in range(40) ]
    l2 = [values[i][k][1] for k in range(40) ]
    l3 = [values[i][k][2] for k in range(40) ]
    l4 = [values[i][k][3] for k in range(40) ]
    ax = [values[i][k][4] for k in range(40) ]
    ay = [values[i][k][5] for k in range(40) ]
    az = [values[i][k][6] for k in range(40) ]
    gx = [values[i][k][7] for k in range(40) ]
    gy = [values[i][k][8] for k in range(40) ]
    gz = [values[i][k][9] for k in range(40) ]
    mx = [values[i][k][10] for k in range(40) ]
    my = [values[i][k][11] for k in range(40) ]
    t = [l1, l2, l3, l4, ax, ay, az, gx, gy, gz, mx, my]
    Plotting_values.append(t)

labels = ['l1', 'l2', 'l3', 'l4', 'ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mx', 'my']
for j in range(12) :
    Y1 = Plotting_values[0][j]
    Y2 = Plotting_values[1][j]
    Y3 = Plotting_values[2][j]
    X = np.linspace(0, 2, 40)
    plt.plot(X, Y1)
    plt.plot(X, Y2)
    plt.plot(X, Y3)
    plt.title(labels[j])
    plt.savefig('with_filter/param'+str(j)+'.png')
    plt.show()
    
  