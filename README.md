# TASC-FeatureExtraction

TASC-FeatureExtraction repository包含针对社会媒体数据集抽取特征的过程<br>

代码包含了两部分，其中一部分描述了从社会媒体数据中提取文本特征以及非文本特征的基本流程，第二部分描述了针对开放社会媒体数据处理的具体处理流程。<br>

##目录结构及文件介绍

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
