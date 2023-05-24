#导入数据集
import matplotlib.pyplot as plt    #绘图
from mpl_toolkits.mplot3d import Axes3D   #可视化
from sklearn import datasets    #sklearn中包含很多数据集，其中就有鸢尾花数据集
from sklearn.decomposition import PCA    #主成分分析
import numpy as np   #机器学习中通常将数据以数组的形式存储，特别是这里包含了特征数据和分类数据

iris = datasets.load_iris()   #利用load函数装载数据集

print('鸢尾花数据集的数据类型是：',type(iris))  
  
print('鸢尾花数据集的数据有：',dir(iris))
for i in dir(iris):
	eval('print(i,"/t",type(iris.'+i+'))')   #遍历数据集中的数据，查看每个数据的数据类型
print()    

print('鸢尾花数据集中feature_names取值：',iris.feature_names)
print('鸢尾花数据集中数据的行列数：',iris.data.shape)
print('鸢尾花数据集中target取值：',np.unique(iris.target))
print('鸢尾花数据集中target_names的取值：',iris.target_names)   

#实现可视化
a,b=0,1
X = iris.data[:,[a,b]]      #二维可视化，即只取两个属性，这里取的是全部行和前两列（sepal length和sepal width）
y = iris.target     #由上述程序结果可知取值为0,1,2，代表3种品种的鸢尾花

x_min,x_max = X[:,0].min()-.5, X[:,0].max()+.5   #x值的最小值和最大值分别是第一列最小值和最大值-5和+5
y_min,y_max = X[:,1].min()-.5, X[:,1].max()+.5   #y值的最小值和最大值分别是第二列最小值和最大值-5和+5

plt.figure(2,figsize=(8,6))
plt.clf

plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.Set1,edgecolor='w')  #绘制散点图，c即color，cmap是将y不同的值画出不同颜色，edgecolor为白色
plt.xlabel(iris.feature_names[a])   #x轴名称
plt.ylabel(iris.feature_names[b])   #y轴名称

plt.xlim(x_min,x_max)    #x轴的作图范围
plt.ylim(y_min,y_max)    #y轴的作图范围
plt.xticks(())     #x轴的刻度内容的范围
plt.yticks(())     #y轴的刻度内容的范围

plt.show()

fig = plt.figure(1,figsize=(8,6))
ax = Axes3D(fig,elev=-150,azim=110)   #？？？？？？？？？？？？？？？
X_reduced = iris.data[:,:3]   #可以改变列看图形分布X_reduced = iris.data[:,[0,2,3]]

ax.scatter(X_reduced[:, 0],X_reduced[:, 1],X_reduced[:, 2],c=y,cmap=plt.cm.Set1,edgecolor='w',s=40)
ax.set_title('Iris 3D')

ax.set_xlabel(iris.feature_names[0])
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel(iris.feature_names[1])
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel(iris.feature_names[2])
ax.w_zaxis.set_ticklabels([])

plt.show()

fig = plt.figure(1,figsize=(8,6))
ax = Axes3D(fig,elev=-150,azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)   
                    #n_components是PCA算法中所要保留的主成分个数n，也即保留下来的特征个数n,这里四维降三维n_components=3
                    #fit_transform 对数据先拟合 fit，找到数据的整体指标，如均值、方差、最大值最小值等，然后对数据集进行转换transform，从而实现数据的标准化、归一化操作

ax.scatter(X_reduced[:,0],X_reduced[:,1],X_reduced[:,2],c=y,cmap=plt.cm.Set1,edgecolor='w',s=40)
ax.set_title('First three PCA directions')

ax.set_xlabel('1st eigen vector')
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel('2nd eigen vector')
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel('3rd eigen vector')
ax.w_zaxis.set_ticklabels([])

plt.show()

a,b=0,1
X_reduced = PCA(n_components=2).fit_transform(iris.data)
X = X_reduced[:,[a,b]]      #二维可视化，即只取两个属性，这里取的是全部行和前两列（sepal length和sepal width）
y = iris.target     #由上述程序结果可知取值为0,1,2，代表3种品种的鸢尾花

x_min,x_max = X[:,0].min()-.5, X[:,0].max()+.5   #x值的最小值和最大值分别是第一列最小值和最大值-5和+5
y_min,y_max = X[:,1].min()-.5, X[:,1].max()+.5   #y值的最小值和最大值分别是第二列最小值和最大值-5和+5

plt.figure(2,figsize=(8,6))
plt.clf

plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.Set1,edgecolor='w')  #绘制散点图，c即color，cmap是将y不同的值画出不同颜色，edgecolor为白色
plt.xlabel(iris.feature_names[a])   #x轴名称
plt.ylabel(iris.feature_names[b])   #y轴名称

plt.xlim(x_min,x_max)    #x轴的作图范围
plt.ylim(y_min,y_max)    #y轴的作图范围
plt.xticks(())     #x轴的刻度内容的范围
plt.yticks(())     #y轴的刻度内容的范围
