# Sundae Bar Ordering System 🍨

### Video Demo: <https://youtu.be/nREpi7pEnAI>

### Program Description:
This basic Python program aims to emulate a customer ordering system for a "make-your-own" ice cream sundae bar. The program first requires that the user select an ice cream flavour from the list provided and enter the number of scoops that they would like. The program then prompts the user to optionally add a sauce and various toppings to their creation. Finally, the program prints the order details, including the total price, to the user's screen.

I chose to structure my program around a custom "Sundae" class. I find object-orientated programming to be quite challenging and wanted to practice creating a class with attributes/properties and methods to help improve my understanding of this topic. I did not nest all data validation within my class as the project brief required that I include at least three functions outside of any classes.

When designing my program I chose to keep all data structures (including *available_flavours*, *available_sauces* and *available_toppings*) in the main source code file. If more data needed to be stored (i.e. the store provides a greater selection of ice cream flavours, sauces and/or toppings) I would move these data structures into a separate file to maintain code readability.

I found writing comprehensive unit tests for several of my program's functions to be difficult. This is because the functions I needed to test (e.g. *check_scoops()*) contained loops inside of them and any invalid user input resulted in the input() function being recalled. Unfortunately, I was unable to find a clear solution to my problem using Pytest.

To improve my program for the future I would consider creating a graphical user interface (GUI) to improve my program's user experience.

### Included files:
- *project.py* contains the program's source code.
- *test_project.py* contains unit tests for several of the program's functions/methods
- *requirements.txt* lists all third-party modules required to run the program.
