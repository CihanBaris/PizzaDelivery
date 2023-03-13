import csv
import datetime
from PizzaContent.PizzaSauce import*

def print_menu():
     with open("Menu.txt","r",encoding="UTF-8") as menu:
        p_lines = menu.readlines()[:7]  
        for line in p_lines:
             print(line)

def main():
    print("Welcome to Tiny Ceasar Pizza")
    tap = input("Press any key to continue...")
    print("What would you like to do?")
    print("1. Menu")

    operations = {
                  1 : print_menu,
                  2 : "View Order()",
                  3 : "Checkout()"
                  }
    
    while True:
        try:
            user_opr = operations[int(input("Press (1): "))]()
            break
        except ValueError:
            print("Your input is invalid! Please try again.")
            
        except KeyError:
            print("There is no such an input.Please enter between 1 and 3.")

    # The user makes a selection in the list
    
    pick_pizza = {
                    1 : MargheritaPizza,
                    2 : TexanBBQPizza,
                    3 : SupremePizza,
                    4 : HawaiianPizza,
                    5 : PepperoniPizza
                }
    
    # The user's choice sets the class of the relevant product
    pizza_choice = pick_pizza[int(input("Press (1-5): "))]()
    
    # Print sauce list to terminal
    with open("Menu.txt","r",encoding="UTF-8") as menu:
        s_lines = menu.readlines()[7:]
        for line in s_lines: 
            print(line)
 
    # The user makes a selection in the list
    pick_sauce = {
                    1 : Olive(pizza_choice),
                    2 : Corn(pizza_choice),
                    3 : Mushroom(pizza_choice),
                    4 : Chedar(pizza_choice),
                    5 : Sausage(pizza_choice)
                 }
    
    # The user's choice sets the class of the relevant product
    sauce_choice = pick_sauce[int(input("Select (1-5): "))]
    

    def order(pizza,sauce):
         ordered_pizza_name = pizza.get_name()        
         total_price = sauce.get_cost()
         return ordered_pizza_name,sauce.get_description(),total_price

    pizza_name,order_desc,total_price = order(pizza_choice,sauce_choice)
    # Get user information

    
    while True:
        name = input("Please enter your name: ")
        if not name.isalpha():
            print("Please enter only alphabetical characters for your name.")
        else:
            break
    while True:
        tc_id = input("Please enter your TC identification number: ")
        if not tc_id.isnumeric():
            print("Please enter only numerical characters for your TC identification.")
        else:
            break
    while True:
        credit_card_num = input("Please enter your credit card number: ")
        if not credit_card_num.isnumeric():
            print("Invalid Input")
        else:
            break
    while True:
        credit_card_cvv = input("Please enter your credit card CVV: ")
        if not credit_card_cvv.isnumeric():
            print("Invalid Input")
        else:
            break
    

    with open('Orders_Database.csv', mode='a', newline='') as order_file:
            writer = csv.writer(order_file)
            writer.writerow([name, tc_id, credit_card_num, credit_card_cvv,f"{pizza_name}Pizza : {order_desc}" ,total_price ])

    print("\nThank you for your order! Your pizza will be delivered shortly.\n")

if __name__ == "__main__":
    main()











    










        
       

