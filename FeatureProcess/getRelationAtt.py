# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1


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
        # sentimentfilename = "../all_asc_tweetsOutput/filterData/HumanLabel/mergedSentiment"
        sentimentfilename = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Divided/sentiment"
        tweetrelationfilename = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Preprocess/tweetrelation"
        # 输出：
        relationattributefilename = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Feature/RelationAtt"
        DicTweetNoSentiment={}

        tweetNo = 1
        with open(sentimentfilename,"r") as sentimentreader:
            for sentiment in sentimentreader:
                sentiment = sentiment.strip()
                DicTweetNoSentiment[tweetNo] = sentiment
                tweetNo = tweetNo +1
        sentimentreader.close()
        RelationAttwriter = open(relationattributefilename,"w")

        tweetNo = 1
        with open(tweetrelationfilename,"r") as tweetRealtionreader:
            for relations in tweetRealtionreader:
                 relationarr = relations.strip().split()
                 parentlist = [tweetnumber for tweetnumber in relationarr if int(tweetnumber) < tweetNo]
                 childrenlist = [tweetnumber for tweetnumber in relationarr if int(tweetnumber) > tweetNo]

                 '''计算parent和children 属性值'''
                 parentAtt=0
                 for tweetnumber in parentlist:
                     if DicTweetNoSentiment[int(tweetnumber)]=="positive":
                        parentAtt = parentAtt+1
                     elif DicTweetNoSentiment[int(tweetnumber)]=="negative":
                         parentAtt = parentAtt-1

                 childrenAtt=0
                 for tweetnumber in childrenlist:
                     if DicTweetNoSentiment[int(tweetnumber)]=="positive":
                         childrenAtt = childrenAtt+1
                     elif DicTweetNoSentiment[int(tweetnumber)]=="negative":
                         childrenAtt = childrenAtt-1

                 print parentAtt,childrenAtt
                 tweetNo = tweetNo+1
                 RelationAttwriter.write(str(parentAtt)+" "+str(childrenAtt)+"\n")
        tweetRealtionreader.close()

        RelationAttwriter.flush()
        RelationAttwriter.close()