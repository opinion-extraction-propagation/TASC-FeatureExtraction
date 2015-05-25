# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1
# 计算情感一致性方差

import numpy as np
import string

def sortfilebyauthorname(authorfilename,sentimentfile):
    '''
    根据作者姓名文件和情感标记文件，每行对应形成一个字符串，中间以\t间隔
    将字符串列表进行排序，得到以作者名排序的列表
    :param authorfilename: 作者姓名文件
    :param sentimentfile:   tweet label文件
    :return 返回已排序的作者名+标记 列表
    '''
    authorfilereader = open(authorfilename,'r')
    sentimentfilereader = open(sentimentfile,'r')
    listauthornamesentiment = []
    for authorname in authorfilereader:
        authorname = authorname.strip()
        sentimentlabel = sentimentfilereader.readline().strip()
        authorsentiment = authorname+"\t"+sentimentlabel
        listauthornamesentiment.append(authorsentiment)
    listauthornamesentiment.sort()
    authorfilereader.close()
    sentimentfilereader.close()
    return listauthornamesentiment

if __name__ == "__main__":
    # 输入：
    authornamefile = "../newAllAscTweetsOut/author.name"
    sentimentfile = "../newAllAscTweetsOut/label"
    # 输出：
    ConsistentResultfile = "../newAllAscTweetsOut/Preprocess/SentimentConsistent"
    authorSenConsiswriter = open(ConsistentResultfile,'w')
    listauthornamesentiment = sortfilebyauthorname(authornamefile,sentimentfile)


    numauthor=0  # 作者总数量
    numauthortweeteg2=0 # 发的tweet数量大于2个的作者数量
    firstauthor=""; # 遍历的过程中出现的第一个不同的作者
    allauthormeansentimentlist=[];  # 列表：存放了针对所有作者，计算每个作者情感的方差值，用于情感方差的均值计算
    sameauthorsentimentlist=[]; # 列表：存放相同作者的情感标记，也就是每个作者发表tweet的情感列表

    numberauthorpositiveeg2=0;  # 度大于2的tweet中情感为正的个数
    numberauthorneutraleg2=0;
    numberauthornegativeeg2=0;
    for authornamelabel in listauthornamesentiment:
        author = authornamelabel.split("\t")[0]
        sentiment = authornamelabel.split("\t")[1]
        #author=author.strip("\n")
        #sentiment = sentimentreader.readline();
        #sentiment=sentiment.strip("\n")
        sentiment=string.atoi(sentiment)
        if firstauthor=="":
            numauthor=numauthor+1;
            sameauthorsentimentlist.append(sentiment)
            firstauthor=author;
        else:
            if author == firstauthor:
                sameauthorsentimentlist.append(sentiment)
            else:
                #print sameauthorsentimentlist
                numauthor=numauthor+1;
                x=np.var(sameauthorsentimentlist)

                #print x
                if len(sameauthorsentimentlist) >1:
                    for sentimentinlist in sameauthorsentimentlist:
                        if sentimentinlist == 0:
                           numberauthorneutraleg2=numberauthorneutraleg2+1;
                        elif sentimentinlist == 1:
                            numberauthorpositiveeg2=numberauthorpositiveeg2+1;
                        elif sentimentinlist == -1:
                            numberauthornegativeeg2=numberauthornegativeeg2+1;
                    numauthortweeteg2=numauthortweeteg2+1
                    allauthormeansentimentlist.append(x)
                firstauthor=author;
                sameauthorsentimentlist=[sentiment]

    allmean=np.mean(allauthormeansentimentlist)
    authorSenConsiswriter.write("所有作者的情感方差的均值为："+str(allmean)+'\n')
    authorSenConsiswriter.write("作者数量（distinct）："+str(numauthor)+"\n")
    authorSenConsiswriter.write("发表tweet数量大于等于2条的作者数："+str(numauthortweeteg2)+"\n")
    authorSenConsiswriter.write("度大于2的tweet中情感为正的个数:"+str(numberauthorpositiveeg2)+"\n")
    authorSenConsiswriter.write("度大于2的tweet中情感为中的个数:"+str(numberauthorneutraleg2)+"\n")
    authorSenConsiswriter.write("度大于2的tweet中情感为负的个数:"+str(numberauthornegativeeg2)+"\n")
    authorSenConsiswriter.flush()
    authorSenConsiswriter.close()
    print u"方差:"
    print allmean
    print u"不同作者数："
    print numauthor
    print u"tweet数>2的作者数："
    print numauthortweeteg2;
    print u"度大于2的tweet中情感为正的个数："
    print numberauthorpositiveeg2
    print u"度大于2的tweet中情感为中的个数："
    print numberauthorneutraleg2
    print u"度大于2的tweet中情感为负的个数："
    print numberauthornegativeeg2
 
