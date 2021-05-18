'''
 论文空间利用率柱状图
'''
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
# 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 横坐标集合名称
data_set = ['RandomNum', 'DocWord', 'Fingerprint']
# 统计数据
path_heigth = [0.9428, 0.951, 0.9427]
cached_heigth = [0.917281, 0.91, 0.917176]
cached_heigthL3 = [0.956113, 0.95075, 0.950517]

bar_width = 0.2
index_path = np.arange(len(data_set)) # path条形图的横坐标
index_cached = index_path + bar_width + 0.05 # cached 条形图横坐标
index_cachedL3 = index_cached + bar_width + 0.05 # cached 条形图横坐标

# 画图
plt.bar(index_path, path_heigth,  width = bar_width, color = 'slategrey', label = 'path')
plt.bar(index_cached, cached_heigth, width = bar_width, color = 'c', label = 'CEPH')
plt.bar(index_cachedL3, cached_heigthL3, width = bar_width, color = 'lightsteelblue', label = 'CEPHL3')

# 显示横纵坐标相关
plt.legend(loc= 0, ncol = 3, bbox_to_anchor=(0.8, 1.17)) # 显示图例
plt.xticks(index_cached  , data_set) #让横坐标刻度显示data_set
plt.ylabel('空间利用率', fontsize=12)
plt.grid(axis='y', alpha=0.5)
plt.title('哈希表的空间利用率')

# 将纵坐标变成百分比形式
def to_percent(temp, position):
    return '%1.0f' % (100*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

plt.savefig('./picture/spaceUtilization.jpg')
plt.show()
