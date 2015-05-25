# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1

'''
    读取公共情感词publicwordPMI ，然后读取topicPMI，将重复的去掉，按照降序输出到nonpublicwordPMI
'''


if __name__  == "__main__":
    # 输入：
    publicwordpmifilename = "../Dictionary/publicwordPMI"
    topicwordfreqfilename = "../all_asc_tweetsOutput/Preprocess/topicwordfrequency"
    topicwordpmifilename = "../Input/topicwordPMI"

    # 输出：
    nonpublicwordpmifilename = "../all_asc_tweetsOutput/Feature/nonpublicwordPMI"
    nonpublicwordfreqge2filename = "../all_asc_tweetsOutput/Feature/nonpublicwordfreqge2"
    removedpublicwordfilename = "../all_asc_tweetsOutput/Feature/removednonpublicword"

    publicwordDic={}
    nonpublicwordDic={}
    nonpublicwordfrequency={}

    removedpublicword = open(removedpublicwordfilename,"w")
    nonpublicwordwriter = open(nonpublicwordpmifilename,"w")
    nonpublicwordfreqge2writer = open(nonpublicwordfreqge2filename,"w")

    with open(publicwordpmifilename,"r") as publicwordreader:
        for publicwordvalue in publicwordreader:
            wordvalue = publicwordvalue.strip().split("\t")
            publicwordDic[wordvalue[0]] = wordvalue[1]
    publicwordreader.close()

    with open (topicwordpmifilename,"r") as topicwordreader:
        for topicwordvalue in topicwordreader:
            wordvalue = topicwordvalue.strip().split("\t")
            if not publicwordDic.has_key(wordvalue[0]):
                nonpublicwordDic[wordvalue[0]] = wordvalue[1]
            else:
                removedpublicword.write(topicwordvalue)
    topicwordreader.close()



    with open(topicwordfreqfilename,"r") as topicwordfrequencyreader:
        for topicwordfreq in topicwordfrequencyreader:
            wordfreq = topicwordfreq.strip().split("\t")
            if wordfreq.__len__()==2 and wordfreq[0] !="" and wordfreq[1]!="":
                nonpublicwordfrequency[wordfreq[0]] = wordfreq[1]
    topicwordfrequencyreader.close()

    nonpublicwordlist = sorted(nonpublicwordDic.items(),lambda x,y: cmp(x[1],y[1]),reverse=True)


    for key,value in nonpublicwordlist:
        if nonpublicwordfrequency.has_key(key):
            nonpublicwordwriter.write(key+"\t"+value+"\t"+nonpublicwordfrequency[key]+"\n")
            if nonpublicwordfrequency[key]>"2":
                nonpublicwordfreqge2writer.write(key+"\t"+value+"\t"+nonpublicwordfrequency[key]+"\n")


        else:
            removedpublicword.write(key+"\t"+value+"\n")


    nonpublicwordfreqge2writer.flush(),nonpublicwordfreqge2writer.close()

    nonpublicwordwriter.flush(),nonpublicwordwriter.close()
    removedpublicword.flush(),removedpublicword.close()


