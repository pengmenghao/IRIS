"""
 作者：pengmenghao
 日期：2021年7月13日
 """
from function.feature import generateFeatureDataset

dp = r'./photo'
fdp = r'./feature'

generateFeatureDataset(feature_dataset_path=fdp, dataset_path=dp, mode='swt')
print('已完成')