import csv
import datetime
from Pizza import *


# The menu is printed first
def main():
    f = open('Menu.txt', 'r')
    print(f.read())
    f.close()
    # Then the user will choose from the menu

    while True:
        pizza_choice = int(input("Please choose a pizza base:"))

        if pizza_choice == 1:
            pizza = ClassicPizza()
            break

        elif pizza_choice == 2:
            pizza = MargheritaPizza()
            break

        elif pizza_choice == 3:
            pizza = TurkPizza()
            break

        elif pizza_choice == 4:
            pizza = PlainPizza()
            break

        else:
            print("You made the wrong choice!!")

    while True:
        sauce_choose = int(input("Please choose a sauce:"))
        if sauce_choose == 11:
            sauce = Olives(pizza)
            break

        elif sauce_choose == 12:
            sauce = Mushrooms(pizza)
            break

        elif sauce_choose == 13:
            sauce = GoatCheese(pizza)
            break

        elif sauce_choose == 14:
            sauce = Meat(pizza)
            break

        elif sauce_choose == 15:
            sauce = Onions(pizza)
            break

        elif sauce_choose == 16:
            sauce = Corn(pizza)
            break

        else:
            print("You made the wrong choice!!")

    desired_pizza = sauce.get_description()
    price_of_pizza = sauce.get_cost()

    print("Desired pizza:", desired_pizza)
    print("Price of pizza:", price_of_pizza)

    full_name = input("Please enter your first and last name: ")
    id_number = input("Please enter your ID number:")
    card_number = input("Please enter your credit card number:")
    card_password = input("Please enter your credit card password:")
    print("Your order has been received successfully.")

    with open('Orders_Database.csv', 'a') as db:
        writer = csv.writer(db)
        writer.writerow([sauce.get_description(), f"{sauce.get_cost()}TL", full_name, id_number, card_number,
                         card_password, datetime.datetime.now()])


main()