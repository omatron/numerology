



global i
global j
global j0

i = 0
j = 0
j0 = 0
soma = 0
debug = 0
somaTotal = 0
somaNome = 0
numbers = []


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s == 10:
        s = 1
    return s

print('Digite seu nome completo: ')

myName = input()



while i < len(myName):
    
        
    if myName[i] == ' ':
        numbers = numbers + [soma]
        
        while j != i:
            print(myName[j])
            j = j + 1
        print('**********')
        print(str(soma) + ' = ' + str(sum_digits(soma)))
        somaTotal = somaTotal + sum_digits(soma)
        
        somaNome = ''
        soma = 0
        
        
    
    if myName[i] == 'a' or myName[i] == 'j' or myName[i] == 's' or myName[i] == 'A' or myName[i] == 'J' or myName[i] == 'S':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 1



    if myName[i] == 'b' or myName[i] == 'k' or myName[i] == 't' or myName[i] == 'B' or myName[i] == 'K' or myName[i] == 'T':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 2
        

    if myName[i] == 'c' or myName[i] == 'l' or myName[i] == 'u' or myName[i] == 'C' or myName[i] == 'L' or myName[i] == 'U':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 3   



    if myName[i] == 'd' or myName[i] == 'm' or myName[i] == 'v' or myName[i] == 'D' or myName[i] == 'M' or myName[i] == 'V':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 4   



    if myName[i] == 'e' or myName[i] == 'n' or myName[i] == 'w' or myName[i] == 'E' or myName[i] == 'N' or myName[i] == 'W':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 5   



    if myName[i] == 'f' or myName[i] == 'o' or myName[i] == 'x' or myName[i] == 'F' or myName[i] == 'O' or myName[i] == 'X':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 6   



    if myName[i] == 'g' or myName[i] == 'p' or myName[i] == 'y' or myName[i] == 'G' or myName[i] == 'P' or myName[i] == 'Y':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 7   



    if myName[i] == 'h' or myName[i] == 'q' or myName[i] == 'z' or myName[i] == 'H' or myName[i] == 'Q' or myName[i] == 'Z':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 8   



    if myName[i] == 'i' or myName[i] == 'r' or myName[i] == 'I' or myName[i] == 'R':
        if debug == 1:
            print(myName[i])
            print('na posicao ' + str(i+1))

        soma = soma + 9   




    i = (i + 1)



if len(myName) > 1:

    while j != i:
            print(myName[j])
            j = j + 1
    #print(somaNome + ' ')
    print('**********')
    print(str(soma) + ' = ' + str(sum_digits(soma)))
    somaTotal = somaTotal + sum_digits(soma)

    somaNome = ''
    soma = 0



    if somaTotal == 11 or somaTotal == 22 or somaTotal == 33:
        print('A soma total deu: ' + str(somaTotal))
    else:
        print('A soma total deu: ' + str(sum_digits(somaTotal)))

else:
    print('Nome Inválido!!!')


input('Press <ENTER> to continue')
    





