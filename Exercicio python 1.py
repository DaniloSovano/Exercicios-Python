Num1 = int(input('insira o primeiro numero:'))
Num2 = int(input('insira o segundo numero:'))
soma =  (Num1 + Num2)
sub = (Num1 - Num2)
multi = (Num1 * Num2)
div = (Num1 // Num2)
rest = (Num1 % Num2)
print( f'a soma de {Num1} + {Num2} é: {soma}')
print( f'a subtração de {Num1} - {Num2} é: {sub}')
print(f'a multiplicação de {Num1} * {Num2} é: {multi}')
print( f'a divisão de {Num1} por {Num2} é: {div}')
print( f'O resto da divisão de {Num1} por {Num2} é: {rest}')
echo "# Exercicios-Python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/DaniloSovano/Exercicios-Python.git
git push -u origin main