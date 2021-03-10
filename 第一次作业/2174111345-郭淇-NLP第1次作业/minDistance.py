import numpy as np
import copy


def minDistance(str1, str2, insert_cost=1, delete_cost=1, replace_cost=1):
    '''
    最小编辑距离，可以修改操作代价
    :param str1:字符串1
    :param str2:字符串2
    :param insert_cost:插入代价，默认为1
    :param delete_cost:删除代价，默认为1
    :param replace_cost:替换代价，默认为1
    :return:最小编辑距离
    '''
    m = len(str1)
    n = len(str2)

    # 定义表
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    bt = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 回退路径，2表示插入，3表示删除，1表示替换或匹配

    # 初始化
    for i in range(n + 1):
        dp[0][i] = i * insert_cost
        bt[0][i] = 2
    for j in range(m + 1):
        dp[j][0] = j * delete_cost
        bt[j][0] = 3
    bt[0][0] = 0

    # 状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                replace = dp[i - 1][j - 1]
            else:
                replace = dp[i - 1][j - 1] + replace_cost
            insert = dp[i][j - 1] + insert_cost
            delete = dp[i - 1][j] + delete_cost

            dp[i][j] = min(replace, min(insert, delete))

            # 回溯使用
            if dp[i][j] == replace:
                bt[i][j] = 1
            elif dp[i][j] == insert:
                bt[i][j] = 2
            else:
                bt[i][j] = 3
    print("状态转移矩阵为：")
    for k in range(m + 1):
        print(str(dp[k]) + "\t")
    return dp[m][n], bt


def back_trace(bt):
    (m, n) = np.array(bt).shape
    retain = []
    while True:
        retain.append(bt[m - 1][n - 1])
        if bt[m - 1][n - 1] == 1:
            m -= 1
            n -= 1
        elif bt[m - 1][n - 1] == 2:
            n -= 1
        else:
            m -= 1
        if bt[m - 1][n - 1] == 0:
            break
    return list(reversed(retain))


def transform(retain, str1, str2):
    k = len(retain)
    str3 = copy.deepcopy(str1) + ' ' * len(str2)
    i = j = 0
    for iter in range(k):
        if retain[iter] == 1:
            if str3[i] == str2[j]:
                i += 1
                j += 1
            else:
                l = copy.deepcopy(str3)
                str3 = str3[0:i] + str2[j] + str3[i + 1:]
                print("将{}改为{}".format(l, str3))
                i += 1
                j += 1
        elif retain[iter] == 2:
            l = copy.deepcopy(str3)
            str3 = str3[0:i] + str2[j] + str3[i:]
            print("将{}改为{}".format(l, str3))
            i += 1
            j += 1
        else:
            l = copy.deepcopy(str3)
            str3 = str3[0:i] + str3[i + 1:]
            print("将{}改为{}".format(l, str3))


if __name__ == '__main__':
    str1 = input("请输入字符串1:")
    str2 = input("请输入字符串2:")
    insert_num = int(input("请输入增加代价:"))
    delete_num = int(input("请输入删除代价:"))
    replace_num = int(input("请输入更改代价:"))

    distance, backtrace = minDistance(str1, str2, insert_num, delete_num, replace_num)
    print("{}和{}的编辑距离为{}".format(str1, str2, distance))
    retain = back_trace(backtrace)

    print("修改步骤为：")
    transform(retain, str1, str2)

    input("输入任意字母后回车退出")
