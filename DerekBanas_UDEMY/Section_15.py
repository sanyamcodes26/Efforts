def initial():
    id_dict = {"f_name": "Akash", "l_name": "Sengupta"}
    print(id_dict)
    print(id_dict["f_name"])
    print("phone" in id_dict)
    id_dict['phone'] = "9231905873"
    print("phone" in id_dict)
    print(id_dict)
    employees = []
    f_name, l_name = input("Fname Lname").split()
    employees.append({"f_name": f_name, "l_name": l_name})
    print(employees)


def test():
    customers = []
    i = 1
    while True:
        ch = input("Enter Customers (y/n) : ")
        if ch == "y" or ch == "Y":
            f_name, l_name = input("Fname Lname : ").split()
            customers.append({"id":i, "f_name":f_name, "l_name":l_name})
            i += 1
        else:
            for i in customers:
                print(i)
            break


if __name__ == "__main__":
    # initial()
    test()
