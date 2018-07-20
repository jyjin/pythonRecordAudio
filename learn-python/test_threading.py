import threading
def func_timer():
    print('Hello timer')
    global timer
    timer = threading.Timer(1, func_timer)
    timer.start()

Timer = threading.Timer(0, func_timer)
Timer.start()