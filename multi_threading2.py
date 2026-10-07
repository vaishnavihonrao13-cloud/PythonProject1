import threading
import time
def download():
    print("downloading....")
    time.sleep(10)
    print("complete....")
def email():
    print("email sending....")
    time.sleep(5)
    print("complete....")
t1= threading.Thread(target=download())
t2= threading.Thread(target=email())
t1.start()
t2.start()
t1.join()
t2.join()
print('complete....')