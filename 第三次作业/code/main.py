from GMM import result
import numpy as np
from evaluate import evaluate
from k_means import k_means


def main():
    label_name = ['rec.motorcycles', 'sci.electronics', 'talk.politics.guns']

    # 高斯混合模型
    predicted_labels = result()

    # # k-means聚类
    # predicted_labels = k_means()

    true_labels = []

    for i in range(3):
        for j in range(1000):
            true_labels.append(i)
    true_labels = np.array(true_labels)

    nmi, acc, ri, confusion_matrix = evaluate(true_labels, predicted_labels)
    print("通过GMM聚类运行的结果为：")
    print("+" * 80)
    print("混淆矩阵为:")
    print("{:20}{:20}{:20}{:20}".format(' ', label_name[0], label_name[1], label_name[2]))
    print("{:20}{:^20}{:^20}{:^20}".format(label_name[0],
                                           confusion_matrix['aa'],
                                           confusion_matrix['ab'],
                                           confusion_matrix['ac']))
    print("{:20}{:^20}{:^20}{:^20}".format(label_name[1],
                                           confusion_matrix['ba'],
                                           confusion_matrix['bb'],
                                           confusion_matrix['bc']))
    print("{:20}{:^20}{:^20}{:^20}".format(label_name[0],
                                           confusion_matrix['ca'],
                                           confusion_matrix['cb'],
                                           confusion_matrix['cc']))
    print("+" * 80)
    print("互信息为{}\n正确率为{}\n调整兰德指数为{}".format(nmi, acc, ri))


def compare():
    GMM = result()
    kmeans = k_means()
    res = [GMM == kmeans]
    res2 = [1 for i in res[0] if i]
    num = len(res2)
    return num


if __name__ == '__main__':
    # main()
    num = compare()
    print("GMM和k-means预测相同的个数为：", num)
    # a = input("输入任意字符退出")
