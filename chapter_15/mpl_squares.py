import matplotlib.pyplot as plt
import matplotlib
# from matplotlib.font_manager import _rebuild

# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 有中文出现的情况，需要u'内容'

# _rebuild()

matplotlib.rcParams['font.family'] = 'SimHei'

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth=5)
plt.title('事例', fontsize=21)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
