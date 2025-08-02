def soma(a, b):
    """
    Realiza a soma de dois números.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da soma
    """
    return a + b

if __name__ == "__main__":
    print("Teste da função soma:")
    print(f"2 + 3 = {soma(2, 3)}") 
    print(f"7.2 + 3.8 = {soma(7.2, 3.8)}") 


def dividir(a, b):
    try:
        resultado = a / b
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")


print("Calculadora de Divisão")
num1 = float(input("Digite o dividendo: "))
num2 = float(input("Digite o divisor: "))
dividir(num1, num2)