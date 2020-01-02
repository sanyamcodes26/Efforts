import threading
import time
import random


def exec_thread(i):
    print()
    print("{} -> Thread Sleep : {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep = random.randint(1, 5)
    print()
    time.sleep(rand_sleep)
    print()
    print("{} -> Thread Wake : {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    print()


def normal():
    for i in range(10):
        thread = threading.Thread(target=exec_thread, args=(i + 1,))
        thread.start()
        print()
        print("Active Thread :", threading.active_count())
        print("Thread Objects :", threading.enumerate())
    return


def get_time(name):
    print("{} -> Thread Sleep : {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep = random.randint(1, 5)
    time.sleep(rand_sleep)


class Custom_thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        get_time(self.name)
        print("Thread {} ends".format(self.name))


def custom():
    thread1 = Custom_thread("One")
    thread2 = Custom_thread("Two")
    thread1.start()
    thread2.start()
    print(thread1.getName())
    print("Thread Alive :", thread1.is_alive())
    print(thread2.getName())
    print("Thread Alive :", thread2.is_alive())
    thread1.join()
    thread2.join()
    return


thread_lock = threading.Lock()


class Bank_Account(threading.Thread):
    ac_balance = 100

    def __init__(self, name="Default", money_request=0):
        threading.Thread.__init__(self)
        self.name = name
        self.money_request = money_request

    def run(self):
        thread_lock.acquire()
        Bank_Account.get_money(self)
        thread_lock.release()

    @staticmethod
    def get_money(customer):
        print("Name : {}\nWithdrawal : ${}\nTime : {}".format(customer.name, customer.money_request,
                                                              time.strftime("%H:%M:%S", time.gmtime())))
        if Bank_Account.ac_balance - customer.money_request >= 0:
            print("Old Balance :", Bank_Account.ac_balance)
            Bank_Account.ac_balance -= customer.money_request
            print("Current Balance :", Bank_Account.ac_balance)
        else:
            print("Over Drafting Not Allowed")
            print("Current Balance :", Bank_Account.ac_balance)
        print()
        time.sleep(3)


def initial():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    # normal()
    # custom()

    a = Bank_Account("A", 24)
    b = Bank_Account("B", 50)
    c = Bank_Account("C", 150)
    d = Bank_Account("D", 15)

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    return


if __name__ == "__main__":
    initial()
