from threading import *
class Myclass(Thread):
    def run(self):
        print("hello from thread")
obj=Myclass()
obj.start()