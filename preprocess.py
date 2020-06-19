# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-06-19
# @Author  : mrdon
# @FileName: preprocess.py
# @Software: PyCharm


import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser

LTP_DATA_DIR = './ltp_data_v3.4.0'  # You can change this variable to your own path
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')
f = open('./train/CGED16_HSK_Train_Text.txt', 'r', encoding='utf-8')  # You can change this variable to your own path
g = open('./train/CGED16_HSK_CRF_Input.txt', 'w', encoding='utf-8')  # You can change this variable to your own path


def process(text):
    segmentor = Segmentor()
    postagger = Postagger()
    parser = Parser()
    segmentor.load(cws_model_path)
    postagger.load(pos_model_path)
    parser.load(par_model_path)
    words = segmentor.segment(text)
    postags = postagger.postag(words)
    arcs = parser.parse(words, postags)
    for i in range(len(words)):
        if len(words[i]) == 1:
            if arcs[i].head != 0:
                g.write(
                    words[i] + ' B-' + postags[i] + ' B-' + words[i] + ' B-' + words[arcs[i].head - 1] + ' B-' + arcs[
                        i].relation + '\n')
            else:
                g.write(
                    words[i] + ' B-' + postags[i] + ' B-' + words[i] + ' B-' + 'Root' + ' B-' + arcs[i].relation + '\n')
        if len(words[i]) >= 2:
            if arcs[i].head != 0:
                g.write(words[i][0] + ' B-' + postags[i] + ' B-' + words[i] + ' B-' + words[arcs[i].head - 1] + ' B-' +
                        arcs[i].relation + '\n')
                for j in range(1, len(words[i])):
                    g.write(
                        words[i][j] + ' I-' + postags[i] + ' I-' + words[i] + ' I-' + words[arcs[i].head - 1] + ' I-' +
                        arcs[i].relation + '\n')
            else:
                g.write(words[i][0] + ' B-' + postags[i] + ' B-' + words[i] + ' B-' + 'Root' + ' B-' + arcs[
                    i].relation + '\n')
                for j in range(1, len(words[i])):
                    g.write(words[i][j] + ' I-' + postags[i] + ' I-' + words[i] + ' I-' + 'Root' + ' I-' + arcs[
                        i].relation + '\n')
    segmentor.release()
    postagger.release()
    parser.release()


if __name__ == "__main__":
    for line in f:
        process(line.strip())
        g.write('\n')
    f.close()
    g.close()
