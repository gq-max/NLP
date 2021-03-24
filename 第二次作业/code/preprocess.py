import os
import pickle
import re
import nltk.stem.lancaster as lc


def load_text(filepath=r'D:/文件仓库/自然语言处理/NLP/第二次作业/20_newsgroups', stopwords_file=r'D:/文件仓库/自然语言处理/NLP/第二次作业/stopwords.txt'):
    syntax_list = ['[^a-zA-Z\']']
    word_syntax = re.compile('[a-zA-Z_]*')

    # 加载停用词
    with open(stopwords_file, 'r+', encoding='utf') as f:
        stopwords = list()
        for line in f.readlines():
            stopwords.append(line.strip('\n'))

    for index, syntax in enumerate(syntax_list):
        syntax_list[index] = re.compile(syntax_list[index])

    class_record = dict()
    for root, dir, file in os.walk(filepath):
        for sub_dir in dir:
            # print(sub_dir)
            for new_root, new_dir, textfile_set in os.walk(os.path.join(root, sub_dir)):
                text_record = list()
                for textfile in textfile_set:
                    with open(os.path.join(new_root, textfile), 'r', encoding='windows-1252') as f:
                        text_one_article = f.readlines()
                        for pattern in syntax_list:
                            text_one_article = list(map(lambda x: pattern.sub(' ', x), text_one_article))
                        text_flushed = list()
                        for text in text_one_article:
                            text = text.split()
                            for word in text:
                                if word_syntax.match(word) and word not in stopwords:
                                    text_flushed.append(word.lower())
                        text_record.append(text_flushed)
                class_record[sub_dir] = text_record
    return class_record


def word_stem():
    '''提取词干'''
    stemmer = lc.LancasterStemmer()
    words = load_text()

    class_words = {}
    for root, dir, file in os.walk('D:/文件仓库/自然语言处理/NLP/第二次作业/20_newsgroups'):
        for sub_dir in dir:
            words_stem = []
            n = len(words['{}'.format(sub_dir)])
            for i in range(n):
                list_flashed = []
                for word in words['{}'.format(sub_dir)][i]:
                    stem = stemmer.stem(word)
                    list_flashed.append(word)
                words_stem.append(list_flashed)
            class_words[sub_dir] = words_stem
    return class_words


text = load_text()
with open('./data.txt', 'wb+') as f:
    pickle.dump(text, f)
