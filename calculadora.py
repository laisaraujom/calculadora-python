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

def subtracao(a, b):
    return a - b
# Exemplo de uso
resultado = subtracao(10, 5)
print(f"10 - 5 = {resultado}")