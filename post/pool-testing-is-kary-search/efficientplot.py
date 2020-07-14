import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Plot the efficient region.
    fig, ax = plt.subplots()
    x = [i for i in np.arange(1.0, 40.0, 0.01)]
    y = [1 - math.pow(i, -1/i) for i in x]
    ax.plot(x, y, color='C0', linestyle='--')
    ax.fill_between(x, 0, y, alpha=-0.4, facecolor='C0')

    plt.xlim(right=39)
    ax.set(title='Pool Testing\'s \"Efficient Region\" by Pool Size', xlabel='Pool Size', ylabel='Infection Rate')
    ax.grid()
    fig.savefig('efficientplot.png', dpi=300)
