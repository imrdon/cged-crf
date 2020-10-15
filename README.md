# Chinese Grammar Error Diagnosis Based on Conditional Random Field

![Language Python](https://img.shields.io/badge/Language-Python-red)
[![License MIT](https://img.shields.io/github/license/imrdong/cged-crf.svg?label=License&color=blue)](https://github.com/imrdong/cged-crf/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/imrdong/cged-crf.svg?style=social&label=Star&maxAge=10)](https://github.com/imrdong/cged-crf/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/imrdong/cged-crf?style=social&label=Fork&maxAge=10)](https://github.com/imrdong/cged-crf/network/members/)

# Background

The purpose of the Chinese grammar error diagnosis task is to develop a system that can detect four types of grammar errors in the learner's corpus. The types of errors in the data set sentences are defined as follows: redundant words (R), missing words (M), word selection errors (S), word ordering errors (W). The system should be able to identify the type of error and the corresponding error location included in the sentence. If the sentence does not contain any grammar errors, it should output correct. The system finally achieve the automatic diagnosis of Chinese grammar errors based on CRF algorithm.

# Install

## PyLTP

PyLTP is used to achieve word segmentation, part-of-speech tagging, dependency parsing, semantic role labeling and semantic dependency parsing of the text.

## CRF++ Toolkit

The Windows version is crf++0.58.

# Dataset

Download the compressed package named nlptea16cged_release1.0.zip from the official website.

## Training Set

All sentences in the Training dataset are used to train the Chinese grammar error diagnosis system. The grammar error comments and corresponding corrections in each sentence are represpented in SGML format, and the sentence may contain one or more errors.

## Test Set

The test set and the training set are in the same format, but there are no corresponding error types and error locations, only sentence instances.

## Jar Package

Jar package used to evaluate model performance.

# Training

In this system, we decided to solve the diagnosis of Chinese grammar errors at the level of character set. First, we extracted the sentence instance in the training set, and then preprocessed the sentence instance according to the feature project we analyzed, then generate data in the format of CRF++ input requirements. Then, we implemented the in-depth expansion of features according to the feature template we designed, finally, training through CMD command to get the final model.

# Test 

The test set is preprocessed in the same way as the training set, and then tested by the trained model. If the current statement does not contain any grammar errors, the model will output "Correct"; otherwise, the error location and corresponding error type will be output.

# Performance Evaluation

The performance evaluation of this system is evaluated from three levels: detection level, Identification level and position level. All performance metrics are measured at all levels with the help of confusion matrix.

# Chinese Grammar Error Diagnosis System

Based on all of the above, we built a grammar error diagnosis system based on the current model, which can achieve automatic detection of Chinese grammar errors.

# Statement

The code is for communication and learning only.