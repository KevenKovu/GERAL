def soma_divisores(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma
