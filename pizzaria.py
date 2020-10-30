from pizza import Pizza

class Pizzaria:
    def __init__(self, name):
        self.name = name
        print("Creating a Pizzaria with name", self.name)

    def get_menu(self):
        # fixture
        menu =  [
            {   "name": "Pereroni",
                "price": 8.50,
                "type": "Pizza"
            },
            {
                "name": "Calzone",
                "price": 11.75,
                "type": "Pizza"
            }
        ]
        return menu

    def order_pizzas(self, numbers_of_pizzas, time, money):
        print("First checking the amount of money")
        if money <= 0.0:
            raise Exception("Not enough money!")

        margarita = Pizza("Margarita", 42)
        calzone = Pizza("Calzone", 23)

        print("The real name of the margarita object is", margarita.name)
        print("The real name of the calzone object is", calzone.name)

        pizzas = [margarita, calzone]
        return pizzas