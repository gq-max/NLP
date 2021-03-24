import numpy as np


def validation(data):
    precisions = []
    precisions_lists = []
    for key in data.keys():
        precisions_list = []
        for key2 in data[key].keys():
            precisions_list.append(data[key][key2])
        precisions_lists.append(precisions_list)
    precisions_array = np.array(precisions_lists)
    accuracy_list = []
    for i in range(len(precisions_array)):
        accuracy_list.append(precisions_array[i][i])
    precisions = [x / 200 for x in accuracy_list]
    total_precision = sum(accuracy_list) / 4000
    return precisions, total_precision
