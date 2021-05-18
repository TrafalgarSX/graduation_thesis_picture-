'''
Author: guo yawen
Date: 2021-05-17 23:14:55
LastEditTime: 2021-05-17 23:23:28
LastEditors: guo yawen
Description: 最后一百万的搜索延迟的柱状图
FilePath: \Thesis\lastSearchLatency.py
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
# 统计数据
path_heigth = [1.091, 1.192, 1.208]
cached_heigth = [0.913, 0.997, 1.017]

bar_width = 0.3
index_path = np.arange(len(data_set)) # path条形图的横坐标
index_cached = index_path + bar_width + 0.05 # cached 条形图横坐标

plt.bar(index_path, path_heigth, width= bar_width, color = 'slategrey', label = 'path')
plt.bar(index_cached, cached_heigth, width= bar_width, color = 'c', label = 'CEPH')


# 显示横纵坐标相关
plt.legend(loc= 0, ncol = 2, bbox_to_anchor=(0.7, 1.17)) # 显示图例
plt.xticks(index_path + (bar_width + 0.05)/ 2 , data_set) #让横坐标刻度显示data_set

# y_major_locator=MultipleLocator(0.1)
# plt.gca().yaxis.set_major_locator(y_major_locator)
plt.ylabel('搜索延迟(us)', fontsize=12)
plt.grid(axis='y', alpha=0.5)

plt.title('path和CEPH在LF=0.6下的搜索延迟(后100万数据)')

plt.savefig('./picture/lastSearchLatency0.6.jpg')
plt.show()



