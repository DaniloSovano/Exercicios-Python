import matplotlib.pyplot as plt
import numpy as np

calculator = """
 _________________
|  _____________  |
| |_CALCULADORA_| |
| |             | |
| | x² √  CE  C | |
| | 7  8  9   / | |
| | 4  5  6   * | |
| | 1  2  3   - | |
| | 0  .  =   + | |
| |_____________| |
|_________________|
    """
print(calculator)


def soma(a, b):
    soma = a + b
    return soma

def subtracao(a, b):
    sub = a-b
    return sub


def multiplicacao(a, b):
    mult = a * b
    return mult


def divisao(a, b):
    div = a/b
    return div


def linear(x, a, b):
    lin = (a * x) + b
    return lin

def plot_linear(x):
   plt.plot(linear(x)) 


def exponencial(a, x):
    exp = a ** x
    return exp


def plot_exponencial(x, y):
    plt.plot(exponencial(x))

def funcao_quadratica(x, a, b, c):
    print("Faça o código")


def calcular_raizes(a, b, c):
    print("Faça o código")


def plot_quadratica(a, b, c):
    print("Faça o código")


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

def print_calculator():

    mostrarCalculadora("""Inicie uma operação       
                                
    1: Básicas
    2: Funções 
    3: Sair""")


def print_basica():
    mostrarCalculadora("""Escolha sua  Opção     
                       
  1: Soma       
  2: Subtração  
  3: Multip.   
  4: Divisão    
  5: Voltar""")


def print_funcoes():
    mostrarCalculadora("""Escolha sua Função    
                                 
      1: Exponencial        
      2: Quadrática    
      3: Linear    
      4: Fatorial
      5. Voltar""")


def init():
    print_calculator()

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print_basica()

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    print("Faça o código")
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    print("Faça o código")
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    print("Faça o código")
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    print("Faça o código")
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    print("Faça o código")
                    break

                elif funcao == 2:
                    print("\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    print("Faça o código")
                    break

                elif funcao == 3:
                    print("\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    print("Faça o código")
                    break

                elif funcao == 4:
                    print("\nVocê escolheu a função FATORIAL f(x) = (a * x + b)")
                    print("Faça o código")
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()