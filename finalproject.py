menu = '''
Bem vindo a caculadora!!
Escolha a operação que você deseja realizar.
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
5: Potenciação
6: Fatorial
7: Sair
'''
print(menu)



    

def adição(a,b):
        soma = a + b
        return soma

def subtração(a,b):
    sub = a-b
    return sub
def multiplicação(a,b):
    mult = a * b
    return mult
def divisão(a,b):
    div = a/b
    return div
def potencia(a,b):
    pot = a ** b
    return pot

def fatorial1(a):
    if a == 0:
        return 1
    elif a<0:
        print('erro')
    else:
        fatorial = 1
        for i in range(1, a+1):
            fatorial *= i
            
        return fatorial
    


while True:
    resposta = input('Escolha uma opção:')
    if resposta in ('1','2','3','4','5'):
        a = int(input('Digite o primeiro numero:'))
        b = int(input('Digite o segundo numero:'))
        
        if resposta == '1':
            resultado = adição(a,b)
            print(f'O seu resultado é: {resultado}')
        elif resposta == '2':
            resultado = subtração(a,b)
            print(f'O seu resultado é: {resultado}')
        elif resposta == '3':
            resultado = multiplicação(a,b)
            print (f'O seu resultado é: {resultado}')
        elif resposta == '4':
            resultado = divisão(a,b)
            print(f'O seu resultado é: {resultado}')
        elif resposta == '5':
            resultado = potencia(a,b)
            print(f'O seu resultado é: {resultado}')
    
    elif resposta in ('6'):
        fat = int(input('Digite seu numero para fatorial: '))
        resultado = fatorial1(fat)
        print(f'O seu resultado é: {resultado}')
    elif resposta in ('7'):
        print('Até a próxima')
        break
    
    
    