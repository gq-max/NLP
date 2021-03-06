import numpy as np


class GMM:
    def __init__(self, k=2):
        self.k = k  # 定义聚类个数,默认值为2
        self.p = None  # 样本维度
        self.n = None  # 样本个数
        # 声明变量
        self.params = {
            "pi": None,  # 混合系数1*k
            "mu": None,  # 均值k*p
            "cov": None,  # 协方差k*p*p
            "pji": None  # 后验分布n*k
        }

    def init_params(self, init_mu):
        pi = np.ones(self.k) / self.k
        mu = init_mu
        cov = np.ones((self.k, self.p, self.p))
        cov = cov.astype(np.float32)
        pji = np.zeros((self.n, self.k))
        self.params = {
            "pi": pi,  # 混合系数1*k
            "mu": mu,  # 均值k*p
            "cov": cov,  # 协方差k*p*p
            "pji": pji  # 后验分布n*k
        }

    def gaussian_function(self, x_j, mu_k, cov_k):
        one = -((x_j - mu_k) @ np.linalg.pinv(cov_k + 10e-8) @ (x_j - mu_k).T) / 2
        two = -self.p * np.log(2 * np.pi) / 2
        three = -np.log(np.linalg.det(cov_k)) / 2
        return np.exp(one + two + three)

    def E_step(self, x):
        pi = self.params["pi"]
        mu = self.params["mu"]
        cov = self.params["cov"]

        for j in range(self.n):
            x_j = x[j]
            pji_list = []
            for i in range(self.k):
                pi_k = pi[i]
                mu_k = mu[i]
                cov_k = cov[i]
                pji_list.append(pi_k * self.gaussian_function(x_j, mu_k, cov_k))
            self.params['pji'][j, :] = np.array([v / np.sum(pji_list) for v in pji_list])

    def M_step(self, x):
        mu = self.params["mu"]
        pji = self.params["pji"]
        for i in range(self.k):
            mu_k = mu[i]  # p
            pji_k = pji[:, i]  # n
            pji_k_j_list = []
            mu_k_list = []
            cov_k_list = []
            for j in range(self.n):
                x_j = x[j]  # p
                pji_k_j = pji_k[j]
                pji_k_j_list.append(pji_k_j)
                mu_k_list.append(pji_k_j * x_j)
            self.params['mu'][i] = np.sum(mu_k_list, axis=0) / np.sum(pji_k_j_list)
            for j in range(self.n):
                x_j = x[j]  # p
                pji_k_j = pji_k[j]
                cov_k_list.append(pji_k_j * np.dot((x_j - mu_k).T, (x_j - mu_k)))
            self.params['cov'][i] = np.sum(cov_k_list, axis=0) / np.sum(pji_k_j_list)
            self.params['pi'][i] = np.sum(pji_k_j_list) / self.n
        print("均值为：", self.params["mu"].T[0], end=" ")
        print("方差为：", self.params["cov"].T[0][0], end=" ")
        print("混合系数为：", self.params["pi"])

    def fit(self, x, mu, max_iter=10):
        x = np.array(x)
        self.n, self.p = x.shape
        self.init_params(mu)

        for i in range(max_iter):
            print("第{}次迭代".format(i))
            self.E_step(x)
            self.M_step(x)
        return np.argmax(np.array(self.params["pji"]), axis=1)


def result():
    from sklearn.mixture import GaussianMixture
    import pickle
    with open("D:/文件仓库/自然语言处理/NLP/第三次作业/word_vectors.txt", 'rb') as f:
        word_vectors = pickle.load(f)

    gmm = GaussianMixture(3, random_state=10)
    labels = gmm.fit_predict(word_vectors)
    labels = np.array(labels)

    labels[np.where(labels == 0)] = 3
    labels[np.where(labels == 1)] = 4
    labels[np.where(labels == 2)] = 5
    labels[np.where(labels == 3)] = 1
    labels[np.where(labels == 4)] = 2
    labels[np.where(labels == 5)] = 0

    return labels

