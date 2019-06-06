from chapter_15.die import Die
import pygal

# 创建一个D6
die = Die()

# 投掷骰子，并将结果存贮在列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.刻度'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
