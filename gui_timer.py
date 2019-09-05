import tkinter as tk  # Imports the library tkinter, to do all the graphical interface stuff.
from time import sleep  # Imports the sleep module from the time library.
import data_handler  # Imports the module I wrote to handle the JSON data.
from grapher import graph_data  # Imports the function that graphs the current data.


# Takes the current time from the global variables minutes and seconds and returns them in a string format (00:00).
def format_time():
    global m, s
    return f'{"%02d" % m}:{"%02d" % s}'


# Adds 1 to the minutes and sets seconds to 0 if the number of seconds reaches 60.
def min_check():
    global m
    global s
    if s >= 60:
        m += 1
        s = 0


labData = data_handler.File('JSON File Name')  # Defines a variable, labData, as a File object.
root = tk.Tk()  # Initializes a tkinter window (GUI window).

pauseReq = False  # Defines a variable, pauseReq, as false. This stores whether or not the Pause button is pressed.
resetReq = False  # Defines a variable, resetReq, as false. This stores whether or not the reset button is pressed.
m, s = 0, 0  # defines minutes and seconds as an initial value of 0.
time = tk.StringVar()  # Defines time as manipulable tkinter variable (so that the text could be changed in the GUI).
time.set(format_time())  # Defines the time tkinter variable as an empty time str (00:00).


#                   DISCARDED CODE
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
#
#def check_req():
#    if pauseReq:  # if pauseReq == True
#        return True
#    elif not pauseReq:  # if pauseReq == False
#        return False
#    else:
#        raise ValueError('EReraadad 101010fsoafj beep boop boop beep beep')

# Starts the timer and adds the time onto the current global time amount.
def timer():
    global pauseReq, resetReq, time, m, s
    while True:  # Infinite loop of time.
        if pauseReq:  # If the pause button was pressed, sets pauseReq back to false and breaks out of the time loop.
            pauseReq = False
            break
        elif resetReq:  # If the reset button was pressed, sets resetReq back to false and breaks out of the time loop (the minutes and seconds have already been reset somewhere else).
            resetReq = False
            break
        root.update()  # Updates the GUI window
        s += 1  # Adds 1 to the seconds
        min_check()  # Checks if the seconds reached 60 and needs to go into minutes.
        sleep(1)  # Program stops for 1 second
        time.set(f'{"%02d" % m}:{"%02d" % s}')  # Sets the time text to the new current time.
        root.update()  # Updates the GUI window
    root.update()  # Updates the GUI window outside the loop (unsure if this is needed but I have it in case).


# Changes the pressed state of the buttons.
def request(var, boolean: bool):
    global pauseReq, resetReq, m, s
    # Changes correct request variable depending on which one was requested to change.
    if var == 'pause':
        pauseReq = boolean
    elif var == 'reset':
        resetReq = boolean
        if resetReq:  # If a reset was requested, sets time to 0, sets to the request back to false, and updates the text and GUI window.
            m = 0
            s = 0
            resetReq = False
            time.set(f'{"%02d" % m}:{"%02d" % s}')
            root.update()
    else:
        raise TypeError('Expected boolean')  # Raises a TypeError if it receives a value that isn't a boolean.


# Saves new measurement at time of button press to the JSON file.
def log_data():
    labData.new([f'{"%02d" % m}:{"%02d" % s}', float(data.get())])
    data.delete(0, tk.END)  # Deletes what was in the textbox.


display = tk.Label(root, padx=5, pady=5, textvariable=time)  # Timer label
start = tk.Button(root, padx=5, pady=5, text='Start', command=timer)  # Start button
pause = tk.Button(root, padx=5, pady=5, text='Pause', command=lambda *args: request('pause', True))  # Pause button
reset = tk.Button(root, padx=5, pady=5, text='Reset', command=lambda *args: request('reset', True))  # Reset button
data = tk.Entry(root)  # Data textbox
log = tk.Button(root, padx=5, pady=5, text='Log', command=lambda *args: log_data())  # Log button
export = tk.Button(root, padx=5, pady=5, text='Export', command=lambda *args: labData.export('Export File Name'))  # Export button
graph = tk.Button(root, padx=5, pady=5, text='Graph', command=lambda *args: graph_data(labData.name))  # Graph button

# Positions all the tkinter GUI elements in it's correct position in the window.
display.grid(row=0, column=0)
start.grid(row=1, column=0)
pause.grid(row=0, column=1)
reset.grid(row=1, column=1)
reset.grid(row=1, column=1)
data.grid(row=0, column=2)
log.grid(row=1, column=2)
export.grid(row=1, column=3)
graph.grid(row=0, column=3)

tk.mainloop()  # Begins the window loop
