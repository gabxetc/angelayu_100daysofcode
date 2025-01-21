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

def take_order(size, pepp, extra_chee):

    ordering_size = True
    ordering_pepp = True
    ordering_chee = True

    bill = 0

    while ordering_size:
        size = input("What size pizza do you want? S, M or L: ").upper()
        if (size == small or size == medium or size == large):
            if size == small:
                bill += 15    
            elif size == medium:
                bill += 20
            elif size == large:
                bill += 25
            ordering_size = False
        else:
            print("Enter a correct value")

    while ordering_pepp:
        pepp = input("Do you want pepperoni on your pizza? Y or N: ").upper()
        if (pepp == yes or pepp == no):
            if pepp == yes and size == small:
                bill += 2
            elif pepp == yes and (size == medium or size == large):
                bill += 3
            ordering_pepp = False
        else:
            print("Enter a correct value")

    while ordering_chee:
        extra_chee = input("Do you want extra chee? Lactose intolerate ass. Y or N: ").upper()
        if (extra_chee == yes or extra_chee == no):
            if extra_chee == yes:
                bill += 1
            ordering_chee = False
        else:
            print("Enter a correct value")

    return print("Your final bill is: $" + str(bill) + ".")

if __name__ == "__main__":
    take_order(size, pepp, extra_chee)

# Feedback:

# I could've had 3 different if statments 
# instead of nested if statments that checked for pepp and extra chee

# Final print statment should have been:
# print(f"Your final bill is: ${bill}.")

# Modifications:

# I want to be able to repeat asking the question if they enter an incorrect value
# i want to be able to remove or minus amounts from the total if the client chaanges their mind on an order
