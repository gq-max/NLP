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
    bt = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 回退路径，0表示插入，1表示删除，2表示替换或匹配

    # 初始化
    for i in range(n + 1):
        dp[0][i] = i
    for j in range(m + 1):
        dp[j][0] = j

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
            if dp[i][j] == replace and dp[i][j] == delete and dp[i][j] == insert:
                bt[i][j] = 7
            elif dp[i][j] == insert and dp[i][j] == delete and dp[i][j] != replace:
                bt[i][j] = 6
            elif dp[i][j] == insert and dp[i][j] != delete and dp[i][j] == replace:
                bt[i][j] = 5
            elif dp[i][j] != insert and dp[i][j] == delete and dp[i][j] == replace:
                bt[i][j] = 4
            elif dp[i][j] != insert and dp[i][j] != delete and dp[i][j] == replace:
                bt[i][j] = 3
            elif dp[i][j] != insert and dp[i][j] == delete and dp[i][j] != replace:
                bt[i][j] = 2
            else:
                bt[i][j] = 1
    return dp[m][n], bt


if __name__ == '__main__':
    # str1 = 'cafe'
    # str2 = 'coffee'
    # distance, backtrace = minDistance(str1, str2)
    # print("{}和{}的编辑距离为{}".format(str1, str2, distance))
    # for i in range(len(backtrace)):
    #     print(str(backtrace[i]) + "\t")
    #
    # str1 = 'intention'
    # str2 = 'execution'
    # distance, backtrace = minDistance(str1, str2)
    # print("{}和{}的编辑距离为{}".format(str1, str2, distance))
    # for i in range(len(backtrace)):
    #     print(str(backtrace[i]) + "\t")
    #
    # str1 = 'intention'
    # str2 = 'execution'
    # distance, backtrace = minDistance(str1, str2, replace_cost=2)
    # print("替换代价为2时，{}和{}的编辑距离为{}".format(str1, str2, distance))
    # for i in range(len(backtrace)):
    #     print(str(backtrace[i]) + "\t")
    str1 = 'cafe'
    str2 = 'coffee'
    distance, backtrace = minDistance(str1, str2, replace_cost=2)
    print("删除和修改代价为2时，{}和{}的编辑距离为{}".format(str1, str2, distance))
    for i in range(len(backtrace)):
        print(str(backtrace[i]) + "\t")

