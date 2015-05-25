# encoding=utf-8
# author : lifuxin1125@gmail.com
# date: 2014-06-20
# version: 0.1


"""
    通过content，author.name，author.nickname三个文件得到tweet之间的relation关系文件
    输入：
        content，author.name，author.nickname
    输出：
        tweetrelation
"""


def listwrite2file(tweetrelationfilewriter,authorname2tweetNos):
    '''
    将列表元素写入到文件里
    :param tweetrelationfilewriter: 待写入的文件
    :param authorname2tweetNos: 作者相应的tweet列表
    '''
    for content in authorname2tweetNos:
        tweetrelationfilewriter.write(str(content))
        tweetrelationfilewriter.write(str(" "))
                     
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
        authornamefilename = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Divided/author.name"
        contentfilename = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Divided/content"
        # 输出：
        tweetrelationfilename = "../newAllAscTweetsOut/SpecialDomain/"+topicname+"/Preprocess/tweetrelation"

        authorset=set() #发状态的作者集合，set去掉重复名字
        authornicknameset=set()
        nickname2authorname={}  #nickname到authorname的映射
        authorname2tweetNo={}   #作者名字到作者发布的tweet号的映射,注意map的value是个list，也就是tweet集合

        try:
            #authorname每个tweet的作者列表（有重复）
            authornamefilereader = open(authornamefilename,'r')
        except IOError,e:
            print ("***  file open error:",e)
        else:
            # 遍历作者名字文件，将作者的名字存入到作者集合中（去掉重复作者），同时，记录每个作者发布的tweet状态号
            tweetNo=1
            for authorname in authornamefilereader:
                authorname = authorname.strip('\n')
                '''
                #   如果当前作者不存在于作者集中，那么就将作者添加到作者集，并且初始化作者到tweetNo的映射
                #   否则，说明作者之前已经添加过，直接将作者发布的tweetNo添加到之前添加的tweetNo集中
               '''
                if authorname not in authorset:
                    authorset.add(authorname)
                    authorname2tweetNo[authorname]=[tweetNo]
                else:
                    authorname2tweetNo[authorname].append(tweetNo)
                tweetNo=tweetNo+1
            authornamefilereader.close()

        '''
            #   得到的结构体：
            #   authorset authornicknameset 作者集合
            #   nickname2authorname  nickname到authorname的映射
            #   authorname2tweetNo  作者名字到tweet号的映射

            #   遍历每一条tweet content，查询content中的@符号，发现@的作者s
            #   然后通过字典集authorname2tweetNo 查询该作者发的tweets，记录到文件中
        '''

        try:
            contentfilereader = open(contentfilename,'r')
            tweetrelationfilewriter = open(tweetrelationfilename,'w')
        except IOError,e:
            print ("*** contentfilereader file open error:",e)
        else:
            tweetNo=1
            for content in contentfilereader:
                content = content.strip('\n')
                tweetNo = tweetNo +1
                if len(content)!=0:
                     startpos=content.find('@')
                     while startpos!=-1:
                        endpos=content.find(' ',startpos)
                        if endpos!=-1:
                             atauthorname=content[startpos+1:endpos]
                             content=content[endpos:len(content)]
                        else:
                             atauthorname=content[startpos+1:len(content)]
                        # 将该作者发布的tweetNo输出到文件中
                        if atauthorname in authorset:
                            listwrite2file(tweetrelationfilewriter,authorname2tweetNo[atauthorname])
                        elif atauthorname in authornicknameset:
                            listwrite2file(tweetrelationfilewriter,authorname2tweetNo[authornicknameset[atauthorname]])
                        if endpos==-1:
                             break
                        else:
                            startpos=content.find('@')
                tweetrelationfilewriter.write('\n')
            contentfilereader.close()

            tweetrelationfilewriter.flush()
            tweetrelationfilewriter.close()


                

