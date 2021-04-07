def checkHex(s):
    if s == 10:
        return 'A'
    elif s == 11:
        return 'B'
    elif s == 12:
        return 'C'
    elif s == 13:
        return 'D'
    elif s == 14:
        return 'E'
    elif s == 15:
        return 'F'
    else:
        return s


def binToExa(n):
    n = list(n)
    aux = ''
    n1 = []

    while len(n) > 0:
        x = 0
        aux = ''
        while x <= 3 and len(n) > 0:
            aux = n.pop() + aux[0:]
            x = x + 1
        n1.insert(0, aux)

    aux = []
    for x in n1:    
        aux.append(checkHex(binTo(x)))
    return aux


def binToOcta(n):
    n = list(n)
    aux = ''
    n1 = []

    while len(n) > 0:
        x = 0
        aux = ''
        while x <= 2 and len(n) > 0:
            aux = n.pop() + aux[0:]
            x = x + 1
        n1.insert(0, aux)

    aux = []
    for x in n1:    
        aux.append(binTo(x))
    return aux


def binTo(n):
    exp = len(n) - 1
    aux = 0
    cont = 0

    for x in n:
        # operação de conversão
        aux = aux + (int(x) * (2 ** exp))
        # impressão
        if exp == 0:
            print("2^", exp, "*", x)
        else:
            print("2^", exp, "*", int(n[cont]), " + ", end=" ")
        exp = exp - 1

    print(n, "→", aux)
    return aux


def checkStr(s):
    if s == 'A':
        return 10
    elif s == 'B':
        return 11
    elif s == 'C':
        return 12
    elif s == 'D':
        return 13
    elif s == 'E':
        return 14
    elif s == 'F':
        return 15
    else:
        return int(s) 


def divisions(D):
    numberI = []    
    results = ""
    OLD = D
    print(D," em binário: ")
    while D >= 1:
        R = D % 2
        numberI.append(int(R))
        old = int(D)
        D = int(D)/2
        print(old, "/", 2, "=", D, "→", old, "%", 2, "=", int(R))
    
    numberI = numberI[::-1] 
    
    print(OLD, " ---------- ", end="")

    for x in numberI:
        results += str(x)
    
    print(results)
    
    return results


def correctToHexa(n):
    if len(n) < 4:
        while (4 - len(n)) > 0:
            n = "0" + n[0:]
    return n


def correctToOcta(n):
    if len(n) < 3:
        while (3 - len(n)) > 0:
            n = "0" + n[0:]
    return n


def convertOctaToB(n):
    results = ""
    for x in n:    
        for y in str(correctToOcta(divisions(checkStr(x)))):
            results += y
    return results


def convertHexToB(n):
    results = ""    
    for x in n:    
        for y in str(correctToHexa(divisions(checkStr(x)))):
            results += y
    return results


def exaToOcta(n):
    results = ''
    aux = []
    print("Convertendo para binário:")
    aux = convertHexToB(n)
    print("Convertendo para octal:")
    for x in binToOcta(aux):
        results += str(x)
    return results


def main():
    n = []
    results = " "
    op = " "
    print("**CONVERSOR BINARIO PARA HEXADECIMAL OU OCTAL**")

    # menu
    op = input("Digite:\n1 --------- bin to hexa\n2 --------- bin to octa\n3 --------- hexa to octa\n4 --------- hexa to bin and dec\n5 --------- octa to bin and dec\n🐱‍💻: ")

    if op == "1":
        # entradas do teclado
        n = input('Entre com o binario para conversão em hexadecimal (digite apenas números binários): ')
        results = binToExa(n)
        print("\n", n, "em hexadecimal:",end=" ")
        for x in results:
            print(x, end="")

    elif op == "2":
        # entradas do teclado
        n = input('Entre com o binario para conversão em octal (digite apenas números binários): ')
        results = binToOcta(n)
        print("\n", n, "em octal:",end=" ")
        for x in results:
            print(x, end="")

    elif op == "3":
        # entradas do teclado
        n = input('Entre com o Hexadecimal para conversão em octal(digite letras maiusculas): ')
        results = exaToOcta(n)
        print("\n", n, "em octal:", results)
    
    elif op == "4":
        # entradas do teclado
        n = input('Entre com o Hexadecimal para conversão em binário e decimal (digite letras maiusculas): ')
        print("Conversão em binário")
        results = convertHexToB(n)
        print("\n", n, "em binário:", results)
        print("\nConversão em decimal:")
        results = binTo(results)
        print("\n", n, "em decimal:", results)

    elif op == "5":
        # entradas do teclado
        n = input('Entre com o Octal para conversão em binário e decimal (digite letras maiusculas): ')
        print("Conversão em binário")
        results = convertOctaToB(n)
        print("\n", n, "em binário:", results)
        print("\nConversão em decimal:")
        results = binTo(results)
        print("\n", n, "em decimal:", results)

    elif op == "secret":
        # entradas do teclado
        n = input('Entre com o binario para conversão (digite apenas números binários): ')
        results = binTo(n)
        print("\n", n, "em decimal:", results)
    
    else:
        print("Opção inválida 😪")

    # controlador do menu
    op = input('\nDigite 0 para sair...\nOu qualquer outra tecla pra continuar...')
    if op != '0':
        main()


# start da aplicação
main()
