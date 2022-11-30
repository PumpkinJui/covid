# GitHub 仓库：https://github.com/PumpkinJui/covid
# 程序开发：PumpkinJui
# 数据录入：PumpkinJui
# 数据复核：PumpkinJui
# 数据来源：内蒙古自治区卫生健康委员会
# 数据网站：https://wjw.nmg.gov.cn/xwzx/xwfb/

from matplotlib import pyplot as plt
from matplotlib import font_manager as fma
from os.path import exists as ex
from time import strftime,localtime,time,strptime,mktime

def demo(day1, day2):#计算日期差
    time_array1 = strptime(day1, "%y%m%d")
    timestamp_day1 = int(mktime(time_array1))
    time_array2 = strptime(day2, "%y%m%d")
    timestamp_day2 = int(mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
    return result

date = [27,28,29,30]# 九月
for i in range(1,31+1):
    date.append(i)# 十月
for i in range(1,29+1):
    date.append(i)# 十一月
x = range(len(date))

con = [0,1,1,17,25,77,144,54,19,8,226,188,87,113,# 27~10
       28,28,35,23,5,6,9,8,9,11,# 11~20
       8,6,7,8,9,6,8,5,7,10,7,# 21~31
       20,188,238,72,39,55,156,129,101,91,# 1~10
       79,101,75,76,73,77,81,73,80,71,# 11~20
       58,105,55,71,94,66,66,53,68
       ]

conall = [0,1,2,19,44,121,265,319,338,346,572,723,794,885,
          862,820,781,712,599,335,270,253,250,254,
          258,259,260,263,265,263,263,260,261,264,266,
          279,437,647,694,712,729,850,947,1008,1065,
          1133,1221,1286,1232,1086,1076,1014,981,981,961,
          894,868,734,705,575,470,469,450,442
          ]

non = [0,0,0,6,5,21,225,239,441,651,371,376,499,574,
       374,144,89,53,23,23,22,24,34,45,
       44,48,46,49,53,59,64,62,71,85,144,
       283,730,514,469,618,958,1604,891,956,1063,
       1056,1177,1061,1096,1057,888,1111,1060,670,536,
       422,315,243,244,152,176,139,169,125
       ]

nonall = [0,0,0,6,11,29,248,453,880,1525,1765,2066,2538,3070,
          3431,3549,3570,3422,3336,2937,2222,1967,1895,1856,
          1861,1872,1878,1891,1903,1919,1943,1952,1973,1991,2088,
          2300,2938,3362,3762,4278,5118,6534,7249,8020,8903,
          9501,10157,10690,11309,11069,10232,9838,9755,9385,8615,
          7502,6431,4701,4159,662,722,824,824+169-697,824+169-697+125-1055
          ]

# print(len(con),len(conall),len(non),len(nonall))
# 调试代码，可以分别打印以上四个列表中的元素数量

'''
cont = 0
for i in con:
    cont += i
print(cont)
# 调试代码，可以打印累计确诊病例数
'''

'''
nont = 0
for i in non:
    nont += i
print(nont)
# 调试代码，可以打印累计无症状病例数
'''

plt.figure(figsize=(16,9),dpi=120)

plt.plot(x,con,marker='o',c='orange',label='确诊')
plt.plot(x,conall,marker='o',c='red',label='现有确诊')
plt.plot(x,non,marker='o',c='purple',label='无症状')
plt.plot(x,nonall,marker='o',c='blue',label='现有无症状')# 折线图

plt.legend(loc='best')# 显示标签
plt.grid(True,linestyle='--',alpha=0.5)# 显示网格

path = 'C:/WINDOWS/Fonts/LXGWBright-Regular.ttf'# 优先字体：LXGW Bright
if not ex(path):
    path = 'C:/WINDOWS/Fonts/msyh.ttc'# 字体不存在：使用微软雅黑
    plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
else:
    fma.fontManager.addfont(path)
    plt.rcParams['font.sans-serif'] = 'LXGW Bright'

title = '自 2022 年 09 月 27 日以来，呼和浩特市的本土新冠肺炎疫情病例数据'
plt.title(title,size=16)# 显示标题
plt.xticks(x,date)# 显示日期线
plt.xlabel('日期',size=14)
plt.ylabel('病例数',size=14)# 显示坐标轴标签

day = str(int(strftime("%y%m%d",localtime(time()-86400))))# 计算昨天几号
h = int(strftime("%H",localtime()))# 计算现在几点
plt.savefig(day + '_Single.png')# 保存图片

if demo('220926',day) != len(date) and h >= 9:# 内蒙古卫健委在九点更新前一天的数据
    txt = '当前数据已过期，最新为'+day[:-3:-1]+'，现为'+str(date[-1])
    plt.text(20,8000,txt,color='#88B04B')
elif demo('220926',day) != len(date):# 到了第二天但没到九点，暂无数据
    txt = '当前数据为 '+str(int(day)-1)+' 的最新数据'
    plt.text(20,8000,txt,color='green')
else:# 当天
    txt = '当前数据为 '+day+' 的最新数据'
    plt.text(20,8000,txt,color='green')

plt.get_current_fig_manager().window.state('zoomed')# 全屏显示
plt.show()# 显示窗口
