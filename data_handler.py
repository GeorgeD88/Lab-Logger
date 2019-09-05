import json  # Imports the library, json, to deal with JSON data.


class File:  # Class for file objects so that you could call methods on a file instead of retyping the filename everytime you call a function with that file.

    def __init__(self, file_name: str):
        self.name = file_name  # Defines attribute, self.name, as the name of the file.
        try:  # Tries to open a JSON file with the name of object, if it doesn't exist it throws an error.
            with open(self.name + '.json', 'r') as in_file:  # Opens JSON file for reading
                pass  # Does nothing
        except FileNotFoundError:  # If it catches a FileNotFoundError, it makes one with an empty data list.
            with open(self.name + '.json', 'w+') as out_file:  # Opens new JSON file for writing
                json.dump({'intervals': []}, out_file)  # Saves empty data list

    # Saves new list pair of data [time, measurement] to the list of lists in the JSON file of the object.
    def new(self, interval: tuple or list):
        with open(self.name + '.json', 'r') as in_file:  # Opens the JSON file for reading
            data = json.load(in_file)  # Defines a variable, data, as the contents of the JSON file.
        data['intervals'].append(interval)  # Appends the argument, interval, to the list of intervals.
        with open(self.name + '.json', 'w') as out_file:  # Opens the JSON file for writing
            json.dump(data, out_file)  # Dumps the edited list back into the JSON.

    # Saves the current data in the JSON file to a text file in a readable table format.
    def export(self, export_file_name: str):
        with open(self.name + '.json', 'r') as in_file:  # Opens the JSON file for reading
            data = json.load(in_file)  # Defines a variable, data, as the contents of the JSON file.
        intervals = data['intervals']  # Defines a variable for iteration, intervals, as the data that was logged.
        export = ' Time | Data\n-------------\n'  # Defines a variable, export, as a string with the beginning of the table which will have data added to it.
        for interv in intervals:  # Iterates through the list of data recorded at every interval of time.
            export += f'{interv[0]} | {interv[1]}\n'  # Adds the data to the table in the correct table format.
        with open(export_file_name + '.txt', 'w+') as out_file:  # Opens a new file, or overwrites one.
            out_file.write(export)  # Saves the table string to the text file.
