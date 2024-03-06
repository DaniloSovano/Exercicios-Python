import matplotlib.pyplot as plt
    
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
    

def função(a,b,c):
    delta = (b** 2) - 4 * a * c
    
    if delta > 0:
        raiz1 = ((-b) + (delta ** 0.5)) / ( 2 * a)
        raiz2 = ((-b) - (delta ** 0.5)) / ( 2 * a)
        return raiz1,raiz2
    
    elif delta == 0:
        raiz1 = (-b) / (2 * a)
        return raiz1
    else:
        print('Delta negativo não possui raizes')

resultado = função(a,b,c)

plt.bar(resultado)
plt.show()
print(resultado)
