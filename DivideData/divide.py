# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1

'''
    # 读取数据，通过tab键分割得到tweetId;pub.date.GMT;content;author.name
    # 输出数据：分割后的内容文件，同时根据rating得到sentiment
    # author.nickname;rating =>sentiment
'''

import time
def write2tweetid(tweetid):
    tweetidFileWriter.write(str(tweetid))
    tweetidFileWriter.write("\n")

def write2pubdate(pubdate):
    pubdatetime=time.strptime(pubdate,"%m/%d/%y %H:%M")
    pubdatefilewriter.write(str(pubdate))
    pubdatefilewriter.write("\n")

    yearfilewriter.write(str(pubdatetime[0]))
    yearfilewriter.write("\n")

    monthfilewriter.write(str(pubdatetime[1]))
    monthfilewriter.write("\n")

    dayfilewriter.write(str(pubdatetime[2]))
    dayfilewriter.write("\n")

    hourfilewriter.write(str(pubdatetime[3]))
    hourfilewriter.write("\n")

    minfilewriter.write(str(pubdatetime[4]))
    minfilewriter.write("\n")


def write2content(content):
    #contentfilewriter.write(str(content).lower())
    contentFileWriter.write(str(content))
    contentFileWriter.write("\n")

def write2authorname(authorname):
    authornameFileWriter.write(str(authorname))
    authornameFileWriter.write("\n")

def write2authornickname(authornickname):
    authornicknamewriter.write(str(authornickname))
    authornicknamewriter.write("\n")

# negative;positive;mixed;other
def countadd(ratings):
    ratings=ratings.strip(" ")
    ratings=ratings.strip("\n")
    ratings=ratings.strip("\t")
    # print ratings
    if ratings=="1":
        sentiment[0]=sentiment[0]+1
    elif ratings=="2":
        sentiment[1]=sentiment[1]+1
    elif ratings=="3" or ratings=="4":
        sentiment[2]=sentiment[2]+1


'''
   定义一个字典映射： position 到 函数的一个映射
'''
positionAction = {
    "1":write2tweetid,
    "2":write2pubdate,
    "3":write2content,
    "4":write2authorname,
    "5":write2authornickname,
    "6":countadd,
    "7":countadd,
    "8":countadd,
    "9":countadd,
    "10":countadd,
    "11":countadd,
    "12":countadd,
    "13":countadd
}
'''
    定义一个label Map映射，情感label字符串到数字label的映射
'''
labelMap = {
    "positive":"1",
    "neutral":"0",
    "negative":"-1"
}
global sentiment
if __name__ == "__main__":
    inputdatafile = "../input/sorteddata"
    outputdir = "../Output/"
    try:
        global tweetsFileReader,tweetidFileWriter,pubdatefilewriter,yearfilewriter
        global monthfilewriter,dayfilewriter,hourfilewriter,minfilewriter
        global contentFileWriter,authornameFileWriter,authornicknamewriter
        global ratingswriter,labelFileWriter
        tweetsFileReader = open(inputdatafile,'r')
        tweetidFileWriter=open(outputdir+'tweet.id','w')
        pubdatefilewriter = open(outputdir+'pub.date.GMT','w')
        yearfilewriter = open(outputdir+'year','w')
        monthfilewriter = open(outputdir+'month','w')
        dayfilewriter = open(outputdir+'day','w')
        hourfilewriter = open(outputdir+'hour','w')
        minfilewriter = open(outputdir+'min','w')
        contentFileWriter = open(outputdir+'content','w')
        authornameFileWriter = open(outputdir+'author.name','w')
        authornicknamewriter = open(outputdir+'author.nickname','w')
        ratingswriter = open(outputdir+'sentiment','w')
        labelFileWriter = open(outputdir+'label','w')
    except IOError,e:
        print ("读取源数据出现错误",e)
    else:
        tweetNo = 1
        for tweetstructure in tweetsFileReader:
            tweets = tweetstructure.split("\t")
            position=1
            # negative positive netural
            sentiment=[0,0,0]
            for temp in tweets:
                positionAction.get(str(position))(temp)
                position = position+1
            label=""
            if sentiment[0]>sentiment[1] and sentiment[0]>sentiment[2]:
                label="negative"
            elif sentiment[0]==sentiment[1] or (sentiment[2]>sentiment[0] and sentiment[2]>sentiment[1]):
                label="neutral"
            else:
                label="positive"

            #ratingswriter.write(str(sentiment[0])+" "+str(sentiment[1])+" "+str(sentiment[2])+" "+str(label))
            ratingswriter.write(str(label))
            ratingswriter.write("\n")

            labelFileWriter.write(labelMap[str(label)]+"\n")
            tweetNo=tweetNo+1


        tweetsFileReader.close()
        tweetidFileWriter.flush(),tweetidFileWriter.close()
        pubdatefilewriter.flush(),pubdatefilewriter.close()
        contentFileWriter.flush(),contentFileWriter.close()
        authornameFileWriter.flush(),authornameFileWriter.close()
        authornicknamewriter.flush(),authornicknamewriter.close()
        ratingswriter.flush(),ratingswriter.close()
        yearfilewriter.flush(),yearfilewriter.close()
        monthfilewriter.flush(),monthfilewriter.close()
        dayfilewriter.flush(),dayfilewriter.close()
        hourfilewriter.flush(),hourfilewriter.close()
        minfilewriter.flush(),minfilewriter.close()
        labelFileWriter.flush(),labelFileWriter.close()
    
