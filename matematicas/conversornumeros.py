decimal = int(input("Ingrese un número decimal: "))

binario = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)

print("El número decimal {} equivale en binario a {}".format(decimal, binario))
print("El número decimal {} equivale en octal a {}".format(decimal, octal))
print("El número decimal {} equivale en hexadecimal a {}".format(decimal, hexadecimal))

"""este programa hace una conversion simple de numeros decimales hacia los otros sistemas de numeracion programados
Sofia Castillo 2023- IES MB 9008"""