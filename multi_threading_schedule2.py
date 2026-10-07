import sched
import time
scheduler=sched.scheduler(time.time, time.sleep)
def schedule_event(name, start):
    now = time.time()
    elapsed=int(now -start)
    print('elapsed=',elapsed, 'name=',name)
start=time.time()
print('start',time.ctime(start))
scheduler.enter(2,1,schedule_event,('Event 1',start))
scheduler.enter(3,1,schedule_event,('Event 2',start))
scheduler.run()
