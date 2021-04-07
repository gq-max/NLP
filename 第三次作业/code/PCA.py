import numpy as np

def EM_pca(data, k):
    p, m = data.shape
    # 初始化
    W = np.random.randn(p, k)
    Z = np.random.randn(k, m)
    x_mean = np.mean(data, axis=1).reshape(p, 1)
    for epoch in range(50):
        print("第{}次迭代".format(epoch))
        # E步
        x_mean = np.mean(data, axis=1).reshape(p, 1)
        data = data - x_mean
        Z = np.linalg.inv(W.T @ W) @ W.T @ data
        # M步
        W = data @ Z.T @ np.linalg.inv(Z @ Z.T)
    return Z