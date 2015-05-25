# TASC-FeatureExtraction

TASC-FeatureExtraction repository包含针对社会媒体数据集抽取特征的过程<br>

代码包含了两部分，其中一部分描述了从社会媒体数据中提取文本特征以及非文本特征的基本流程，第二部分描述了针对开放社会媒体数据处理的具体处理流程。<br>

##目录结构及文件介绍

###feature extraction for weka version

Dictionary<br>
1）主要包含了两个公共情感词库：hownet和wordnet<br>
2）由PMI-IR计算共现次数，得到的hownetPMI值和wordnetPMI<br>
3）合并两个PMI文件，得到情感词的WORDPMI<br>
4）选择得到公共情感词的PMI文件<br>
由于公共情感词基本不变，所以该目录的结构和文件也无需修改。<br>

>hownet<br>
>hownetPMI<br>
>wordnet<br>
>wordnetPMI<br>
>publicwordPMI<br>
>WORDPMI<br>
>mergeWordnetandhownet.py<br>
	用于将两个情感词库合并，同时去重，得到公共情感词PMI库<br>

input<br>
>sorteddata<br>
    按时间排序，并且有一个格式的源数据<br>
>topicwordPMI<br>
    后续得到的话题相关的情感词PMI-IR值<br>

output<br>

