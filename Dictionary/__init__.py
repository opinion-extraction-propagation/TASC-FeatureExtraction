# -*- coding: cp936 -*-
__author__ = 'lifuxin'


'''
情感词典：
    1.从WordNet Affect上搜集的六类情感词库：anger disgust fear joy sadness surprise，处理合并为wordnet.txt.共1536个词语
    2.从HowNet情感词库里面取出四类词语：  正、负面情感词   正、负面评价词,处理合并为hownet.txt.共5367个词语
    3.用统计方法找到话题相关的、可能表达情感的词语,存入文件topicwords.txt
    通常wordnet和hownet是固定的，但是话题相关的词语就需要统计，话题不同，处理自然就不同）

情感词典对应的PMI-IR值,主要是计算单词分别与“excellent”和“poor”的共现次数，然后通过公式计算得到PMI-IR值
    1.wordnetPMI
    2.hownetPMI
    该计算是在google提供的搜索接口计算得到的，一般该值不会改变，所以这两个词库的PMI-IR值可以保持不变。
'''