import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Plot the tests saved for various pool sizes.
    fig, ax = plt.subplots()
    x = [i for i in np.arange(0.0, 1.01, 0.01)]
    ax.plot(x, [(math.pow(1 - i, 4) - 1.0/4.0) * 100 for i in x], color='C0', label='Pools of 4')
    ax.plot(x, [(math.pow(1 - i, 8) - 1.0/8.0) * 100 for i in x], color='C1', label='Pools of 8')
    ax.plot(x, [(math.pow(1 - i, 16) - 1.0/16.0) * 100 for i in x], color='C2', label='Pools of 16')
    ax.plot(x, [(math.pow(1 - i, 32) - 1.0/32.0) * 100 for i in x], color='C3', label='Pools of 32')

    plt.xlim(-0.02, 0.42)
    plt.ylim(-24, 104)
    ax.set(title='Tests Saved with One Round of Pool Testing', xlabel='Infection Rate', ylabel='% Tests Saved')
    ax.grid()
    ax.legend(loc='upper right')
    fig.savefig('savingsplot.png', dpi=300)
