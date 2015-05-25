# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1
# 读取作者名字，情感标记两个文件：统计每个作者发的tweet的情感
# 输出格式：作者姓名\t正类情感tweet数\t中类\t负类


if __name__ == "__main__":
    authornamefile = "../Output/author.name"
    sentimentfile = "../Output/sentiment"
    authorsentimentstatfile = "../StatisticResult/authorsentimentstat"

    # 获得每个tweet号到tweet的情感标记映射
    DicTweetNoSentiment={} # 词典：每个tweet的sentiment，tweet号到tweet sentiment label 的映射词典
    tweetNo = 1
    with open(sentimentfile,"r") as sentimentreader:
        for sentiment in sentimentreader:
            sentiment = sentiment.strip()
            DicTweetNoSentiment[tweetNo] = sentiment
            tweetNo = tweetNo +1
    sentimentreader.close()


    authorsentimentstat = open(authorsentimentstatfile,"w")
    tweetNo = 1
    DicAuthor2sentiment={} # 词典，作者名字到作者发的tweet的三类情感标记数 name->list(positive,netural,negative)
    with open(authornamefile,"r") as authornamereader:
        for authorname in authornamereader:
            authorname = authorname.strip()
            if authorname in DicAuthor2sentiment.keys():
                if DicTweetNoSentiment[tweetNo] == "positive":
                    DicAuthor2sentiment[authorname][0]=DicAuthor2sentiment[authorname][0]+1
                elif DicTweetNoSentiment[tweetNo] == "neutral":
                    DicAuthor2sentiment[authorname][1]=DicAuthor2sentiment[authorname][1]+1
                elif DicTweetNoSentiment[tweetNo] == "negative":
                    DicAuthor2sentiment[authorname][2]=DicAuthor2sentiment[authorname][2]+1
            else:
                DicAuthor2sentiment[authorname]=[0,0,0]
                if DicTweetNoSentiment[tweetNo] == "positive":
                    DicAuthor2sentiment[authorname][0]=1
                elif DicTweetNoSentiment[tweetNo] == "neutral":
                    DicAuthor2sentiment[authorname][1]=1
                elif DicTweetNoSentiment[tweetNo] == "negative":
                    DicAuthor2sentiment[authorname][2]=1
            tweetNo=tweetNo+1
    for key in DicAuthor2sentiment.keys():
        authorsentimentstat.write(str(key)+"\t"+str(DicAuthor2sentiment[key][0])+\
                                  "\t"+str(DicAuthor2sentiment[key][1])+"\t"+str(DicAuthor2sentiment[key][2])+"\n")
    authorsentimentstat.flush()
    authorsentimentstat.close()
    authornamereader.close()