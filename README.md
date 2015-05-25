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





