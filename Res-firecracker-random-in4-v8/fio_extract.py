#For CPU, use "cpu_perf.txt" to generate "mpstat_data.csv"
#(1-idle%) of all, core 0, core 1, core 2, core 3.....core 31

import os
import re
from decimal import *
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


mpstat_regex = re.compile(r'(all|\d{1,2})\s+?((?:\d|\.)+)\s+?(?:(?:\d|\.)+)\s+?((?:\d|\.)+)\s+?((?:\d|\.)+).*?\s((?:\d|\.)+)$')

#go into folder by itself
folders = os.listdir('.')

for folder in folders:
  # mpstat
  cpu_perf_path = os.path.join('.', folder, 'cpu_perf.txt')
  if os.path.exists(cpu_perf_path):
    outputs = []

    with open(cpu_perf_path, 'r') as file:
      lines = file.readlines()

      lineBuf = []
      for line in lines:
        m = mpstat_regex.search(line)
        if m:
          groups = m.groups()
          # print("groups[0] is "+str(groups[0]))
          # print("lineBuf is")
          # print(lineBuf)

          if str(groups[0]) == 'all' and len(lineBuf) != 0:
            outputs.append(','.join(lineBuf))
            lineBuf = []
          
          lineBuf.append(str(100 - float(groups[4])))

    mpstat_csv_path = os.path.join('.', folder, 'mpstat_data.csv')
    with open(mpstat_csv_path, 'wt') as file:
      file.write('\n'.join(outputs))

# #draw pictures cpu utilization during time
def mpstatDataPng():
  for folder in folders:
    mpstat_csv_path = os.path.join('.', folder, 'mpstat_data.csv')

    if os.path.exists(mpstat_csv_path):
      plt.style.use('ggplot') #图的风格bmh、ggplot、dark_background、fivethirtyeight和grayscale。

      data = pd.read_table(mpstat_csv_path,sep=',',encoding='utf_8_sig',engine='python',header=None) #pd.read_table返回一个数据结构,DataFrame
      # T=data.T #行列转换
      # print("第一行")
      # print(data.iloc[0])  #打印第一行
      rowZero=data.iloc[0] #打印第一行
      colNum = len(rowZero) #第一行有几个数字

      # date=data.values
      # date=data[0]
      # print(date)
      plt.cla() #清空坐标轴
      x = range(0,len(data)) #60个数字60s
      for i in range(0,colNum-1): #32个core，这个是非典型画图，跳过了第一列，第一列是all
      # for i in range(0,4): #32个core
        plt.plot(x, data[i+1], '-', marker='o',label='cpu{}'.format(i)) #s-:方形,o-:圆形
      plt.plot(x, data[0], '-', marker='o',label='avg cpu') #s-:方形,o-:圆形,把跳过的第一列的线画在最后
      plt.xlabel('time(s)') #横坐标名
      plt.xticks(rotation=45)
      plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d')) #gca就是get current axes的意思
      plt.ylabel('Cpu Utilization %') #纵坐标名
      plt.title('{}_cpu_overtime'.format(folder))
      plt.legend(loc='lower left', bbox_to_anchor=(1.01,0),ncol=2) #图例 (loc='best')自动选择放在合适位置，loc指的是我们的legend的左下角的那个顶点的坐标
      plt.grid(True) #设置网格模式
      sch_fig_path = os.path.join('.', folder, 'mpstat_data_overtime.png')
      # print(sch_fig_path)

      fig=plt.figure(1) #解决1
      fig.savefig(sch_fig_path, bbox_inches='tight') #解决1

mpstatDataPng() #


#print avg cpu utlization of all cores during 60s
def printAvgCpu():
  for folder in folders:
    mpstat_csv_path = os.path.join('.', folder, 'mpstat_data.csv')
    
    if os.path.exists(mpstat_csv_path):
      print("folder is")
      print(folder)
      outputs = [] ##
      with open(mpstat_csv_path, 'r') as file:
        lines = file.readlines()

        summ = 0
        lenn = 0
        matrix = []
        for line in lines:
          items =[float(item) for item in line.split(',')]
          matrix.append(items) #txt文件读到二维数组里面
          lenn = lenn + 1
        # print(matrix)

        # rowNum = int(len(matrix)) #行数
        # colNum = len(matrix[0]) #列数
        # for i in range(0,rowNum):
        for i in range(0,lenn):
          summ = summ + matrix[i][0]
        avg = summ/lenn
        print("avg cpu utilizations is:")
        print(avg)
        print("")