DivideData<br>
    正向表情符号：:),;), :-),^_^,^^,:-),-),:D,;],:],:P,;P,:p,;p,-__-,-_-   <br>
    负向表情符号：:(,:-(,:[    <br>
>divide.py<br>
    用于处理源数据，根据sorteddata得到tweet数据集的各个字段 <br>
    每个字段都分别存入到一个文件中。同时，根据rating得到情感标记   <br>

ProcessingData<br>
>PreprocessandgetFrequency.py<br>
    预处理数据，将分割后的杂乱文本处理得到预处理文本。同时，得到话题中包含的单词以及词频<br>
    输出：precontent，topicword和topicwordfrequency

SentimentDiffusion<br>
>checkposrelation.py<br>
    根据作者文件和文本文件得到tweetrelation  <br>

RelationProcess<br>
>relationsentiment.py<br>
    根据tweetrelation和sentiment文件得到，当前tweet的情感，以及与其有关联的tweet的情感   <br>

StatisticData<br>
    实验前的数据统计<br>
>allusersametweetvar.py<br>
    作者情感一致性检验   <br>
>check@relationsentiment.py<br>
    统计direct和mutual边的情感一致性  <br>
>checkhyperlinkgraph.py<br>
    得到图的基本信息，以及画图用的数据，以一定的格式存储  <br>
>getEachAuthorSentiemnt.py<br>
    统计每个作者所发的tweet中，正，中，负三类情感的数量    <br>

StatisticResult<br>
    统计结果文件，保存统计结果的  <br>
>authorsentimentstat    <br>
>RelationDirectMutualStat    <br>
>SentimentConsistent   <br>
>RelationDirectMutualStat    <br>
>SentimentConsistent   <br>
>alllink.net   <br>
>allinkstr <br>
>graphbasicinfo    <br>
>notsinglelink.net <br>

FeatureProcess<br>
    处理各个特征，得到特征矩阵的文件    <br>
>getRelationAtt.py     <br>
    根据tweetrelation得到relation feature （parent，child）    <br>
>gettopicwordPMI.py    <br>
    根据话题相关的情感词topicwordPMI以及topicword词频，得到非公共情感词库及其PMI  <br>
>MergeToGetFM.py   <br>
    根据各个特征，得到不同的特征矩阵    <br>

Feature<br>
    生成的特征和特征矩阵集  <br>
>attprefix    <br>
>RelationAtt    <br>
>nonpublicwordPMI    <br>
>nonpublicwordfreqge2    <br>
>removednonpublicword    <br>
>FeatureMatrixWithNPW    <br>
>FeatureMatrixWithNPWRelation    <br>

###开放社会媒体数据集处理
封闭的带表情符号数据集合，数量是 1915200    <br>
先以表情符号选择推特数据集，然后统计数据集中的用户已经被@用户，再将该用户发布的推特合并过
来  <br>
封闭数据集：all_asc_tweetsOutput/filterData/EmocCloseData <br>
****

####根据需求过滤数据：


FilterData/fitlerData.py    <br>
    根据需求过滤数据,得到带表情符号的数据，以及通过带表情符号得到封闭数据集    <br>
    输出： <br>
>all_asc_tweetsOutput/filterEmocData 含有表情符号的数据集 1208266条tweets   <br>
>all_asc_tweetsOutput/EmocCloseData 封闭数据集  1915200条tweets    <br>

####HashTag 筛选话题
statHashTag.py     <br>
    输出：
>all_asc_tweetsOutput/HashTagStat HashTag统计信息 <br>
>手工过滤，筛选20个话题 all_asc_tweetsOutput/topicData/   <br>


    话题名称  | 微博数量    |话题名称 | 微博数量
    ------------- | -------------   |   ------------- | -------------
    BieberD3D     | 857 | DamnItsTrue     | 608
    Egypt         | 2148    |   Superbowl         | 2344
    MentionKe     | 3749   |   shoutout   | 2933
    NEVERSAYNEVER3D       | 896 |   icantdateyou          | 667
    TeamFollowBack        | 1495    |   fb        | 820
    Twitition     | 1467    |     februarywish    | 739
    cumanNANYA    | 1425    |  Ff         | 5231
    improudtosay          | 563 |    pickone      | 643
    jfb   | 1560    |   purpleglasses     | 744
    nowplaying    | 5888    |   nw        | 669

####HashTag 人工标注数据
humanLabel.py     <br>
    将EmocCloseData中带表情符号的数据进行正／负标注，然后输出需要人工标注的数据 <br>
>输入:
>>封闭的数据集：all_asc_tweetsOutput/filterData/EmocCloseData  <br>

>输出:    <br>
>>已经按照正负标注好的数据：all_asc_tweetsOutput/filterData/HumanLabel/EmocCloseDataLabel    <br>
>>需要人工标注的数据：all_asc_tweetsOutput/filterData/HumanLabel/humanLabelContent  <br>
>>需要人工标注的数据的位置，tweetId：all_asc_tweetsOutput/filterData/HumanLabel/humanLabelNumber    <br>

进行人工标注数据：   <br>
>输出：
>>all中对百万级数据的中对百万级数据的_asc_tweetsOutput/filterData/HumanLabel/humanLabel500    <br>


mergeHumanLabel.py     <br>
合并人工标注的数据HumanLabel/humanLabel500 和 通过表情符号标注的数据HumanLabel/EmocCloseDataLabel    <br>
>输入：   <br>
>>已正负标注好的数据：all_asc_tweetsOutput/filterData/HumanLabel/EmocCloseDataLabel   <br>
>>人工标注的数据：all_asc_tweetsOutput/filterData/HumanLabel/humanLabel500    <br>
>>人工标注数据对应的位置：all_asc_tweetsOutput/filterData/HumanLabel/humanLabelNumber <br>

>输出：
>>合并的数据标注：all_asc_tweetsOutput/filterData/HumanLabel/mergedLabel    <br>
>>合并的数据标注情感：all_asc_tweetsOutput/filterData/HumanLabel/mergedSentiment   <br>

>统计 mergeLabel中正类／负类的数据量比例   <br>

        情感倾向  | 微博数量
        ------------- | -------------
        正类      | 994822
        负类      | 119763
        标注的中性数据    | 100

>注意类别标注： <br>
   
        类别  | 类别标注
        ------------- | -------------
        positive          | 1
        neutral   | 0
        negative          | －1
        unknown   | 2
   
   
#### 处理混合数据
divide.py     <br>
    删除掉输出的sentiment 和 label, 因为已经之前有标注好的    <br>
>ProcessingData/PreprocessandgetFrequency.py:    <br>
>SentimentDiffusion/checkposrelation.py: <br>
>RelationProcess/relationsentiment.py:   <br>
>StatisticData/allusersametweetvar.py   <br>
>StatisticData/check@relationsentiment.py <br>
>StatisticData/checkhyperlinkgraph.py   <br>
>StatisticData/getEachAuthorSentiemnt.py     <br>
>FeatureProcess/getRelationAtt.py : 根据tweetrelation得到relation feature （parent，child）    <br>

#### 处理某个话题领域的话题相关情感词
allTweetsPreprocess/divide.py  <br>
ProcessingData/PreprocessandgetFrequency.py  <br>
SentimentDiffusion/checkposrelation.py  <br>
RelationProcess/relationsentiment.py  <br>
FeatureProces/getRelationAtt.py  <br>
