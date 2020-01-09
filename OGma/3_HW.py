class Car:
    def __init__(self, model_no="CAR"):
        self._condition = "PARKED"
        self.model_no = model_no

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value="PARKED"):
        self._condition = value

    def start_car(self, flag=0):
        if flag == 0:
            print(f"--> {self.model_no} ENGINE STARTED \t >>")
            self.condition = "ON"
        else:
            print(f"{self.model_no}'s IGNITION ALREADY ON")
            self.condition = "ON"

    def stop_car(self, flag=0):
        if flag == 0:
            print(f"--> {self.model_no} HALTED \t >>||")
            self.condition = "PARKED"
        else:
            print(f"{self.model_no}'s ENGINE ALREADY OFF")
            self.condition = "PARKED"

    def accelerate_car(self, flag=0):
        if flag == 0:
            print(f"--> {self.model_no} IN TOP SPEED \t >>>>")
            self.condition = "SPEED"
        else:
            print(f"{self.model_no} ENGINE BUSTED")
            self.condition = "BUSTED"

    def brake_car(self, flag=0):
        if flag == 0:
            print(f"--> {self.model_no} SLOWING DOWN \t >>|>")
            self.condition = "SLOW"
        else:
            print(f"{self.model_no} TOTALED")
            self.condition = "BUSTED"

    def left_turn(self):
        print(f"--> {self.model_no} TURNING LEFT \t >>↑↑")
        self.condition = "ON"

    def right_turn(self):
        print(f"--> {self.model_no} TURNING RIGHT \t >>↓↓")
        self.condition = "ON"


if __name__ == "__main__":
    name = input("Name and Model of your car : ")

    car_obj = Car(name)

    command_list_1 = ("START", "STOP")
    command_list_2 = ("ACCELERATE", "BRAKE")
    command_list_3 = ("LEFT", "RIGHT")

    while True:
        print("_" * 15, "\n--Command List--")
        print(command_list_1, "\n", command_list_2, "\n", command_list_3)
        command = input("==> ").upper()

        if command not in (command_list_1 + command_list_2 + command_list_3):
            print("Wrong Command. Try Again...")
        else:
            if command in command_list_1:
                if car_obj.condition == "ON":
                    if command == "START":
                        car_obj.start_car(1)
                    else:
                        car_obj.stop_car()
                elif car_obj.condition == "PARKED":
                    if command == "START":
                        car_obj.start_car()
                    else:
                        car_obj.stop_car(1)
                else:
                    if command == "START":
                        car_obj.start_car()
                    else:
                        car_obj.stop_car()
            elif command in command_list_3:
                if car_obj.condition == "ON":
                    if command == "LEFT":
                        car_obj.left_turn()
                    else:
                        car_obj.right_turn()
                else:
                    if car_obj.condition == "PARKED":
                        print("TURN ON <ENGINE> TO TURN")
                    else:
                        if command == "LEFT":
                            car_obj.left_turn()
                        else:
                            car_obj.right_turn()
            else:
                if car_obj.condition == "ON":
                    if command == "ACCELERATE":
                        car_obj.accelerate_car()
                    else:
                        car_obj.brake_car()
                elif car_obj.condition == "PARKED":
                    print("TURN ON <ENGINE> TO ACCELERATE OR DECELERATE")
                elif car_obj.condition == "SPEED":
                    if command == "ACCELERATE":
                        car_obj.accelerate_car(1)
                    else:
                        car_obj.brake_car()
                else:
                    if command == "ACCELERATE":
                        car_obj.accelerate_car()
                    else:
                        car_obj.brake_car(1)

            if car_obj.condition == "BUSTED":
                print("XXX GAME OVER XXX")
                break