printAvgCpu()


#第一张图
#只看all的数据
#all随时间变化，横坐标60个柱状图
#第一秒all的 usr%,   第二秒all的 usr%,   第三秒all的 usr% .....,   第60秒all的 usr%
#第一秒all的 sys%,   第二秒all的 sys%,   第三秒all的 sys% .....,   第60秒all的 sys%
#第一秒all的 soft%,  第二秒all的 soft%,  第三秒all的 soft% .....,  第60秒all的 soft%
#第一秒all的 guest%, 第二秒all的 guest%, 第三秒all的 guest% ....., 第60秒all的 guest%
#第一秒all的 other%, 第二秒all的 other%, 第三秒all的 other% ....., 第60秒all的 other%
#Other就是=1-idle%-uer%-sys%-soft%-guest%
#go into folder by itself
folders = os.listdir('.')
def mpstatAllTxt():
  for folder in folders:
    cpu_perf_path = os.path.join('.', folder, 'cpu_perf.txt')
    if os.path.exists(cpu_perf_path):
      outputs = []

      with open(cpu_perf_path, 'r') as file:
        lines = file.readlines()

        lineBuf = []
        for line in lines:

          a=line.split() #返回分割后的字符串列表list

          if 'all' not in line: #或者写成 if a[1:2] == ['all']:然后后面的要缩进
            continue

          for idx in [2, 4, 7, 9]:
            lineBuf.append(a[idx])      #不用重复写lineBuf.append(','.join(a[2:3]))
           
          other=Decimal(100)-Decimal(a[11])-Decimal(a[2])-Decimal(a[4])-Decimal(a[7])-Decimal(a[9])
          # #如果觉得other=-0.01画图很奇怪，就加上下面两行
          # if str(other) == '-0.01': #或者写成if other < 0:
          #   other=0.00

          lineBuf.append(str(other))  #用Decimal的话，这一行就不会变成科学计数法.或者other='%.2f'%(other)

          outputs.append(','.join(lineBuf))
          lineBuf =[]

      mpstat_csv_path = os.path.join('.', folder, 'mpstat_all.txt')
      with open(mpstat_csv_path, 'wt') as file:
        file.write('\n'.join(outputs))

      # 下面几行把文件'mpstat_all.txt'里面内容行列转换
      data = pd.read_table(mpstat_csv_path,sep=',',encoding='utf_8_sig',engine='python',header=None) #pd.read_table返回一个数据结构DataFrame
      T=data.T #行列转换
      # print(T)
      T.to_csv(mpstat_csv_path,sep=',',index=False,header=None)

mpstatAllTxt() 

# #draw pictures，画第一张图的堆叠柱状图
def mpstatAllPng():
  for folder in folders:
    mpstat_csv_path = os.path.join('.', folder, 'mpstat_all.txt')
    # print("path")
    # print(mpstat_csv_path)
    if os.path.exists(mpstat_csv_path):
      outputs=[]
      plt.style.use('ggplot') #图的风格bmh、ggplot、dark_background、fivethirtyeight和grayscale。

      with open(mpstat_csv_path, 'r') as file:
        lines = file.readlines() #输出是string类型
        for line in lines:
          pieces=line.split(',')
          outputs.append(list(map(lambda n: float(n), pieces)))
        # print(outputs)
      rowNum = len(outputs) #有几行
      # print(rowNum)
      colNum = len(outputs[0]) #有几列
      # print(colNum)
      line0=outputs[0]
      # print(line0)

      plt.cla() #清空坐标轴
      plt.title('mpstat Cpu utilization-all')

      ind = np.arange(colNum)  #[ 0  1  2  3....60]
      # plt.xticks(ind, ('G1', 'G2', 'G3', 'G4'))
      # my_y_ticks = np.arange(0,20,2)
      # plt.yticks(my_y_ticks)
      # my_x_ticks = np.arange(0,60,10)
      # plt.xticks(my_x_ticks)
      plt.ylim((0,70)) #坐标轴范围

      plt.ylabel('Cpu utilization %')
      plt.xlabel('time(s)') #横坐标名

      Bottom = outputs[4] #other
      Center3 = outputs[3] #guest
      Center2 = outputs[2] #soft
      Center1 = outputs[1] #sys
      Top = outputs[0] #usr

      bottom1 = []
      bottom2 = []
      bottom3 = []
      for i in range(0, len(Bottom)):
        sum1 = Bottom[i] + Center3[i]
        sum2 = Bottom[i] + Center3[i] + Center2[i]
        sum3 = Bottom[i] + Center3[i] + Center2[i] + Center1[i]
        bottom1.append(sum1)
        bottom2.append(sum2)
        bottom3.append(sum3)

      width = 0.8  # 设置条形图一个长条的宽度
      p1 = plt.bar(ind, Bottom, width, color='orangered') 
      p2 = plt.bar(ind, Center3, width, bottom=Bottom,color='limegreen') 
      p3 = plt.bar(ind, Center2, width, bottom=bottom1,color='darkorange')
      p4 = plt.bar(ind, Center1, width, bottom=bottom2,color='skyblue') 
      p5 = plt.bar(ind, Top, width, bottom=bottom3,color='lightcoral')

      plt.legend((p5[0], p4[0], p3[0], p2[0], p1[0]), ('usr', 'sys', 'soft', 'guest', 'other'),loc='lower left', bbox_to_anchor=(1.01,0))
      # plt.show()
      mpstat_fig_path = os.path.join('.', folder, 'mpstat_all.png')
      # print(sch_fig_path)

      fig=plt.figure(1) #解决1
      fig.savefig(mpstat_fig_path, bbox_inches='tight') #解决1

