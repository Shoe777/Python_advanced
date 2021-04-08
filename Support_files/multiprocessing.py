import multiprocessing
import os
import time

def func():
    print("hello from process %s" % os.getpid())
    time.sleep(1)

proc = multiprocessing.Process(target=func, args=())
proc.start()
proc = multiprocessing.Process(target=func, args=())
proc.start()