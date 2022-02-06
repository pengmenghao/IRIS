# IRIS
文件结构说明：
一、function文件夹为各功能函数实现
config.py 配置说明
contrast.py  目标图像与特征数据库比对函数
feature.py 提取特征函数
innerCircle 内圆检测函数
outerCircle 外圆检测函数
Visualization 可视化函数

二、photo 虹膜数据集 左右眼分开
三、feature 提取的所有虹膜的特征数据集
四、CASIA-Iris-Interval 备用数据库 暂时不用


使用说明：
IOCircle.py  完成第一步：内外圆检测 并可视化
Normalize.PY  完成第二步：规范化虹膜区域
FeatureMap.py 完成第三步：提取特征
ALL Feature.PY 完成第四步：提取虹膜数据集中所有虹膜的特征 并保存到 feature文件中
Contrast.py 完成第五步：提取将要对比的图片的特征 并与特征数据库中文件进行比对 输出最理想的结果（loss越小，结果越好）
