import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import numpy as np
from PCA import EM_pca


def load_data(file):

    with open(file, 'rb') as f:
        data = pickle.load(f)

    data_classes = []  # 文件类型
    voc_list = []  # 单词列表

    for key in data.keys():
        data_classes.append(key)
        voc_list.append(data[key])

    return data_classes, voc_list


def get_tfidf(words):
    words_list = []
    for word in words:
        for i in word:
            words_transit = ",".join(i)
            words_list.append(words_transit)
    transformer = TfidfVectorizer()
    tfidf = transformer.fit_transform(words_list)
    tfidf_arr = tfidf.toarray()
    return tfidf_arr


def word2vector(file):
    data_classes, voc_list = load_data(file)
    word_vectors = get_tfidf(voc_list)
    word_vectors = np.array(word_vectors)

    # # 采用自己写的PCA算法
    # word_vectors_transform = word_vectors.T
    # new_word_vectors = EM_pca(word_vectors_transform, 1000)
    # new_word_vectors = new_word_vectors.T

    # 调用包
    pca = PCA(n_components=2000)
    new_word_vectors = pca.fit_transform(word_vectors)
    print("将数据降到2000维后保留的信息量为：", sum(pca.explained_variance_ratio_))
    return new_word_vectors


word_vectors = word2vector("D:/文件仓库/自然语言处理/NLP/第三次作业/data.txt")
with open('../my_word_vectors.txt', 'wb+') as f:
    pickle.dump(word_vectors, f)

