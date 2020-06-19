# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-06-19
# @Author  : mrdon
# @FileName: client.py
# @Software: PyCharm


import os
import sys
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser

LTP_DATA_DIR = './ltp_data_v3.4.0'  # You can change this variable to your own path
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')


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
                        i].relation + ' \n')
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
    print('\n')
    print('************************************************************')
    print('Welcome to Chinese Grammar Error Diagnosis System')
    print('Grammar errors type defined as:')
    print('words redundant errors (denoted as a capital "R")')
    print('words missing errors (denoted as a capital "M")')
    print('word selection errors (denoted as a capital "S")')
    print('word ordering errors (denoted as a capital "W")')
    print('Input your sentence, if there are no grammar errors, system will output "correct", else, system will output '
          'the start position、end position and error type of the sentence')
    print('Input "quit" to exit the system')
    print('************************************************************')
    text = input('Please input your sentence:' + '\n')
    while text != 'quit':
        g = open('./CRF_Input.txt', 'w', encoding='utf-8')  # You can change this variable to your own path
        process(text)
        g.close()
        print('Loading model...')
        os.system('crf_test -m model CRF_Input.txt>CRF_Output.txt')
        f = open('./CRF_Output.txt', 'r', encoding='utf-8')  # You can change this variable to your own path
        pos = 0
        correct = 'yes'
        errortype = []
        position = []
        for line in f:
            if line != '\n':
                pos = pos + 1
                newline = line.strip('\n')
                if newline[-1] != 'O':
                    correct = 'no'
                    position.append(pos)
                    errortype.append(newline[-1])
        f.close()
        if correct == 'yes':
            print('Correct')
        else:
            # print('Error Information:')
            for i in range(len(errortype)):
                print(str(position[i]) + ',' + str(position[i]) + ',' + errortype[i])
        text = input('Please input your sentence:' + '\n')
    sys.exit()
