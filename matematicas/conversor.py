def dec_to_bin(num):
    return bin(num)

def dec_to_oct(num):
    return oct(num)

def dec_to_hex(num):
    return hex(num)

def bin_to_dec(num):
    return int(num, 2)

def oct_to_dec(num):
    return int(num, 8)

def hex_to_dec(num):
    return int(num, 16)

if __name__ == "__main__":
    num = int(input("Ingrese un número decimal: "))

    print("Binario: ", dec_to_bin(num))
    print("Octal: ", dec_to_oct(num))
    print("Hexadecimal: ", dec_to_hex(num))

    num = input("Ingrese un número binario: ")
    print("Decimal: ", bin_to_dec(num))
    print("Octal: ", oct(bin_to_dec(num)))
    print("Hexadecimal: ", hex(bin_to_dec(num)))

    num = input("Ingrese un número octal: ")
    print("Decimal: ", oct_to_dec(num))
    print("Binario: ", bin(oct_to_dec(num)))
    print("Hexadecimal: ", hex(oct_to_dec(num)))

    num = input("Ingrese un número hexadecimal: ")
    print("Decimal: ", hex_to_dec(num))
    print("Octal: ", oct(hex_to_dec(num)))
    print("Binario: ", bin(hex_to_dec(num)))
"""este programa permite ver por terminal la conversion de numeros de un sistema a otro
el programa solicitara el ingreso de un numero en diferentes sistemas de numeracion y ejecutara
la conversion en los restantes sitemas programados
Sofia Castillo 2023- IES MB 9009"""
