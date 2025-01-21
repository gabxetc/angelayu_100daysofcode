yes = "Y"
no = "N"
small = "S"
medium = "M"
large = "L"
bill = 0


print("Welcome to Python Pizza Deliveries!")
while bill >= 0:
    size = input("What size pizza do you want? S, M or L: ").upper()
    if size != (small or medium or large):
        print("Enter a correct value")
        break
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    if pepperoni != (yes or no):
        print("Enter a correct value")
        break
    extra_chee = input("Do you want extra chee? Lactose intolerate ass. Y or N: ").upper()
    if extra_chee != (yes or no):
        print("Enter a correct value")
        break

# Small pizza: $15
# Extra pepp small: + $2

# Medium pizza: $20
# Large pizza: $25
# Extra pepp medium/large: + $3

# Extra chee witcho lactose ass: + $1

# todo: work out how much they need to pay based on their size choice

# todo: work out addition to bill based on pepp choice

# todo: work out final amount based on if they want extra chee

    if size == small:
        bill += 15
        if pepperoni == yes:
            bill += 2
        elif extra_chee == yes:
            bill += 1
        else:
            bill += 0
        print("Your final bill is: $" + str(bill) + ".")
        break

    elif size == medium:
        bill += 20
        if pepperoni == yes:
            bill += 3
        elif extra_chee == yes:
            bill += 1
        else:
            bill += 0
        print("Your final bill is: $" + str(bill) + ".")
        break

    elif size == large:
        bill += 25
        if pepperoni == yes:
            bill += 3
        elif extra_chee == yes:
            bill += 1
        else:
            bill += 0
        print("Your final bill is: $" + str(bill) + ".")
        break

# Feedback:

# I could've had 3 different if statments 
# instead of nested if statments that checked for pepp and extra chee

# Final print statment should have been:
# print(f"Your final bill is: ${bill}.")

# Modifications:

# I want to be able to repeat asking the question if they enter an incorrect value
# i want to be able to remove or minus amounts from the total if the client chaanges their mind on an order
