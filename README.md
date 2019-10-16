# Lab-Logger
Lab-Logger is a GUI program that can be used to take measurements with time to make taking lab measurements easier. The way the program works is by displaying a stopwatch timer, entry box, and a few buttons: start, pause, reset, log, graph, and export.   
The user starts the stopwatch and whenever would like to take a measurement would type the measurement in the entry box and press log. The program then takes the measurement and current time and saves them to a JSON file as a list pair `["00:00", 0]`

## Buttons
Here are the different buttons and what they do.

### Start
The start button starts the stopwatch or continues it if it was paused.

### Pause
The pause button pauses the stopwatch if it's already running. The other buttons are still functional while the stopwatch is paused.

### Reset
The reset button resets the stopwatch back to zero and keeps running if it was running when the button was pressed.

### Log
The log button takes whatever's in the entry box at the time of the button press and saves it to the JSON file with the time alongside it. If nothing is in the entry box, it saves a zero.

### Graph
The graph button takes all the currently logged data from the JSON file and graphs it.

### Export
The export button takes the data from the JSON file and saves it to a text file in a readable table form.
