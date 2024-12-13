#import pygal

#line_chart = pygal.Line()
#line_chart.title='Statistika'
#line_chart.x_labels=['Fevral','Mart','Aprel','May']
#line_chart.add('Facebook',[9.24,13.7,16.24,18.07])
#line_chart.add('Instagram',[24.03,26.81,21.03,22.77])
#line_chart.add('YouTube',[8.95,15.81,19,19,22.67])
#line_chart.render_in_browser()


import pygal

# 1-Ijtimoiy tarmoq
tarmoq1 = input('1-Ijtimoiy tarmoq nomini kiriting: ')
a = list(map(input(tarmoq1 + ' ning 3 ta qiymatini kiriting: ').strip().split()))[:3]

# 2-Ijtimoiy tarmoq
tarmoq2 = input('2-Ijtimoiy tarmoq nomini kiriting: ')
b = list(map(input(tarmoq2 + ' ning 3 ta qiymatini kiriting: ').strip().split()))[:3]

# 3-Ijtimoiy tarmoq
tarmoq3 = input('3-Ijtimoiy tarmoq nomini kiriting: ')
c = list(map(input(tarmoq3 + ' ning 3 ta qiymatini kiriting: ').strip().split()))[:3]

# Pygal diagrammasi yaratish
line_chart = pygal.Line()
line_chart.title = 'Ijtimoiy Tarmoqlar Statistikalari'
line_chart.x_labels = [tarmoq1, tarmoq2, tarmoq3]
line_chart.add(tarmoq1, a)
line_chart.add(tarmoq2, b)
line_chart.add(tarmoq3, c)

# Diagramma brauzerda ko'rsatish
line_chart.render_in_browser()
