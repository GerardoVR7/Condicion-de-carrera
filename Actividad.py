import threading
import time
import random
class Cinema():
    def __init__(self,tickets=20, snacks= 0, client1=0, client2=0):
        self.locked = threading.Lock()
        self.stockTicket = tickets
        self.snacksSells =  snacks
        self.client1 = client1
        self.client2 = client2

    def buy(self, num):
        self.locked.acquire()
        try:
            self.stockTicket = self.stockTicket - num
            self.client1 += 1
            print(f"Cliente{self.client1} Stock de tickets: {self.stockTicket}")
        finally:
            self.locked.release()


    def snacks(self, num):
        self.locked.acquire()
        try:
            self.snacksSells += num
            self.client2 += 1
            print(f"Client{self.client2} Sells of snacks: {self.snacksSells}")
        finally:
            self.locked.release()

def day(cinema):

    for i in range(3):
        num = 0
        num = random.randint(1,3)
        # print(numTickets)
        time.sleep(1)
        cinema.buy(num)
        num = random.randint(1,3)
        cinema.snacks(num)


if __name__ == '__main__':
    cinema = Cinema()
    for y in range (3):
        client1 = threading.Thread(target=day, args=(cinema,))
        client1.start()



