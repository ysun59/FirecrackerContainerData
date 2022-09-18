#For cat /proc/interrupts, use "interrupts.txt" to generate "interrupts_deltaData.txt"
# to generate "interrupts_fig.png"
# RES:........Rescheduling interrupts

import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
# from scipy import interpolate


#取每个core的“RES:........Rescheduling interrupts”那一行的数据：
#core0，core1，core2，...core31的"RES:........Rescheduling interrupts"一行数据 <第一秒数据>
#core0，core1，core2，...core31的"RES:........Rescheduling interrupts"一行数据  <第二秒数据>
#.....
#core0，core1，core2，...core31的"RES:........Rescheduling interrupts"一行数据  <第60秒数据>
#go into folder by itself
folders = os.listdir('.')
def interruptsTxt():
  for folder in folders:
    cpu_perf_path = os.path.join('.', folder, 'interrupts.txt')
    if os.path.exists(cpu_perf_path):
      outputs = []

      with open(cpu_perf_path, 'r') as file:
        lines = file.readlines()

        # lineBuf = []
        for line in lines:

          a=line.split() #返回分割后的字符串列表list

          if a[0:1]==['RES:']:
            outputs.append(','.join(a[1:33]))


      mpstat_csv_path = os.path.join('.', folder, 'interrupts_data.txt')
      with open(mpstat_csv_path, 'wt') as file:
        file.write('\n'.join(outputs))

interruptsTxt() #取每个核的nr_switches



#calculate delta, eg: delta of core 0's "RES:........Rescheduling interrupts"一行数据 at No_1s - No_0s
#core0，core1，core2，...core31的"RES:........Rescheduling interrupts"一行数据 <第二秒数据 - 第一秒数据>
#core0，core1，core2，...core31的"RES:........Rescheduling interrupts"一行数据 <第三秒数据 - 第二秒数据>
#.....
#core0，core1，core2，...core31的"RES:........Rescheduling interrupts"一行数据 <第60秒数据 - 第59秒数据>
def interruptsDelta():
  for folder in folders:
    mpstat_csv_path = os.path.join('.', folder, 'interrupts_data.txt')
    if os.path.exists(mpstat_csv_path):
      outputs = []

      with open(mpstat_csv_path, 'r') as file:
        lines = file.readlines()

        matrix = []
        for line in lines:
          items =[int(item) for item in line.split(',')]
          matrix.append(items) #txt文件读到二维数组里面
          # print(matrix)

        lineBuf = []
        # print(matrix[0][1])
        rowNum = len(matrix) #行数
        # print(rowNum)
        colNum = len(matrix[0]) #列数
        # print(colNum)
        for i in range(0,rowNum - 1):
          for j in range(0,colNum):
            lineBuf.append(matrix[i+1][j] - matrix[i][j])
            if j==colNum-1:
              outputs.append(lineBuf)
              lineBuf = []
        # print(outputs)
        mpstat_csv_path = os.path.join('.', folder, 'interrupts_deltaData.txt')
        np.savetxt(mpstat_csv_path,outputs,fmt='%d',delimiter=',') #fmt='%.04f'为保留四位小数

interruptsDelta()
        






# #draw pictures
def schedstatNoColPng():
  for folder in folders:
    mpstat_csv_path = os.path.join('.', folder, 'interrupts_deltaData.txt')

    if os.path.exists(mpstat_csv_path):
      plt.style.use('ggplot') #图的风格bmh、ggplot、dark_background、fivethirtyeight和grayscale。

      data = pd.read_table(mpstat_csv_path,sep=',',encoding='utf_8_sig',engine='python',header=None) #pd.read_table返回一个数据结构
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
      for i in range(0,colNum): #32个core
      # for i in range(0,4): #32个core
        plt.plot(x, data[i], '-', marker='o',label='cpu{}'.format(i)) #s-:方形,o-:圆形
      plt.xlabel('time(s)') #横坐标名
      plt.xticks(rotation=45)
      plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d')) #gca就是get current axes的意思
      plt.ylabel('num') #纵坐标名
      plt.title('{}_interrupts'.format(folder))
      plt.legend(loc='lower left', bbox_to_anchor=(1.01,0),ncol=2) #图例 (loc='best')自动选择放在合适位置，loc指的是我们的legend的左下角的那个顶点的坐标
      plt.grid(True) #设置网格模式
      sch_fig_path = os.path.join('.', folder, 'interrupts_fig.png')
      # print(sch_fig_path)

      fig=plt.figure(1) #解决1
      fig.savefig(sch_fig_path, bbox_inches='tight') #解决1

      # plt.savefig(sch_fig_path) #普通存图片方法
      # plt.show()

      # plt.cla() #清空坐标轴
      # plt.clf()
      # plt.close()

      # plt.xticks(ticks=[i for i in range(3)], labels=[i for i in range(3)])
      # plt.xticks(ticks=[2, 10, 20, 30], labels=[10, 20, 30, 40])
      # plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.0fcpu'))

schedstatNoColPng() #取第N列数据的txt生成png，N从0开始