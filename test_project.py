import pytest
from project import check_scoops, get_answer, check_topping
from project import Sundae
from project import available_toppings


def main():
    test_check_scoops()
    test_get_answer()
    test_check_topping()


def test_check_scoops():
    # Test: input str consists of number only
    assert check_scoops("1", 1, 5) == 1
    assert check_scoops("5", 1, 5) == 5
    # Test: input str consists of number as word only
    assert check_scoops("one", 1, 5) == 1
    assert check_scoops("five", 1, 5) == 5
    # All other responses re-prompt user for input


def test_get_answer():
    # Test: accepts "y" or "n" as response
    assert get_answer("y") == True
    assert get_answer("n") == False
    # Test: accepts "yes" or "no" as response
    assert get_answer("yes") == True
    assert get_answer("no") == False
    # Test: accepts response case-insensitively
    assert get_answer("Y") == True
    assert get_answer("N") == False


def test_check_topping():
    # Test: accepts valid topping
    assert check_topping("Sprinkles", available_toppings) == "Sprinkles"
    # Test: rejects invalid topping
    assert check_topping("lollies", available_toppings) == False


def test_add_toppings():
    # Test: outputs list of toppings
    sundae = Sundae("Vanilla", 0, None, ["Sprinkles", "Chocolate", "Fruit"], 0.0)
    assert sundae.toppings == ["Sprinkles", "Chocolate", "Fruit"]


def test_flavour():
    # Test: valid flavour
    sundae = Sundae("Vanilla", 0, None, None, 0.0)
    assert sundae.flavour == "Vanilla"
    # Invalid flavour re-prompts user for input


def test_add_sauce():
    # Test: valid sauce
    sundae = Sundae("Vanilla", 0, "Chocolate", None, 0.0)
    assert sundae.sauce == "Chocolate"
    # Invalid sauce re-prompts user for input


def test_output():
    # Test: output if no toppings or sauces selected
    sundae = Sundae("Vanilla", 1, None, None, 4.0)
    assert (
        str(sundae)
        == "Please Enjoy Your Vanilla Sundae! 🍨\n            \n...That Will Be $4.00\n"
    )
    # Test: output if sauce selected
    sundae = Sundae("Vanilla", 1, "Chocolate", None, 4.5)
    assert (
        str(sundae)
        == "Please Enjoy Your Vanilla Sundae With Chocolate Sauce! 🍨\n            \n...That Will Be $4.50\n"
    )
    # Test: output if topping/s selected
    sundae = Sundae("Vanilla", 1, None, ["Sprinkles"], 4.5)
    assert (
        str(sundae)
        == "Please Enjoy Your Vanilla Sundae, Topped With Sprinkles! 🍨\n            \n...That Will Be $4.50\n"
    )
    # Test: output if sauce and toppings selected
    sundae = Sundae("Vanilla", 1, "Chocolate", ["Sprinkles"], 5.0)
    assert (
        str(sundae)
        == "Please Enjoy Your Vanilla Sundae With Chocolate Sauce, Topped With Sprinkles! 🍨\n            \n...That Will Be $5.00\n"
    )


if __name__ == "__main__":
    main()
