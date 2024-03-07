import matplotlib.pyplot as plt
import numpy as np

while True:
    
    def linear(x,a,b):
        return (a * x) + b
    
    def plot_linear(a,b):
        axisx = np.linspace(-10,10,100)
        axisy = linear(axisx, a , b)
        plt.plot(axisx,axisy, )
        plt.title(f'Grafico da função linear {a}x + {b}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        
        plt.show()
    break
print(plot_linear(5,9))