mpstatAllPng()





#第二张图
#Core 0的60秒平均 usr%, Core 1的60秒平均 usr%， Core 2的60秒平均 usr% ...., Core 31的60秒平均 usr%
#Core 0的60秒平均 sys%, Core 1的60秒平均 sys%， Core 2的60秒平均 sys% ...., Core 31的60秒平均 sys%
#Core 0的60秒平均 soft%, Core 1的60秒平均 soft%， Core 2的60秒平均 soft% ...., Core 31的60秒平均 soft%
#Core 0的60秒平均 guest%, Core 1的60秒平均 guest%， Core 2的60秒平均 guest% ...., Core 31的60秒平均 guest%
#Core 0的60秒平均 other%, Core 1的60秒平均 other%， Core 2的60秒平均 other% ...., Core 31的60秒平均 other%
#Other就是=1-idle%-uer%-sys%-soft%-guest%
#横坐标cpu 0 - 31, 纵坐标60s的平均值

#输入line, 返回让lineBuf=[usr%, sys%, soft%, guest%, other%]
def getUsrSysSoftGuestOther(line):
  lineBuf=[]
  a=line.split() #返回分割后的字符串列表list
  for idx in [2, 4, 7, 9]:
    lineBuf.append(a[idx])       #不用重复写lineBuf.append(','.join(a[2:3]))
  
  other=Decimal(100)-Decimal(a[11])-Decimal(a[2])-Decimal(a[4])-Decimal(a[7])-Decimal(a[9])
  #如果觉得other=-0.01画图很奇怪，就加上下面两行
  # if str(other) == '-0.01': #或者写成if other < 0:
  #   other=0.00

  lineBuf.append(str(other))  #用Decimal的话，这一行就不会变成科学计数法.或者other='%.2f'%(other)
  return lineBuf

#输入两个列表list,list里是字符串，返回list字符串对应数字求和
def listSum(lineBuf1,lineBuf2):
  # lineBuf3=np.sum([lineBuf1,lineBuf2],axis=0) #axis参数表示纵向求和,这是[1,2,3]这种list里直接是数字的相加
  # 而这里因为list是字符串，所以用下面的方法
  lineBuf1=np.array(lineBuf1).astype(float)
  lineBuf2=np.array(lineBuf2).astype(float)
  return (lineBuf1+lineBuf2).tolist()

