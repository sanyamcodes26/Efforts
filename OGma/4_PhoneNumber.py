if __name__ == "__main__":
    numbers = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
               "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    phone = input(">> Phone Number : ")
    for i in phone:
        if i in numbers.keys():
            print(numbers[i], " ", end="")
