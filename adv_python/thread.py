from threading import *
class Myclass(Thread):
    def run(self):
        print("hello ")
obj=Myclass()
obj.start()



