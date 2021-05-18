'''
Author: guo yawen
Date: 2021-05-18 18:11:36
LastEditTime: 2021-05-18 18:54:17
LastEditors: guo yawen
Description: 
FilePath: \Thesis\cacheLineNum.py
TrafalgarSX
'''
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

# 两行代码正常显示中文 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 横坐标集合名称
data_set = ['RandomNum', 'DocWord', 'Fingerprint']
# cache line data
path_cacheline = [1.913248926,1.912741108,1.91289132]
cached_cacheline = [2.005103,2.005212,2.003143]

bar_width = 0.3
index_path = np.arange(len(data_set)) # path条形图的横坐标
index_cached = index_path + bar_width + 0.05 # cached 条形图横坐标

plt.bar(index_path, path_cacheline, width= bar_width, color = 'slategrey', label = 'path')
plt.bar(index_cached, cached_cacheline, width= bar_width, color = 'c', label = 'CEPH')

# 显示横纵坐标相关
plt.legend(loc= 0, ncol = 2, bbox_to_anchor=(0.7, 1.17)) # 显示图例
plt.xticks(index_path + (bar_width + 0.05)/ 2 , data_set) #让横坐标刻度显示data_set

plt.ylabel('平均写请求数', fontsize=12)
plt.grid(axis='y', alpha=0.5)

plt.title('path和CEPH在LF=0.6下每个请求的平均写入cache 行数')

plt.savefig('./picture/cacheLineNum0.6.jpg')
plt.show()


