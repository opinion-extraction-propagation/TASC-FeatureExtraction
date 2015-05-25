# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1

"""
    查看当前tweet的情感以及该tweet所@得作者发的tweet的情感
    为了方便查看当前tweet的情感以及与该tweet相关联的tweet的情感
"""


import string

if __name__ == "__main__":
    topicnameSet = {"DamnItsTrue","BieberD3D","Egypt","Ff",
                    "MentionKe","NEVERSAYNEVER3D",
                    "TeamFollowBack","Twitition",
                    "cumanNANYA","fb","februarywish",
                    "icantdateyou","improudtosay",
                    "jfb","nowplaying","nw",
                    "pickone","purpleglasses","shoutout","superbowl"}
    for topicname in topicnameSet:
        print topicname
        # 输入：
        # sentimentfile = "../all_asc_tweetsOutput/filterData/HumanLabel/mergedSentiment"
        sentimentfile = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Divided/sentiment"
        tweetrelationfile = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Preprocess/tweetrelation"
        # 输出
        relationsentimentfile = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Preprocess/relationsentiment"

        tweetidSentiment={}

        tweetNo = 1
        with open(sentimentfile,"r") as sentimentreader:
            for sentiment in sentimentreader:
                sentiment = sentiment.strip()
                tweetidSentiment[tweetNo] = sentiment
                tweetNo = tweetNo +1

        sentimentreader.close()
        relationsentimentwriter = open(relationsentimentfile,"w")
        tweetNo = 1
        with open(tweetrelationfile,"r") as tweetRealtionreader:
            for relationships in tweetRealtionreader:
                relationships = relationships.strip()
                relationshipvec = relationships.split(' ')
                relationsentimentwriter.write(tweetidSentiment[tweetNo]+':\t')
                for relation in relationshipvec:
                    if relation =='':
                        continue
                    relationsentimentwriter.write(tweetidSentiment[int(relation)]+'\t')
                relationsentimentwriter.write('\n')
                tweetNo=tweetNo+1
        relationsentimentwriter.flush()
        relationsentimentwriter.close()
        tweetRealtionreader.close()
