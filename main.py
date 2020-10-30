from pizzaria import Pizzaria

# Wouldn't it be nice if...
# we could order pizza's from a pizzaria

def order_some_pizzas(number_of_pizzas, time, money):
    # lets do a lot of work here
    print("Let's order some pizzas.")
    pizzaria = Pizzaria("Mario")
    pizzas = pizzaria.order_pizzas(number_of_pizzas, time, money)
    return pizzas

def eat_pizzas(pizzas):
    print("OK let's eat the pizzas!")
    for pizza in pizzas:
        print(pizza.name, "[", pizza.number, "]")

def main():
    print("Pizza program")
    # order some pizzas...
    # where to get them? Pizzaria
    # is there a menu? Where can we get it
    money = 100.0
    time = "18:30"
    number_of_pizzas = 23
    try:
        pizzas = order_some_pizzas(number_of_pizzas, time, money)
        eat_pizzas(pizzas)
    except Exception as e:
        ("No food... :(")
        print(e)

if __name__ == "__main__":
    main()

