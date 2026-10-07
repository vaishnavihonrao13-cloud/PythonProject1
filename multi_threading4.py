import _thread
import timek

def thread_task(threadName, delay):
    for count in range(1, 6):
        time.sleep(delay)
        print("Thread name: {} count: {}".format(threadName, count))

try:
    _thread.start_new_thread(thread_task, ("thread 1", 1))
    _thread.start_new_thread(thread_task, ("thread 2", 2))

except:
    print("error: unable to start")

while True:
    pass