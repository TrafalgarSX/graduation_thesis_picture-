import matplotlib.pyplot as plt
import numpy as np
# path and cached 0.6factor

# 两行代码正常显示中文 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 横坐标集合名称
data_set = ['RandomNum', 'DocWord', 'Fingerprint']
# 统计数据
path_heigth = [0.707, 0.766, 0.786]
cached_heigth = [0.636, 0.697, 0.721]

bar_width = 0.3
index_path = np.arange(len(data_set)) # path条形图的横坐标
index_cached = index_path + bar_width + 0.05 # cached 条形图横坐标

plt.bar(index_path, path_heigth, width= bar_width, color = 'slategrey', label = 'path')
plt.bar(index_cached, cached_heigth, width= bar_width, color = 'c', label = 'CEPH')


# 显示横纵坐标相关
plt.legend(loc= 0, ncol = 2, bbox_to_anchor=(0.7, 1.17)) # 显示图例
plt.xticks(index_path + (bar_width + 0.05)/ 2 , data_set) #让横坐标刻度显示data_set
plt.ylabel('插入延迟(us)', fontsize=12)
plt.grid(axis='y', alpha=0.5)
plt.title('path和CEPH在LF=0.6下的插入延迟')

plt.savefig('./picture/insertLatency0.6.jpg')
plt.show()
