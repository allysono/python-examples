# For é perfeito para trabalhar com listas no python, indo de um valor inicial para um valor final. Ele é limitado, diferente do while, que pode ser infinito. 

num  = ["1", "2", "3", "4"]

letras = []

frase = 'Teste com For - Python'

#Printar todos os numeros de uma lista
for a in num:
    print(a)

#Printar todas as lestras (string) de uma lista
for a in frase:
    print(a)
    
# Printar todos os numeros de um range de 1 a 10 (lembrando que nesse caso começa do 0)
for x in range(10):
    print (x)

# Printar todos os numeros de 1 a 10 (começando do 3)
for x in range(3,10):
    print (x)
    
# Printar todos os numero de 1 a 10 de dois em dois (isso chama PASSO)    
for x in range(1,10, 2):
    print (x)    
    
# Printar os numeros na sequencia inversa
for y in range(100, 0, -2):
    print(y)
    
# Printar o alfabeto e salvar na variavel letras
for y in range(97, 97 + 26):
    letras.append(chr(y))
    
    print(letras)