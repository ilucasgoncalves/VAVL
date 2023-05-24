import re
import json
import json
import numpy as np
from openpyxl import Workbook

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Initialize a dictionary to store the statistics for each mode
    stats = {'acoustic': {}, 'visual': {}, 'audiovisual': {}}
    modes = ['acoustic', 'visual', 'audiovisual']
    measures = ['F1-Score Macro', 'F1-Score Micro', 'Precision Macro', 'Precision Micro', 'Recall Macro', 'Recall Micro']

    # Iterate through each mode
    for mode in modes:
        # Find the last occurrence of the mode in the file
        last_occurrence = content.rfind(f"This is mode: {mode}")

        if last_occurrence != -1:
            # Extract the relevant statistics
            stat_block = content[last_occurrence:]
            for measure in measures:
                regex = rf"{measure} = (\d+\.\d+)"
                match = re.search(regex, stat_block)
                if match:
                    value = float(match.group(1))
                    # Store the values in a short form
                    short_measure = measure.split(' ')[0] + '-ma' if 'Macro' in measure else measure.split(' ')[0] + '-mi'
                    stats[mode].setdefault(short_measure, []).append(value)
        else:
            print(f"Mode {mode} not found in file {filename}")

    return stats

def main():
    file_prefix = 'partition_'
    file_suffix = '.out'
    num_files = 5

    summary_stats = {'acoustic': {}, 'visual': {}, 'audiovisual': {}}

    for i in range(1, num_files + 1):
        file_stats = process_file(file_prefix + str(i) + file_suffix)

        for mode in file_stats.keys():
            for measure, value in file_stats[mode].items():
                summary_stats[mode].setdefault(measure, []).extend(value)

    with open('summary.json', 'w') as f:
        json.dump(summary_stats, f, indent=2)



    # Read the JSON file
    with open("summary.json", "r") as file:
        data = json.load(file)

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"

    # Write header row
    headers = ["Mode", "Metric", "Values", "Mean", "Variance"]
    ws.append(headers)

    # Write data to the worksheet
    for mode, metrics in data.items():
        for metric, values in metrics.items():
            values_array = np.array(values)
            mean = np.mean(values_array)
            variance = np.var(values_array)
            row = [mode, metric, ", ".join(map(str, values)), mean, variance]
            ws.append(row)

    # Save the workbook to an Excel file
    wb.save("summary.xlsx")

if __name__ == '__main__':
    main()
