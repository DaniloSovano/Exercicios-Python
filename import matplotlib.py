import matplotlib.pyplot as plt
while True:
   
   
   
    def fatorial(a):
        fat = 1
        for i in range(1, a+1):
            fat *= i
        return fat 


    def plot_fatorial(n):
        x = list(range(n + 1))
        y = [fatorial(i) for i in x]
        plt.plot(x , y , marker= 'o', linestyle= '-')
        plt.title('Grafico Fatorial')
        plt.xlabel('Numero')
        plt.ylabel('Fatorial')
        plt.grid(True)
        plt.show()

    result = int(input('Insira o numero para o fatorial: '))

    print(plot_fatorial(result))