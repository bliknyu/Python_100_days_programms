def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


calculator={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

def super_calculator():
    calc=True

    a1 = float(input("Input any number for a1:"))
    while calc:
        new_oper=str(input("Input operation: a choice of +, -, * or /"))
        a2=float(input("Input any number for a2:"))
        for value in calculator:
            if value==new_oper:
                b1=calculator[value](a1, a2)
                print(f"{a1}{new_oper}{a2}={b1}")
        cont=input("Do you want to continue? Y or N?")
        if cont=="Y":
            a1=b1
        else:
            calc = False
            super_calculator()

super_calculator()

# new_operation=calculator["*"]
# print(new_operation(a1,a2))





# TODO-1: Ask the user for input
from os import system

'''
blind_auction = {}
end_of_auction=False
while not end_of_auction:
    name=input("Enter your name :\n")
    bid=int(input("Enter your price :\n"))
# TODO-2: Save data into dictionary {name: price}

    blind_auction[name]=bid
    end_game=input("Do you have another bidder? Y on N?")
    print("\n"*20)
    if end_game=="N":
        end_of_auction=True
max_price = 0
winner = ""

for person in blind_auction:
    if blind_auction[person] > max_price:
        max_price = blind_auction[person]
        winner = person
print("\nAll Bids:", blind_auction)
print(f"\nWinner: {winner} with a bid of ${max_price}")

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
'''

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades ={}
# for mark in student_scores:
#     print(student_scores[mark])
#     if student_scores[mark]>=91:
#         student_grades[mark] ="Outstanding"
#     elif 91>student_scores[mark]>=81:
#         student_grades[mark] ="Exceeds Expectations"
#     elif 81>student_scores[mark]>=71:
#         student_grades[mark] ="Acceptable"
#     else:
#         student_grades[mark] ="Fail"
# print(student_grades)