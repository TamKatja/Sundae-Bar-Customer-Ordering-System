import inflect
import re
import sys
from tabulate import tabulate
from word2number import w2n

p = inflect.engine()

available_flavours = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
]

available_sauces = {
    "Chocolate": "$0.50",
    "Strawberry": "$0.50",
    "Caramel": "$0.50",
}

available_toppings = {
    "Sprinkles": "$0.50",
    "Chocolate": "$0.50",
    "Fruit": "$1.00",
    "Nuts": "$1.00",
}


class Sundae:

    price_per_scoop = 4.0

    def __init__(self, flavour, scoops=0, sauce=None, toppings=None, price=0.0):
        self.flavour = flavour
        self.scoops = scoops
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    @property
    def flavour(self):
        return self._flavour

    @flavour.setter
    def flavour(self, flavour):
        while flavour not in available_flavours:
            # Re-prompt user if flavour invalid
            flavour = input(">>> Flavour unavailable, try again: ").strip().title()
        self._flavour = flavour

    def add_sauce(self, sauce):
        while sauce not in available_sauces:
            # Re-prompt user if sauce invalid
            sauce = input(">>> Sauce unavailable, try again: ").strip().title()
        self.sauce = sauce
        return self.sauce

    def add_toppings(self, toppings):
        print("\n...adding toppings!\n")
        self.toppings = toppings

    def __str__(self):
        if self.toppings != None:
            # Ignore duplicate toppings
            self.toppings = set(self.toppings)
            # Join chosen toppings into a sentence
            self.toppings = p.join(list(self.toppings))

        # Format output if no sauce and no toppings chosen
        if self.sauce == None and self.toppings == None:
            return f"""Please enjoy your {self.flavour} Sundae! 🍨
            \n...That will be ${self.price:.2f}\n""".title()

        # Format output if no toppings chosen
        elif self.sauce != None and self.toppings == None:
            return f"""Please enjoy your {self.flavour} Sundae with {self.sauce} Sauce! 🍨
            \n...That will be ${self.price:.2f}\n""".title()

        # Format output if no sauce chosen
        elif self.sauce == None and self.toppings != None:
            return f"""Please enjoy your {self.flavour} Sundae, topped with {self.toppings}! 🍨
            \n...That will be ${self.price:.2f}\n""".title()

        # Format output if both sauce and toppings chosen
        else:
            return f"""Please enjoy your {self.flavour} Sundae with {self.sauce} Sauce, topped with {self.toppings}! 🍨
            \n...That will be ${self.price:.2f}\n""".title()


def main():

    print("\n * * * WELCOME TO THE SUNDAE BAR * * *")
    print("\nTime to make your sundae...\n")

    # Prompt user to input flavour
    print(display_flavours(available_flavours))
    sundae = Sundae(input(">>> Select an ice cream flavour: ").strip().title())

    # Prompt user to input number of scoops
    min_scoops = 1
    max_scoops = 5
    print(display_scoop_prices())
    scoops = input(f">>> How many scoops of {sundae.flavour}? [1-5]: ").strip()

    # Check valid number of scoops
    sundae.scoops = check_scoops(scoops, min_scoops, max_scoops)

    # Update order price
    sundae.price = sundae.scoops * Sundae.price_per_scoop

    # Check if user would like to add sauce
    if answer := get_answer(
        input("\n>>> Would you like to add a sauce? [y/n]: ").strip()):
        print(display_sauces(available_sauces))
        sauce = sundae.add_sauce(input(f">>> Select a sundae sauce: ").strip().title())

        # Update order price
        sundae.price += float(available_sauces[sauce][1:])

    # Check if user would like to add toppings
    max_toppings = 5
    if answer := get_answer(
        input("\n>>> Would you like to add toppings? [y/n]: ").strip()):
        print(display_toppings(available_toppings))
        print(f"Note: maximum toppings = {max_toppings}\n")

        # Generate list of toppings
        toppings_list = []
        while True:
            if topping := check_topping(
                input(">>> Select a topping: ").strip().title(), available_toppings):
                # Identify duplicate toppings
                if topping in toppings_list:
                    print(f" *** ok, extra {topping} ***")
                # Add valid topping to list
                toppings_list.append(topping)
            # Check for maximum toppings
            if len(toppings_list) >= max_toppings:
                break
            # Prompt user for additional toppings
            if get_answer(input(">>> Would you like another topping? [y/n]: ").strip()):
                continue
            else:
                break

        # Add toppings
        sundae.add_toppings(toppings_list)

        # Update order price
        for topping in toppings_list:
            sundae.price += float(available_toppings[topping][1:])

    # Output sundae and total price
    print(f"\n{sundae}")


def display_flavours(available_flavours):
    """Function to display available flavours as table"""
    return tabulate([available_flavours], tablefmt="rounded_grid")


def display_scoop_prices():
    """Function to display scoop price as table"""
    price = f"Price per scoop: ${Sundae.price_per_scoop:.2f}"
    return tabulate([[price]], tablefmt="rounded_grid")


def check_scoops(n, min_n, max_n):
    """Function to validate number of scoops"""
    # Identify integer input
    while True:
        try:
            if n.isdigit():
                n = int(n)
            elif n.lower() in ["one", "two", "three", "four", "five"]:
                n = int(w2n.word_to_num(n))
            # Check number of scoops within range
            if int(n) < min_n:
                n = input(f"Oops, minimum {min_n} scoop! Try again: ")
                continue
            elif int(n) > max_n:
                n = input(f"Oops, maximum {max_n} scoops! Try again: ")
                continue
            else:
                return int(n)
        except ValueError:
            n = input("I don't understand? Try again: ")
            continue


def get_answer(ans):
    """Function to validate a [y/n] answer"""
    ans = ans.strip().lower()
    while True:
        if ans == "y" or ans == "yes":
            return True
        elif ans == "n" or ans == "no":
            return False
        else:
            ans = input("I don't understand? Try again [y/n]: ")
            continue


def display_sauces(available_sauces: dict):
    """Function to display available sauces as table"""
    return tabulate([available_sauces], headers="keys", tablefmt="rounded_grid")


def display_toppings(available_toppings: dict):
    """Function to display available toppings as table"""
    return tabulate([available_toppings], headers="keys", tablefmt="rounded_grid")


def check_topping(top, toppings):
    """Function to validate topping input"""
    # Identify string input
    if top in toppings:
        return top
    else:
        print("I don't understand?")
        return False


if __name__ == "__main__":
    main()
