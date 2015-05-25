# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1
"""
该脚本的作用：
    读取hownet和wordnet两个情感词库的PMI文本，然后合并得到非公共情感词特征
    注意：1.一般hownet和wordnet两个词库不变，同时PMI-IR值也不变，所以该脚本生成的非公共情感词的PMI值也不变
          2.对hownet和wordnet中的情感词做了去重
"""
import string

if __name__ == "__main__":
    # 输入文件名称：
    hownetpmifile = "../Dictionary/hownetPMI"
    wordnetpmifile = "../Dictionary/wordnetPMI"
    # 输出文件名称：
    nonpublicwordfile = "../Output/nonpublicwordPMI"
    worddic={} # 情感词对应的PMI-IR值词典映射表
    with open(hownetpmifile,"r") as hownetreader:
        for hownetwordvalue in hownetreader:
            wordvaluearr=hownetwordvalue.strip().split("\t")
            worddic[wordvaluearr[0]]=wordvaluearr[1]
    hownetreader.close()

    with open(wordnetpmifile,"r") as wordnetreader:
        for wordnetwordvalue in wordnetreader:
            wordvaluearr = wordnetwordvalue.strip().split("\t")
            if wordvaluearr[0] not in worddic  or  wordvaluearr[1] > worddic[wordvaluearr[0]]:
                worddic[wordvaluearr[0]] = wordvaluearr[1]
    wordnetreader.close()

    # 按照情感词对应的PMI-IR值的大小降序排列
    worddiclist=sorted(worddic.items(),lambda x,y:cmp(x[1],y[1]),reverse=True)
    #worddiclist=sorted(worddic.items(),lambda x,y:abs(float(x[1]))>abs(float(y[1])),reverse=True)
    nonpublicwordPMIwriter = open(nonpublicwordfile,"w")
    for key,value in worddiclist:
        nonpublicwordPMIwriter.write(key+"\t"+value+"\n")
    nonpublicwordPMIwriter.flush()
    nonpublicwordPMIwriter.close()
