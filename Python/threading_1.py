from threading import Thread
import time
class Threadss1():
    def first_thread(self):
        for i in range(5):
            print("one")
            time.sleep(1)

class Threadss2():
    def two_thread(self):
        for i in range(5):
            print("two")
            time.sleep(1)

s1 = Threadss1()
s2 = Threadss2()

s1thread = Thread(target=s1.first_thread)
s2thread = Thread(target=s2.two_thread)

s1thread.start()
time.sleep(0.1)
s2thread.start()
