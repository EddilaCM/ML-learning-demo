## 基于协同过滤的推荐（社会化过滤算法）
### 基于用户的协同过滤
####   相似度计算
1. 闵可夫斯基计算公式
```python
def minkowski(rating1, rating2, r):
    """
    compute minkowski distance
    :param rating1: 
    :param rating2: 
    :param r: 
    :return: 
    """
    distance = 0
    for key in rating1.keys():
        if key in rating2.keys():
            distance += pow(abs(rating1[key] - rating2[key]), r)
    return distance
```
- r = 1时为曼哈顿相似度计算公式
- r = 2时为欧几里得距离相似度计算公式
```
注意： 用0值代替空缺值的方法对结果会有很大影响，平均值填充是一种变通的方法。
总之，在数据比较完整的情况下，曼哈顿和欧几里得计算效果会更好
```

2. 皮尔逊相似度计算公式
    
   > 问题：不同用户的评分标准不一致，闵可夫斯基计算无法刻画，即"分数膨胀"，如A非常喜欢电影评分为4分，B觉得还不错，没有特别喜欢评分为4分。
   
   > 皮尔逊相关系数用于刻画两个变量之间的相关性，取值范围[-1, 1]。 1 表示完全吻合，-1 表示完全相悖

- 计算公式：
![add9f0293ac10c2b56f31dad4f9c02b8.png](evernotecid://0145E6F0-23BE-4011-84F6-77CBA6A90B4A/appyinxiangcom/19312996/ENResource/p120)
- 相似计算公式（原式需要对数据作多次遍历，近似值公式只需遍历一次数据）
![1912bfb958b56a60c36e7cbe60638caf.png](evernotecid://0145E6F0-23BE-4011-84F6-77CBA6A90B4A/appyinxiangcom/19312996/ENResource/p121)

3. 余弦相似度
    > 数据比较稀疏的情况使用，余弦相似度的计算会略过非零值
    ![a767687b97b2592ab8032a4171425b7c.png](evernotecid://0145E6F0-23BE-4011-84F6-77CBA6A90B4A/appyinxiangcom/19312996/ENResource/p122)


#### 小结
1. 如何数据存在"分数膨胀"问题，就使用皮尔逊相关系数
2. 如果数据比较密集，变量之间基本存在公有值，且这些距离数据是非常重要的，那就使用闵可夫斯基距离计算
3. 如果数据稀疏，则使用余弦相似度



#### K近邻算法
> 单纯的依赖某一个用户做推荐，如果这个用户有特殊偏好，就会直接反映在推荐内容中，故可以找到多个相似的用户，即KNN

> **计算用户评分**

### 基于物品的协同过滤
   > 评价： 隐式评价（基于用户行为获得的偏好信息）、显示评价（具体的评分数据）
   > 隐式评价：页面的点击、停留时间、重复访问次数、引用频率， 音乐播放器：播放的曲目，跳过的曲目、播放的次数
   
   > 基于用户的协同过滤又称为内存型的协同过滤，我们需要将所有的评价数据都保留在内存中进行推荐
   > 基于物品的协同过滤也称为基于模型的协同过滤，因为我们不需要保存所有的评价数据，而是通过构建一个物品相似度模型来做推荐
   - 修正的余弦相似度（也是解决"分数膨胀"问题的一种方法）
   > 计算两个物品的距离----从用户评分中减去他所有评价的均值，这就是修正的余弦相似度
   ![6c9b62b337155d62f58e92daac53e737.png](evernotecid://0145E6F0-23BE-4011-84F6-77CBA6A90B4A/appyinxiangcom/19312996/ENResource/p123)

#### slopeOne算法（一种比较流行的基于物品的协同过滤算法）
- 核心思想：通过用户评价过的物品，比较物品两两间的评分差值，预测评分，进行推荐


#### 协同过滤的缺点：
1. 数据的稀疏性和算法的可扩展性
2. 协同过滤倾向于推荐已经很流行的物品


## 基于分类的推荐
 #### 近邻分类器
修正的标准分：取中位数，计算绝对偏差 

公式= （X-中位数）/ 绝对偏差
```python
def getMedian(self, alist):
    """返回中位数"""
    if alist == []:
        return []
    blist = sorted(alist)
    length = len(alist)
    if length % 2 == 1:
        # 列表有奇数个元素，返回中间的元素
        return blist[int(((length + 1) / 2) - 1)]
    else:
        # 列表有偶数个元素，返回中间两个元素的均值
        v1 = blist[int(length / 2)]
        v2 = blist[(int(length / 2) - 1)]
    return (v1 + v2) / 2.0
    
    
def getAbsoluteStandardDeviation(self, alist, median):
    """计算绝对偏差"""
    sum = 0
    for item in alist:
        sum += abs(item - median)
    return sum / len(alist)
```
![2348d65563ad35a1cfcecbf5a4bffe19.png](evernotecid://0145E6F0-23BE-4011-84F6-77CBA6A90B4A/appyinxiangcom/19312996/ENResource/p124)

Kappa指标评价（经验）：

![7fa5139b3d390e4e14047795de667258.png](evernotecid://0145E6F0-23BE-4011-84F6-77CBA6A90B4A/appyinxiangcom/19312996/ENResource/p125)


