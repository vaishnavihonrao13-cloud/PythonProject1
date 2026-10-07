import threading
import time

def schedule_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print('elapsed:', elapsed, 'name:', name)

start = time.time()

print('start:', time.ctime(start))

t1 = threading.Timer(3, schedule_event, args=('event 1', start))
t2 = threading.Timer(1, schedule_event, args=('event 2', start))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print('end:', time.ctime(end))