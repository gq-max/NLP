import math
import pickle


def train(data):
    # 训练部分
    class_frequency_dict = dict()
    frequency_all = dict()  # 所有训练集的词频

    for key in data.keys():
        value = data[key]  # 取对应类别的数据
        total_word_set = set()  # 取某一类中出现过的所有词
        frequency = dict()  # 统计某一类别的词频
        word_count_class = 0  # 统计某一类词的总数
        word_count = 0  # 统计某一类词的总数
        for i in range(800):
            total_word_set.update(value[i])
        for item in total_word_set:
            frequency[item] = 1
        for i in range(800):
            word_count += len(value[i])
            for word in value[i]:
                frequency[word] = frequency[word] + 1
                try:
                    frequency_all[word] = frequency_all[word] + 1
                except KeyError as e:
                    frequency_all[word] = 1
        class_frequency_dict[key] = frequency

    # 计算概率
    word_sum = 0
    key_delete_number = 0
    word_sum = len(frequency_all.keys()) - key_delete_number
    total_class_probability = dict()  # 所有分类词条件概率的总和
    for key in class_frequency_dict.keys():
        per_class_probability = dict()  # 每个分类的条件概率
        for word, word_times in class_frequency_dict[key].items():
            per_class_probability[word] = float(math.log(2.0 / word_sum))
        total_class_probability[key] = per_class_probability
    return word_sum, total_class_probability, class_frequency_dict


def test(data):
    # 测试部分
    word_sum, total_class_probability, class_frequency_dict = train(data)
    text_outcome = dict()
    none_probability = float(math.log(1.0 / word_sum))
    for class_name, class_data in data.items():
        text_data = class_data[:-200:-1]  # 取最后的数据做测试集
        text_outcome_perclass = dict()
        for outcome_name in data.keys():
            text_outcome_perclass[outcome_name] = 0
        for single_data in text_data:
            single_data_class_probability = -100000000
            single_data_class = 'none'
            for belong_class, class_probability in total_class_probability.items():
                probability = 0
                for single_word in set(single_data):
                    try:
                        probability = class_probability[single_word] + probability
                    except KeyError as e:
                        probability = none_probability + probability
                probability = probability + math.log(1 / 20.0)
                if probability > single_data_class_probability:  # 因为取了对数，所以判断条件相反
                    single_data_class_probability = probability
                    single_data_class = belong_class
            text_outcome_perclass[single_data_class] = text_outcome_perclass[single_data_class] + 1
        text_outcome[class_name] = text_outcome_perclass
    return text_outcome, class_frequency_dict, total_class_probability
