import numpy as np
import matplotlib.pyplot as plt


def draw(num, steps, title):
    plt.plot(num, steps, 'r')
    plt.xlabel('Number of inputs')
    plt.ylabel('Number of steps')
    plt.title(title)
    plt.show()


num_of_inputs = np.array(list(range(10)))
steps = [2 for n in num_of_inputs]
steps_mul_2 = [n * 2 for n in num_of_inputs]
steps_pow_2 = [n ** 2 for n in num_of_inputs]

draw(num_of_inputs, steps, "O(c)")
draw(num_of_inputs, steps_mul_2, "O(n)")
draw(num_of_inputs, steps_pow_2, "O(n^2)")
