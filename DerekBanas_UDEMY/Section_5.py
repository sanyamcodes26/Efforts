def initial():
    drink = input("Coke or Pepsi ? ")
    if drink == "coke":
        print("Here's your coke.")
    elif drink == "pepsi":
        print("Here's your pepsi.")
    else:
        print("**ck off")
    return


def calculator():
    equation = input("Enter Calculation : ")
    num_1, operator, num_2 = equation.split()
    num_1 = int(num_1)
    num_2 = int(num_2)
    if operator == "+":
        print(num_1 + num_2)
    elif operator == "-":
        print(num_1 - num_2)
    elif operator == "*":
        print(num_1 * num_2)
    else:
        if num_2 == 0:
            print("Not Divisible by ZERO")
        else:
            print(num_1 - num_2)
    return

def logical_operator():
    age = int(input("Age : "))
    if age >= 1 and age <= 18 or age == 21 or age == 50:
        print("Important")
    else:
        print("Not important")
    grade(age)
    vote(age)
    return


def grade(age):
    if age < 5:
        print("No Studies")
    elif age == 5:
        print("Kindergarten")
    elif age >= 6 and age <= 17:
        print("Grade :", age - 5)
    else:
        print("College")
    return


def vote(age):
    can_vote = True if age >= 18 else False
    print("Can vote :", can_vote)


if __name__ == "__main__":
    # initial()
    # calculator()
    logical_operator()
