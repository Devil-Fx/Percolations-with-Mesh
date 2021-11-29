import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors
import matplotlib as mpl
from scipy.ndimage import measurements
import random
from pylab import arange

def mnkGP(x,y): # функция которую можно использзовать в програме
              n=len(x) # количество элементов в списках
              s=sum(y) # сумма значений y
              s1 = sum(1 / value for value in x) #  сумма 1/x
              s2 = sum(1 / value ** 2 for value in x) #  сумма (1/x)**2
              s3=sum([y[i]/x[i]  for i in range(0,n)])  # сумма y/x                   
              a= round((s*s2-s1*s3)/(n*s2-s1**2),3) # коэфициент а с тремя дробными цифрами
              b=round((n*s3-s1*s)/(n*s2-s1**2),3)# коэфициент b с тремя дробными цифрами
              s4=[a+b/x[i] for i in range(0,n)] # список значений гиперболической функции              
              so=round(sum([abs(y[i] -s4[i]) for i in range(0,n)])/(n*sum(y))*100,3)   # средняя ошибка аппроксимации
              plt.title('Аппроксимация гиперболой y='+str(a)+'+'+str(b)+'/x\n Средняя ошибка--'+str(so)+'%',size=14)
              plt.xlabel('Количество дней с начала.', size=12)
              plt.ylabel('Плотность кластера ρ.', size=14)
              plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Data(x,y)')
              plt.plot(x, s4, color='g', linewidth=2, label='Data(x,f(x)=a+b/x')
              plt.legend(loc='best')
              plt.grid(True)
              plt.show()

L = 100
N = 3000
iter = 1
work = 0

for k in range(iter):
    arr = np.zeros((L,L), dtype="bool_")
    arr[:] = True
    for j in range(N):
        if random.random() <= 1:
            x1 = random.randint(0, L-1)
            y1 = random.randint(0, L-1)
            arr[x1,y1] = False
    lw,num = measurements.label(arr)
    area = measurements.sum(arr, lw)
    #area = measurements.sum(arr, lw, index=arange(lw.max() + 1))
    #Mc = np.amax(area)
    if num == 1:
        work += 1
    #print(area)



#print(lw)
#print(num)
#print(work)
#print(work/30)

#mpl.rcParams['font.family'] = 'fantasy'
x = [1000,1500,2000,2500,3000]
y = [0.9044,0.8602,0.8188,0.7788,0.7395]
#mnkGP(x,y)


plt.plot(x,y)
plt.xlabel('Количество дней с начала.')
plt.ylabel('Плотность кластера ρ')
plt.show()
#cmap = matplotlib.colors.ListedColormap(['white','black'])
#img = plt.imshow(arr,interpolation='nearest',cmap = cmap)
#plt.colorbar(img,cmap=cmap,ticks=[0,1])
#plt.grid(True,color='black', which='minor')
#plt.show()

