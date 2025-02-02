def binario_para_decimal(bin_str):
    return int(bin_str, 2)

def decimal_para_binario(num):
    return bin(num)[2:]

def c2(bin_str):
    if bin_str[0] == '1':  
        valor = -(int(bin_str[1:], 2)) - 1
    else:
        valor = int(bin_str[1:], 2)
    return valor

def sm(bin_str):
    if bin_str[0] == '1':  
        return -int(bin_str[1:], 2)
    else:
        return int(bin_str[1:], 2)

def fixo(bin_str):
    inteiro = int(bin_str[:6], 2)
    fracao = sum(int(bit) * (2 ** -(i + 1)) for i, bit in enumerate(bin_str[6:]))
    return inteiro + fracao

def float(bin_str):
    sinal = -1 if bin_str[0] == '1' else 1
    expoente = int(bin_str[1:6], 2) - 15
    mantissa = 1 + sum(int(bit) * (2 ** -(i + 1)) for i, bit in enumerate(bin_str[6:]))
    return sinal * mantissa * (2 ** expoente)

def menu():
        print("\n--- Tabela correspondencia ---\n")
        print("Escolha o tipo de dado: ")
        print("1. Binario")
        print("2. Natural")
        print("3. Inteiro em sinal magnitude")
        print("4. Inteiro em complemento de 2")
        print("5. Real em ponto fixo")
        print("6. Real em ponto flutuante")
        print("0. Sair")
        op = int(input("Digite a opcao: "))

        return op

def main():
    op = menu()
    while op != 0:

        valor = input("Digite o valor: ")

        if op == 1:  
            print(f"Decimal: {binario_para_decimal(valor)}")
            print(f"Sinal Magnitude: {sm(valor)}")
            print(f"Complemento de 2: {c2(valor)}")
            print(f"Ponto Fixo: {fixo(valor)}")
            print(f"Ponto Flutuante: {float(valor)}")
            op = menu()
        elif op == 2: 
            bin_val = decimal_para_binario(int(valor))
            print(f"Binário: {bin_val}")
            print(f"Sinal Magnitude: {sm(bin_val)}")
            print(f"Complemento de 2: {c2(bin_val)}")
            print(f"Ponto Fixo: {fixo(bin_val)}")
            print(f"Ponto Flutuante: {float(bin_val)}")
            op = menu()
        elif op == 3:  
            print(f"Decimal: {sm(valor)}")
            print(f"Binário: {decimal_para_binario(sm(valor))}")
            print(f"Complemento de 2: {c2(valor)}")
            print(f"Ponto Fixo: {fixo(valor)}")
            print(f"Ponto Flutuante: {float(valor)}")
            op = menu()
        elif op == 4:  
            print(f"Decimal: {c2(valor)}")
            print(f"Binário: {decimal_para_binario(c2(valor))}")
            print(f"Sinal Magnitude: {sm(valor)}")
            print(f"Ponto Fixo: {fixo(valor)}")
            print(f"Ponto Flutuante: {float(valor)}")
            op = menu()
        elif op == 5: 
            print(f"Valor decimal: {fixo(valor)}")
            print(f"Binário: {decimal_para_binario(int(fixo(valor)))}")
            print(f"Sinal Magnitude: {sm(valor)}")
            print(f"Complemento de 2: {c2(valor)}")
            print(f"Ponto Flutuante: {float(valor)}")
            op = menu()
        elif op == 6: 
            print(f"Valor decimal: {float(valor)}")
            print(f"Binário: {decimal_para_binario(int(float(valor)))}")
            print(f"Sinal Magnitude: {sm(valor)}")
            print(f"Complemento de 2: {c2(valor)}")
            print(f"Ponto Fixo: {fixo(valor)}")
            op = menu()
        else:
            print("Opção inválida!")

main()
