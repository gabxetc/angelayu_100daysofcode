# Project Brief

# Small pizza: $15
# Extra pepp small: + $2

# Medium pizza: $20
# Large pizza: $25
# Extra pepp medium/large: + $3

# Extra chee witcho lactose ass: + $1

# todo: work out how much they need to pay based on their size choice

# todo: work out addition to bill based on pepp choice

# todo: work out final amount based on if they want extra chee

print("Welcome to Python Pizza Deliveries!")

yes = "Y"
no = "N"
small = "S"
medium = "M"
large = "L"
size = ""
pepp = ""
extra_chee = ""
bill = 0

def main():
    pizza_size(size, bill)
    pepp_topping(pepp, bill)
    chee_extra_topping(extra_chee, bill)

def pizza_size(size, bill):
    ordering_size = True

    while ordering_size:
        size = input("What size pizza do you want? S, M or L: ").upper()
        if (size == small or size == medium or size == large):
            if size == small:
                bill += 15    
                print(f"Your current total is: ${bill}")
            elif size == medium:
                bill += 20
                print(f"Your current total is: ${bill}")
            elif size == large:
                bill += 25
                print(f"Your current total is: ${bill}")
            change_size = input("Would you like to change the pizza size? Y or N: ").upper()
            if (change_size == no):
                ordering_size = False
            else:
                bill = 0
                continue
        else:
            print("Enter a correct value")
            
    return bill

def pepp_topping(pepp, bill):
    ordering_pepp = True

    while ordering_pepp:
        pepp = input("Do you want pepperoni on your pizza? Y or N: ").upper()
        if (pepp == yes or pepp == no):
            if pepp == yes and size == small:
                bill += 2
                print(f"Your current total is: ${bill}")
                remove_pepp = input(f"You have pepperoni on your {size} pizza. Would you like to remove it? Y or N: ").upper()
                if (remove_pepp == yes):
                    bill -= 2
                    print("You have removed pepperoni from your pizza.")
                    ordering_pepp = False
                else: 
                    ordering_pepp = False
                    
            elif pepp == yes and (size == medium or size == large):
                bill += 3
                print(f"Your current total is: ${bill}")
                remove_pepp = input(f"You have pepperoni on your {size} pizza. Would you like to remove it? Y or N: ").upper()
                if (remove_pepp == yes):
                    bill -= 3
                    pepp = no
                    print(f"You have removed pepperoni from your {size} pizza. Shame, you're probably vegeterian.")
                    ordering_pepp = False
                else:
                    ordering_pepp = False
            else:
                ordering_pepp = False
        else:
            print("Enter a correct value")

def chee_extra_topping(extra_chee, bill):
    ordering_chee = True

    while ordering_chee:
        extra_chee = input("Do you want extra chee? Y or N: ").upper()
        if (extra_chee == yes or extra_chee == no):
            if extra_chee == yes:
                bill += 1
                chee_check = input(f"You have extra chee on your {size} pizza. Would you like to remove it? Y or N: ").upper()
                if (chee_check == yes):
                    bill -= 1
                    extra_chee = no
                    print(f"Okay, you've removed chee from you {size} pizza. Shame, you're probably lactose intolerant.")
                    ordering_chee = False
                else:
                    ordering_chee = False
            ordering_chee = False
        else:
            print("Enter a correct value")

def complete_order(bill, extra_chee, size, pepp):
    final_order = input(f"This is your order:\nPizza Size: {size}\nPepperoni: {pepp}\nExtra chee: {extra_chee}\nAre you happy? Y or N: ").upper()
    if (final_order == yes):
        print("Your final bill is: $" + str(bill) + ".")
    else:
        main()

if __name__ == "__main__":
    main()

# Feedback:

# I could've had 3 different if statments 
# instead of nested if statments that checked for pepp and extra chee

# Final print statment should have been:
# print(f"Your final bill is: ${bill}.")

# Modifications:

# I want to be able to repeat asking the question if they enter an incorrect value --------------------------------------- Complete
# i want to be able to remove or minus amounts from the total if the client chaanges their mind on an order -------------- Complete
# Change top orders from anywhere in the code
# Have seperate functions for each body of code and task
