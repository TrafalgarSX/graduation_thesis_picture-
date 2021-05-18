'''
Author: guo yawen
Date: 2021-05-17 23:41:20
LastEditTime: 2021-05-18 00:57:04
LastEditors: guo yawen
Description: 
FilePath: \Thesis\everySpaceFailSearch.py
TrafalgarSX
'''

import matplotlib.pyplot as plt 
import numpy as np
# 两行代码正常显示中文 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_set = ['0.2','0.4','0.6','0.8']
index = np.arange(len(x_set))
cached_line_y = [2.439,2.547,2.759,2.810]


plt.plot(index, cached_line_y, color='black',linestyle='-', linewidth=3, marker='*',markerfacecolor='w',markersize=12, label = "CEPH")

path_line_y = [2.700,2.700,3.342,5.021]

plt.plot(index, path_line_y, color='black',linestyle='-', linewidth=3, marker='o',markerfacecolor='w',markersize=12, label = "path")

plt.ylim(2, 6)
y_major_locator = plt.MultipleLocator(1)
plt.gca().yaxis.set_major_locator(y_major_locator)

plt.xlim(-0.5,3.5)
# x_major_locator = plt.MultipleLocator(0.2)
# plt.gca().xaxis.set_major_locator(x_major_locator)
plt.xticks(index, x_set)

plt.legend(loc = 'upper left')
plt.ylabel('搜索延迟(us)', fontsize=12)
plt.grid(axis='y', alpha=0.5)

plt.title('随着负载率提升的失败搜索延迟')

plt.savefig('./picture/everySpaceFailSearch.jpg')
plt.show()