def mpstatUsrSysSoftGuestOtherTxt():
  for folder in folders:
    cpu_perf_path = os.path.join('.', folder, 'cpu_perf.txt')
    if os.path.exists(cpu_perf_path):
      outputs = []

      with open(cpu_perf_path, 'r') as file:
        lines = file.readlines()

        # for core in range(32):
        for core in range(32):
          lineBuf=['0','0','0','0','0']
          lenn=0
          for line in lines:
            a=line.split()
            if a[1:2] == ['CPU'] or a[1:2] == [] or a[1:2] == ['all'] or a[1:2] == ['5.4.0-124-generic']:
              continue
            if a[1] == str(core):
              lenn=lenn+1
              lineBufCore=getUsrSysSoftGuestOther(line) #得到这个line的[usr%, sys%, soft%, guest%, other%]
              lineBuf=listSum(lineBufCore,lineBuf)
              # print(lineBuf)
           
          lineBuf = [x/lenn for x in lineBuf] #求个平均
          outputs.append(lineBuf)

          lineBuf =[]
          lenn=0
        # print(outputs)

      mpstat_csv_path = os.path.join('.', folder, 'mpstat_UsrSysEtc.txt')
      np.savetxt(mpstat_csv_path,outputs,fmt='%.02f',delimiter=',')

      # 下面几行把文件'mpstat_all.txt'里面内容行列转换
      data = pd.read_table(mpstat_csv_path,sep=',',encoding='utf_8_sig',engine='python',header=None) #pd.read_table返回一个数据结构DataFrame
      T=data.T #行列转换
      # print(T)
      T.to_csv(mpstat_csv_path,sep=',',index=False,header=None)

mpstatUsrSysSoftGuestOtherTxt()


#draw pictures，画第二张图的堆叠柱状图
def mpstatUsrSysSoftGuestOtherPng():
  for folder in folders:
    mpstat_csv_path = os.path.join('.', folder, 'mpstat_UsrSysEtc.txt')
    if os.path.exists(mpstat_csv_path):
      outputs=[]
      plt.style.use('ggplot') #图的风格bmh、ggplot、dark_background、fivethirtyeight和grayscale。

      with open(mpstat_csv_path, 'r') as file:
        lines = file.readlines() #输出是string类型
        for line in lines:
          pieces=line.split(',')
          outputs.append(list(map(lambda n: float(n), pieces)))
        # print(outputs)
      rowNum = len(outputs) #有几行
      # print(rowNum)
      colNum = len(outputs[0]) #有几列
      # print(colNum)
      line0=outputs[0]
      # print(line0)

      plt.cla() #清空坐标轴
      plt.title('mpstat-UsrSysEtc of 32 cores')

      ind = np.arange(colNum)  #[ 0  1  2  3...31]
      plt.xticks(ind, ('Core0', '1', '2', '3', '4', 'Core5', '6', '7', '8', '9', 'Core10', '11', '12', '13', '14', 'Core15', '16', '17', '18', '19', 'Core20', '21', '22', '23', '24', 'Core25', '26', '27', '28', '29', 'Core30', '31'), rotation='vertical')
      # plt.xticks(ind, ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'), rotation='vertical')

      plt.ylabel('Avg cpu utilization of 60s (%)')
      plt.xlabel('Cores') #横坐标名
      # plt.xticks(rotation=45)
      plt.ylim((0,100)) #坐标轴范围

      Bottom = outputs[4] #other
      Center3 = outputs[3] #guest
      Center2 = outputs[2] #soft
      Center1 = outputs[1] #sys
      Top = outputs[0] #usr

      bottom1 = []
      bottom2 = []
      bottom3 = []
      for i in range(0, len(Bottom)):
        sum1 = Bottom[i] + Center3[i]
        sum2 = Bottom[i] + Center3[i] + Center2[i]
        sum3 = Bottom[i] + Center3[i] + Center2[i] + Center1[i]
        bottom1.append(sum1)
        bottom2.append(sum2)
        bottom3.append(sum3)

      width = 0.7  # 设置条形图一个长条的宽度
      p1 = plt.bar(ind, Bottom, width, color='orangered') 
      p2 = plt.bar(ind, Center3, width, bottom=Bottom,color='limegreen') 
      p3 = plt.bar(ind, Center2, width, bottom=bottom1,color='darkorange')
      p4 = plt.bar(ind, Center1, width, bottom=bottom2,color='skyblue') 
      p5 = plt.bar(ind, Top, width, bottom=bottom3,color='lightcoral')

      plt.legend((p5[0], p4[0], p3[0], p2[0], p1[0]), ('usr', 'sys', 'soft', 'guest', 'other'),loc='lower left', bbox_to_anchor=(1.01,0))
      # plt.show()
      mpstat_fig_path = os.path.join('.', folder, 'mpstat_UsrSysEtc.png')
      # print(sch_fig_path)

      fig=plt.figure(1) #解决1
      fig.savefig(mpstat_fig_path, bbox_inches='tight') #解决1

mpstatUsrSysSoftGuestOtherPng()