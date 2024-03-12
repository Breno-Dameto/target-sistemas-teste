def is_fibonacci_number(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


numero_informado = int(input("Informe um número: "))

if is_fibonacci_number(numero_informado):
    print(f"{numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_informado} não pertence à sequência de Fibonacci.")