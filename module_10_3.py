import threading
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            replenishment_balance = randint(50, 500)
            with self.lock:
                if self.balance < 500 and self.lock.locked():
                    self.balance += replenishment_balance
                    print(f'Пополнение: {replenishment_balance}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            reducing_balance = randint(50, 500)
            print(f' Запрос на {reducing_balance}')
            with self.lock:
                if reducing_balance <= self.balance:
                    self.balance -= reducing_balance
                    print(f'Снятие: {reducing_balance}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонен, недостаточно средств')
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')