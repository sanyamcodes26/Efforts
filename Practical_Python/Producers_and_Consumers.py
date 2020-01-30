import threading as th
import time as ti
import random as ra
import queue as qu


class Producer:
    def __init__(self):
        self.product = ['nail', 'fork', 'cabbage', 'hammer']
        self.next = 0

    def run(self):
        global q
        while ti.perf_counter() < 10:
            if self.next < ti.perf_counter() and not q.full():
                print(">> ", "*" * 15)
                print(f">> QUEUE LENGTH IN: {q.qsize()}")
                f = ra.choice(self.product)
                g = ra.choice(self.product)
                q.put(f)
                q.put(g)
                print(f">> ADDED :: {f} ")
                print(f">> ADDED :: {g} ")
                print(f">> QUEUE LENGTH OUT: {q.qsize()}")
                self.next += ra.random()


class Consumer:
    def __init__(self):
        self.next = 0

    def run(self):
        global q
        while ti.perf_counter() < 10:
            if not q.empty():
                if self.next < ti.perf_counter():
                    print(">> ", "*" * 15)
                    print(f">> QUEUE LENGTH IN: {q.qsize()}")
                    f = q.get()
                    print(f">> REMOVED :: {f} ")
                    print(f">> QUEUE LENGTH OUT: {q.qsize()}")
                    self.next += ra.random()
            else:
                print(">> ", "*" * 15)
                print(">> CONSUMER -- WAITING")


if __name__ == "__main__":
    global q
    q = qu.Queue(10)

    prod = Producer()
    con_1 = Consumer()
    con_2 = Consumer()

    prod_thread = th.Thread(target=prod.run, args=())
    con_1_thread = th.Thread(target=con_1.run, args=())
    con_2_thread = th.Thread(target=con_2.run, args=())

    prod_thread.start()
    con_1_thread.start()
    con_2_thread.start()
