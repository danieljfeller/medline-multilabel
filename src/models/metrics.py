import pandas as pd
import numpy as np


def get_binary_results(y_pred, y_test, column_index):
    print("returns: dataframe with precision, recall, and F")
    accuracy, precision, recall, f1 = [], [], [], []
    # iterate over each patient

    # assign true/false to each prediction
    true_neg, true_pos, false_pos, false_neg = 0, 0, 0, 0
    for row_index in range(0, y_pred.shape[0]):
        predictedLabel = np.round(y_pred[row_index, column_index])
        actualLabel = y_test[row_index, column_index]
        if predictedLabel == 0 and predictedLabel == actualLabel:
            true_neg += 1
        elif predictedLabel == 0 and predictedLabel != actualLabel:
            false_pos += 1
        elif predictedLabel == 1 and predictedLabel == actualLabel:
            true_pos += 1
        elif predictedLabel == 1 and predictedLabel != actualLabel:
            false_neg += 1
        else:
            continue

    # precision
    try:
        p = true_pos / (true_pos + false_pos)
    except:
        p = 0
    precision.append(p)
    # recall
    try:
        r = true_pos / (true_pos + false_neg)
    except:
        r = 0
    recall.append(r)
    # f1 score
    try:
        f1.append((2 * p * r) / (p + r))
    except:
        f1.append(0)

    results = pd.DataFrame({'precision': precision,
                            'recall': recall,
                            'f1': f1})

    return results


def get_multiclass_results(y_pred, y_test):
    print("returns: dataframe with precision, recall, and F")
    labels, accuracy, precision, recall, f1 = [], [], [], [], []
    # iterate over each patient
    for class_index in range(0, y_pred.shape[1]):
        labels.append("Label #" + str(class_index))

        # assign true/false to each prediction
        true_neg, true_pos, false_pos, false_neg = 0, 0, 0, 0
        for row_index in range(0, y_pred.shape[0]):
            predictedLabel = np.round(y_pred[row_index,1])
            actualLabel = y_test[row_index, y_test_column_index]
            if predictedLabel == 0 and predictedLabel == actualLabel:
                true_neg += 1
            elif predictedLabel == 0 and predictedLabel != actualLabel:
                false_pos += 1
            elif predictedLabel == 1 and predictedLabel == actualLabel:
                true_pos += 1
            elif predictedLabel == 1 and predictedLabel != actualLabel:
                false_neg += 1
            else:
                continue

        # precision
        try:
            p = true_pos / (true_pos + false_pos)
        except:
            p = 0
        precision.append(p)
        # recall
        try:
            r = true_pos / (true_pos + false_neg)
        except:
            r = 0
        recall.append(r)
        # f1 score
        try:
            f1.append((2 * p * r) / (p + r))
        except:
            f1.append(0)

    results = pd.DataFrame({'label': labels,
                            'precision': precision,
                            'recall': recall,
                            'f1': f1})

    return results