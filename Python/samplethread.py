from threading import Thread
import time
class TestThread1:
    def printone(self):
        for _ in range(5):
            print("one")
            time.sleep(1)

class TestThread2:
    def print_two(self):
        for _ in range(5):
            print("two")
            time.sleep(1)

s1 = TestThread1()
s2 = TestThread2()

s1thread = Thread(target=s1.printone)
s2thread = Thread(target=s2.print_two)

s1thread.start()
time.sleep(0.1)
s2thread.start()

s1thread.join
s2thread.join
