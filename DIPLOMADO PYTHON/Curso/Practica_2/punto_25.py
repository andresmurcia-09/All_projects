# Imprimir los números del 1 al 100, pero para los múltiplos de 3 imprimir "Fizz",
# para los múltiplos de 5 imprimir "Buzz" y para los múltiplos de ambos imprimir 
# "FizzBuzz" utilizando un bucle `for`.


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
            print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
            print(num)