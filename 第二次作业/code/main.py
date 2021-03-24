import os

from naive_bayes import *
from validation import *

with open('D:/文件仓库/自然语言处理/NLP/第二次作业/code/data.txt', 'rb') as f:
    data = pickle.load(f)
outcome, vocabulary_times, vocabulary_probability = test(data)

# 输出分类结果
print("+" * 80)
for key in outcome.keys():
    for key2 in outcome[key].keys():
        print(outcome[key][key2], end='\t')
    print()
print("+" * 80)

# 计算精度
precisions, total_precision = validation(outcome)
for root, dir, file in os.walk('D:/文件仓库/自然语言处理/NLP/第二次作业/20_newsgroups'):
    i = 0
    for sub_dir in dir:
        print(sub_dir + "的精度为" + "{}".format(precisions[i]))
        i += 1
print("+" * 30)

print("所有文档总的精度为", total_precision)

a = input("输入任意字符回车退出")
print("再见")
