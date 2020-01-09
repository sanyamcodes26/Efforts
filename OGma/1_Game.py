import random


def game():
    while True:

        token = input(">> TOKEN (y/n): ")
        attempt = 3
        sum_1 = 0
        game_list = []
        token = token.upper()

        magic = random.randrange(1, 1000)
        un_luck = random.randrange(1, 1000)
        hf_luck = random.randrange(1, 1000)

        if token == 'N':
            print(">> Enter token to play..")
            break
        else:
            while attempt > 0:
                while True:
                    try:
                        option = int(input(">> TYPE A number (1, 1000) : "))
                    except ValueError as e:
                        print(">> Exception :", e.__str__())
                        print(">> Invalid Input..Input number in range (1, 1000)")
                    else:
                        print(">> Thank You !!!\n", "-" * 10)
                        break

                if magic == option:
                    sum_1 += 100000
                    game_list.append('M')
                    break
                elif un_luck == option:
                    sum_1 -= 2000
                    game_list.append('U')
                    break
                elif hf_luck == option:
                    sum_1 += 10000
                    game_list.append("H")
                    break
                else:
                    game_list.append("-")

                attempt -= 1
            print(">> Sum :", sum_1)
            print(">>", game_list)
            print(">>END")
    return


if __name__ == "__main__":
    game()
