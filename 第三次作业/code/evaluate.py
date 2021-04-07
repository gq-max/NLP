from sklearn.metrics import accuracy_score
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import normalized_mutual_info_score


def evaluate(true_labels, predicted_labels):
    # 计算混淆矩阵
    confusion_matrix = compute_confusion_matrix(predicted_labels)

    # 计算互信息
    nmi = normalized_mutual_info_score(true_labels, predicted_labels)

    # 计算准确率
    acc = accuracy_score(true_labels, predicted_labels)

    # 计算调整兰德系数
    ri = adjusted_rand_score(true_labels, predicted_labels)

    return nmi, acc, ri, confusion_matrix


def compute_confusion_matrix(predicted_labels):
    label_name = ['rec.motorcycles', 'sci.electronics', 'talk.politics.guns']
    confusion_matrix = {'aa': 0, 'ab': 0, 'ac': 0,
                        'ba': 0, 'bb': 0, 'bc': 0,
                        'ca': 0, 'cb': 0, 'cc': 0}

    for predicted_label in predicted_labels[:1000]:
        if predicted_label == 0:
            confusion_matrix['aa'] += 1
        elif predicted_label == 1:
            confusion_matrix['ab'] += 1
        else:
            confusion_matrix['ac'] += 1

    for predicted_label in predicted_labels[1000:2000]:
        if predicted_label == 0:
            confusion_matrix['ba'] += 1
        elif predicted_label == 1:
            confusion_matrix['bb'] += 1
        else:
            confusion_matrix['bc'] += 1

    for predicted_label in predicted_labels[2000:3000]:
        if predicted_label == 0:
            confusion_matrix['ca'] += 1
        elif predicted_label == 1:
            confusion_matrix['cb'] += 1
        else:
            confusion_matrix['cc'] += 1
    return confusion_matrix
