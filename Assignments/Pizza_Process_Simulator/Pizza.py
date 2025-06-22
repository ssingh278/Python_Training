class Pizza:
    """
    This class represents a Pizza object with a specific type, size, and list of toppings.
    It provides methods to calculate the total price and display the pizza details.
    """
    __PizzaType = None
    __Size = None
    __Toppings = None

    # Dictionary to store pizza types
    PizzaTypeList = [
        {"code": "V", "name": "Veggie", "price": 11.49},
        {"code": "NV", "name": "Non Veggie", "price": 12.99}
    ]

    # Dictionary to store pizza sizes
    SizeList = [
        {"code": "S", "name": "Small", "price": 5.99},
        {"code": "M", "name": "Medium", "price": 7.99},
        {"code": "L", "name": "Large", "price": 9.99}
    ]

    # Dictionary to store pizza toppings
    ToppingsList = [
        {"code": "CH", "name": "Cheese", "price": 1.50},
        {"code": "PEP", "name": "Pepperoni", "price": 2.00},
        {"code": "MUS", "name": "Mushrooms", "price": 1.25},
        {"code": "ON", "name": "Onions", "price": 1.00},
        {"code": "OL", "name": "Olives", "price": 1.75},
        {"code": "BG", "name": "Bell Peppers", "price": 1.50}
    ]

    def __init__(self, pizzaType, size, toppings):
        """
        CTOR for class Pizza
        :param pizzaType: Pizza type code
        :param size: Pizza size code
        :param toppings: Pizza topping code
        """
        if not isinstance(pizzaType, str):
            raise TypeError("Pizza type must be a string.")

        valid_types = [item["code"] for item in Pizza.PizzaTypeList]
        if pizzaType not in valid_types:
            raise Exception(f"Pizza type can only be one of: {', '.join(valid_types)}.")

        if not isinstance(size, str):
            raise TypeError("Size must be a string.")

        valid_sizes = [item["code"] for item in Pizza.SizeList]
        if size not in valid_sizes:
            raise Exception(f"Size can only be one of: {', '.join(valid_sizes)}.")

        if not isinstance(toppings, list):
            raise TypeError("Toppings must be a list.")

        valid_toppings = [item["code"] for item in Pizza.ToppingsList]
        for topping in toppings:
            if not isinstance(topping, str):
                raise TypeError(f"Topping '{topping}' must be a string.")
            if topping not in valid_toppings:
                raise Exception(f"Topping '{topping}' is invalid. Valid toppings are: {', '.join(valid_toppings)}.")

        self.__PizzaType = next(item for item in Pizza.PizzaTypeList if item["code"] == pizzaType)
        self.__Size = next(item for item in Pizza.SizeList if item["code"] == size)
        self.__Toppings = [item for item in Pizza.ToppingsList if item["code"] in toppings]

    @staticmethod
    def DisplayPizzaType():
        """
        This method will display the available pizza types to the user
        :return:
        """
        print("\nPizza Type :")
        for option in Pizza.PizzaTypeList:
            print(f"{option['code']:<3} - {option['name']:<15} - ${option['price']:>5.2f}")

    @staticmethod
    def DisplaySize():
        """
        This method will display the available pizza sizes to the user
        :return:
        """
        print("\nPizza Size :")
        for option in Pizza.SizeList:
            print(f"{option['code']:<3} - {option['name']:<15} - ${option['price']:>5.2f}")

    @staticmethod
    def DisplayToppings():
        """
        This method will display the available pizza toppings to the user
        :return:
        """
        print("\nPizza Toppings :")
        for option in Pizza.ToppingsList:
            print(f"{option['code']:<3} - {option['name']:<15} - ${option['price']:>5.2f}")

    def GetTotalPrice(self):
        """
        This method would return the total price for the pizza
        :return: float - total price
        """
        pizzaTypePrice = self.__PizzaType["price"]
        sizePrice = self.__Size["price"]
        topping_prices = sum([topping['price'] for topping in self.__Toppings])
        return pizzaTypePrice + sizePrice + topping_prices

########################################################################################
