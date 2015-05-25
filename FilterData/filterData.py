# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2015-01-07
# version: 0.1
__author__ = 'lifuxin'


'''
    根据需求过滤数据
'''

positiveEmoc = {":)",";)",":-)","^_^","^^",":-)","-)",":D",";]",":]",":P",";P",":p",";p","-__-","-_-"}
negativeEmoc ={":(",":-(",":["}
authorSet=set()

def addAuthor(content):
    '''
    将content中包含的@author 中的author加入到authorSet中
    :param content
    '''
    if len(content)!=0:
        startpos=content.find('@')
        while startpos!=-1:
            endpos=content.find(' ',startpos)
            if endpos!=-1:
                atauthorname=content[startpos+1:endpos]
                content=content[endpos:len(content)]
            else:
                atauthorname=content[startpos+1:len(content)]

            authorSet.add(atauthorname)

            if endpos==-1:
                break
            else:
                startpos=content.find('@')

if __name__ == "__main__":
    inputDataFile = "../../../data/SourceData/all_asc_tweets.txt"
    outputDataFile = "../all_asc_tweetsOutput/filterData/EmocCloseData"



    try:
        global tweetsFileReader,filterDataWriter
        tweetsFileReader = open(inputDataFile,'r')
        filterDataWriter=open(outputDataFile,'w')
    except IOError,e:
        print ("读取源数据出现错误",e)
    else:

        for readLine in tweetsFileReader:
            lineAdd = 0

            readLineArray = readLine.strip('\n').split('\t')
            author = readLineArray[1]
            content = readLineArray[4]

            for emoc in positiveEmoc:
                if emoc in content:
                    lineAdd = 1
                    addAuthor(content)
                    filterDataWriter.write(readLine)
                    break
            if lineAdd == 1:
                continue
            for emoc in negativeEmoc:
                if emoc in content:
                    lineAdd = 1
                    addAuthor(content)
                    filterDataWriter.write(readLine)
                    break
            if lineAdd == 1:
                continue

            if author in authorSet:
                filterDataWriter.write(readLine)


        tweetsFileReader.close()
        filterDataWriter.flush(),filterDataWriter.close()