import threading
import time
lock = threading.Lock()
def even():
    for i in range(1,21):
        if i%2==0:
            with lock:
                print(i)
                time.sleep(2)
def table(n):
    for i  in range(1,11):
        with lock:
            print(i*n)
            time.sleep(1)
even=threading.Thread(target=even())
table=threading.Thread(target=table , args = (10, ))
even.start()
table.start()
even.join()
table.join()
print('complete....')
