from matplotlib import pyplot as plt
ls=[]
with open('co2-mm-mlo.csv','r') as fo:
    for line in fo:
        line=line.replace('\n','')
        ls.append(line.split(','))
x=[]
y1=[]
y2=[]
for i in range(1,len(ls)):
    x.append(ls[i][0])
    y1.append(float(ls[i][3]))
    y2.append(float(ls[i][4]))
plt.plot(x,y1)
plt.plot(x,y2)
plt.xticks([i for i in range(0,len(x),118)])
plt.yticks([j for j in range(0,len(y1),118)])
plt.yticks([j for j in range(0,len(y2),118)])
plt.ylim(300,420)
plt.show()