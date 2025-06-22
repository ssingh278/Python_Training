import Pizza as P

Menu = ["Order Pizza", "Total Sale", "Exit"]  # creating list to display menu
TotalSale = []  # local db to store sales


def DisplayMenu():
    """
    This method will display menu to the user
    :return:
    """
    for i in range(0, len(Menu)):
        print(i + 1, ".", Menu[i])


def GetInput_Menu():
    """
    This method will get input from the user and validate and return it
    :return: int - user response
    """
    user_input = input("Enter your choice: ")
    try:
        number = int(user_input)
        return number
    except ValueError:
        return 0


def DisplayTotalSale():
    """
    This method will display the entire sales to the user
    :return:
    """
    print("\n")
    if len(TotalSale) <= 0:
        print("No Pizza Sold yet.")
    else:
        print("\033[4mSales:\033[0m")
        for i in range(0, len(TotalSale)):
            print(i + 1, ". $", TotalSale[i])

        print("Total - $", sum(TotalSale))


def HandlePizzaOrder():
    """
    This method will process pizza
    :return:
    """
    P.Pizza.DisplayPizzaType()
    pizzaType = input("Enter pizza type code: ").strip().upper()

    P.Pizza.DisplaySize()
    pizzaSize = input("Enter pizza size code: ").strip().upper()

    P.Pizza.DisplayToppings()
    pizzaToppings = input("Enter toppings codes separated by commas: ")
    pizzaToppingsList = [t.strip().upper() for t in pizzaToppings.split(",") if t.strip()]

    try:
        finalPizza = P.Pizza(pizzaType, pizzaSize, pizzaToppingsList)
        finalPrice = finalPizza.GetTotalPrice()
        print(f"\nYour subtotal: $ {finalPrice:.2f}")
        TotalSale.append(finalPrice)
    except Exception as e:
        print(f"Error: {e}")


def HandleDisplayTotalSale():
    """
    This method would process total sale
    :return:
    """
    if TotalSale:
        total = sum(TotalSale)
        print(f"\nTotal sales so far: ${total:.2f}")
    else:
        print("\nNo sales yet.")


def main():
    """
    Main Program to be executed
    :return:
    """
    while True:
        DisplayMenu()
        userChoice = GetInput_Menu()

        if userChoice == 1:
            HandlePizzaOrder()
        elif userChoice == 2:
            HandleDisplayTotalSale()
        elif userChoice == 3:
            print("Thanks, visit again!")
            break
        else:
            print("Invalid choice. Please select an option from the menu.")

        print("\n")


if __name__ == "__main__":
    main()
