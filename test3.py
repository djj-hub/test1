import json
from matplotlib import pyplot as plt
with open('co2-mm-gl.json') as fo:
    ls=json.load(fo)
x=[]
y1=[]
y2=[]
for i in range(1,len(ls)):
    x.append(ls[i]['Date'])
    y1.append(float(ls[i]['Average']))
    y2.append(float(ls[i]['Trend']))
plt.plot(x,y1)
plt.plot(x,y2)
plt.xticks([i for i in range(0,len(x),118)])
plt.yticks([j for j in range(0,len(y1),118)])
plt.yticks([j for j in range(0,len(y2),118)])
plt.ylim(330,420)
plt.show()