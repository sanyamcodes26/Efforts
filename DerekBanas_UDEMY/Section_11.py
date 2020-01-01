def add_numbers(num_1, num_2):
    return num_1 + num_2


def change_name():
    global gbl_name
    gbl_name = "Name"


def solve_eql(eqn):
    x, add, num_1, eql, num_2 = eqn.split()
    num_1, num_2 = int(num_1), int(num_2)
    return num_2 - num_1


def initial():
    global gbl_name
    print("add_numbers(43, 26) :", add_numbers(43, 26))
    change_name()
    print(gbl_name)
    print("x + 43 = 32; x =", solve_eql("x + 43 = 32"))
    return


gbl_name = "Default"


if __name__ == "__main__":
    initial()
