preprocess.py是文件预处理部分，将所有的文件去除停用词和提取词干后通过pickle转换为data.txt

naive_bayes.py是用来处理转换后的文件的，先统计词频转换为向量，在通过朴素贝叶斯训练模型，最后用百分之二十的数据测试

validation.py是计算模型的准确率的

main.py是运行文件

data.txt是转换之后的文件

