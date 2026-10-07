import threading
print(threading.current_thread())

threading.current_thread().name = "mythread"

print(threading.current_thread())

def task():
    print("task executing...")

mytask = threading.Thread(target=task)
t2 = threading.Thread(target=task)

mytask.start()
t2.start()

mytask.join()
t2.join()

print("task finished...")