import matplotlib.pyplot as plt	#导入库
import numpy as np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)	#x从0开始到3π样本数为100
y = np.sin(x)			#y为以x为横轴的正弦信号的纵轴数据

plt.rcParams['font.sans-serif']=['SimHei']	#加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False	#用来正常显示负号
plt.subplot(1,2,1)			#图像显示在1行2列第1个
plt.plot(x,y)			#以x为横轴，y为纵轴显示图像

x1 = [t*0.375*np.pi for t in x]		#x1从0开始到1.125π²样本数为100
y1 = np.sin(x1)			#y1为以x为横轴的正弦信号的纵轴数据
plt.subplot(1,2,2)			#图像显示在1行2列第2个
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$')#显示标题 \omega为ω  \frac{3}{8}为3/8 \pi为π
plt.plot(x, y1)			#以x为横轴，y1为纵轴显示图像
plt.show()				#显示