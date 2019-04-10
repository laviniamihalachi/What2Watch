import csv
import numpy as np


def get_labels(directory):
    test_labels = {}
    with open('./FERPlus/' + directory + '/label.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            label = []
            for i in range(2, 10, 1):
                label.append(float(row[i]))
            maxval = max(label)
            sum_list = sum(label)
            if maxval > 0.5 * sum_list:
                test_labels[row[0]] = np.argmax(label)
                line_count += 1

    print(line_count)
    return test_labels
