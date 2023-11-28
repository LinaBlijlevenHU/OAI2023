"""
function_plots.py

An example of different functions in the same plot.
Note: this makes the plot unreadable. The best way to explore
these functions is to start by adding the constant and linear function,
then uncommenting others to eventually understand the full picture and scope of
these big functions.

These functions all represent different classes of complexity for computer algorithms.

Teacher's note: it's pretty easy to write the code to consider the whole list at once (instead of iterating),
but the code was aimed at beginner programmers.
"""
import matplotlib.pyplot as plt
import numpy as np
import math

def constant(x):
    '''
    Constant function: always has the same outcome, in this case 1.

    Note: the underscore is an anonymous variable. We could give it a
    name, but it doesn't actually matter. Only the number of points matters,
    so we can generate all the ones.

    :param x:  array   Different x-values
    :return x: array   Array of y values for every x
    '''
    return [1 for _ in x]

def linear(x):
    '''
    A linear function where y = x.

    :param  x:  array   List of x values
    :return y: array   the same array really
    '''
    return [val for val in x]

def quadratic(x):
    '''
    A quadratic function that squares each element in a list or range.

    :param  array   List of x values
    :return array   Y values for the quadratic function
    '''
    return [val**2 for val in x]

def exponential(x):
    '''
    An exponential function. These grow very very fast.

    :param  array   List of x values
    :return array   Corresponding y values for the exponential function
    '''
    return [2**val for val in x]

def factorial(x):
    '''
    Factorial function that grows super super fast. (that's faster than very very fast)

    :param x:   array   List of x values
    :return:    array   Corresponding y values for the factorial function
    '''
    return [math.factorial(val) for val in x]

# Generate x values
x_values = np.arange(0, 1001, 50)

# Plot the functions
# Note: when uncommenting the lower functions, the upper functions will become
# near impossible to read.
plt.plot(x_values, constant(x_values), label='Constant (y=1)', color='blue')
plt.plot(x_values, linear(x_values), label='Linear (y=n)', color='green')
plt.plot(x_values, quadratic(x_values), label='Quadratic (y=n^2)', color='red')
plt.plot(x_values, exponential(x_values), label='Exponential (y=2^n)', color='purple')
#plt.plot(x_values, factorial(x_values), label='Factorial (y=n!)', color='orange')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0, 1000)
plt.title('Plot of Different Functions')
plt.legend()

# Show the plot
plt.show()
