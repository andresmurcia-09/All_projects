import random

denominations = {10000: 100, 20000: 50, 50000: 20, 100000: 10}


def generate_balance():
    return random.randint(100000, 300000)


def withdraw(amount, balance):
    if amount < 10000:
        print("El retiro mínimo es de $10.000")
        return balance
    if amount > balance:
        print("Fondos insuficientes")
        return balance
    remaining_amount = amount
    bills = []
    for denomination, quantity in denominations.items():
        while remaining_amount >= denomination and quantity > 0:
            bills.append(denomination)
            remaining_amount -= denomination
            quantity -= 1
    if remaining_amount != 0:
        print("Lo siento, no puedo entregar esa cantidad")
        return balance
    balance -= amount
    print("Retiraste $%d" % amount)
    print("Tu saldo actual es $%d" % balance)
    return balance


def main():
    balance = generate_balance()
    print("Tu saldo actual es $%d" % balance)
    while True:
        try:
            amount = int(input("Ingrese la cantidad que desea retirar: "))
            balance = withdraw(amount, balance)
        except ValueError:
            print("Cantidad inválida")
        finally:
            option = input("¿Desea realizar otro retiro? (s/n):")
            if option.lower() != "s":
                break


if __name__ == "__main__":
    main()
