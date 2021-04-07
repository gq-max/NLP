from sklearn.cluster import KMeans
import pickle
import numpy as np


def k_means():
    with open("D:/文件仓库/自然语言处理/NLP/第三次作业/word_vectors.txt", 'rb') as f:
        word_vectors = pickle.load(f)

    kmeans = KMeans(n_clusters=3, random_state=5)
    kmeans.fit(word_vectors)
    result = kmeans.labels_
    result = np.array(result)

    result[np.where(result == 0)] = 3
    result[np.where(result == 1)] = 4
    result[np.where(result == 2)] = 5
    result[np.where(result == 3)] = 2
    result[np.where(result == 4)] = 1
    result[np.where(result == 5)] = 0

    return result
