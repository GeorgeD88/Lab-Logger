import tkinter as tk
from time import sleep
import data_handler
from grapher import graph_data


def format_time():
    global m, s
    return f'{"%02d" % m}:{"%02d" % s}'


def min_check():
    global m
    global s
    if s >= 60:
        m += 1
        s = 0


labData = data_handler.File('new_test')
root = tk.Tk()

pauseReq = False
resetReq = False
m, s = 0, 0
time = tk.StringVar()
time.set(format_time())


#def timer():
#    global time, m, s
#    for minU in range(60):
#        for sec in range(60):
#            s += 1
#            sleep(1)
#            time.set(format_time())
#            root.update()
#        s = 0
#        m += 1
#        time.set(format_time())
#        root.update()


#def check_req():
#    if pauseReq:  # if pauseReq == True
#        return True
#    elif not pauseReq:  # if pauseReq == False
#        return False
#    else:
#        raise ValueError('EReraadad 101010fsoafj beep boop boop beep beep')


def timer():
    global pauseReq, resetReq, time, m, s
    while True:
        if pauseReq:
            pauseReq = False
            break
        elif resetReq:
            resetReq = False
            break
        root.update()
        s += 1
        min_check()
        sleep(1)
        time.set(f'{"%02d" % m}:{"%02d" % s}')
        root.update()
    root.update()


def request(var, boolean: bool):
    global pauseReq, resetReq, m, s
    if var == 'pause':
        pauseReq = boolean
    elif var == 'reset':
        resetReq = boolean
        if resetReq:
            m = 0
            s = 0
            resetReq = False
            time.set(f'{"%02d" % m}:{"%02d" % s}')
            root.update()

    else:
        raise ValueError('vAlUeErRoR 91 2[e;')


def log_data():
    labData.new([f'{"%02d" % m}:{"%02d" % s}', float(data.get())])
    data.delete(0, tk.END)


# TODO: Add data visualiser at the end.

display = tk.Label(root, padx=5, pady=5, textvariable=time)
start = tk.Button(root, padx=5, pady=5, text='Start', command=timer)
pause = tk.Button(root, padx=5, pady=5, text='Pause', command=lambda *args: request('pause', True))
reset = tk.Button(root, padx=5, pady=5, text='Reset', command=lambda *args: request('reset', True))
data = tk.Entry(root)
log = tk.Button(root, padx=5, pady=5, text='Log', command=lambda *args: log_data())
export = tk.Button(root, padx=5, pady=5, text='Export', command=lambda *args: labData.export('Test Exp'))
graph = tk.Button(root, padx=5, pady=5, text='Graph', command=lambda *args: graph_data(labData.name))

display.grid(row=0, column=0)
start.grid(row=1, column=0)
pause.grid(row=0, column=1)
reset.grid(row=1, column=1)
reset.grid(row=1, column=1)
data.grid(row=0, column=2)
log.grid(row=1, column=2)
export.grid(row=1, column=3)
graph.grid(row=0, column=3)

tk.mainloop()
