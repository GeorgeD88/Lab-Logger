import json


class File:

    def __init__(self, file_name: str):
        self.name = file_name

    def new(self, interval: tuple or list):
        try:  # If the file it's trying to read doesn't exist yet, it defines data as a dict of an empty list.
            with open(self.name + '.json', 'r') as in_file:
                data = json.load(in_file)
        except FileNotFoundError:
            data = {'intervals': []}

        data['intervals'].append(interval)  # Appends the argument, interval, to the list of intervals.
        with open(self.name + '.json', 'w') as out_file:
            json.dump(data, out_file)  # Dumps the edited list back into the json.

    def export(self, export_file_name: str):
        with open(self.name + '.json', 'r') as in_file:
            data = json.load(in_file)
        intervals = data['intervals']
        export = ' Time | Data\n-------------\n'
        for interv in intervals:
            export += f'{interv[0]} | {interv[1]}\n'
        with open(export_file_name + '.txt', 'w+') as out_file:
            out_file.write(export)
