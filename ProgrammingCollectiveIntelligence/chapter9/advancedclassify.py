import os
class matchrow:
    def __init__(self, row, allnum=False):
        if allnum:
            self.data = [float(row[i]) for i in range(len(row)-1)]
        else:
            self.data = row[:len(row)-1]
        self.match = int(row[len(row)-1])
    
def loadmatch(f, allnum=False):
    rows = []
    with open(f) as fi:
        for line in fi:
            rows.append(matchrow(line.strip().split(','), allnum))
    return rows
'''
import os
with open(os.path.join(os.path.dirname(__file__), 'agesonly.csv')) as f:
    for line in f:
        print(line)
'''
def dotproduct(v1, v2):
    return sum([v1[i]*v2[i] for i in range(len(v1))])

def dpclassify(point, avgs):
    b = (dotproduct(avgs[1], avgs[1]) - dotproduct(avgs[0], avgs[0])) / 2
    y = dotproduct(point, avgs[0]) - dotproduct(point, avgs[1]) + b
    if y > 0:
        return 0
    return 1

def yesno(v):
    if v == 'yes':
        return 1
    elif v == 'no':
        return -1
    else:
        return 0

def matchcount(interest1, interest2):
    i1 = interest1.split(':')
    i2 = interest2.split(':')
    x = 0
    for i in i1:
        if i in i2:
            x += 1
    return x

def milesdistance(a1, a2):
    return 0

def loadnumerical():
    oldrows = loadmatch(os.path.join(os.path.dirname(__file__), 'matchmaker.csv'))
    newrows = []
    for row in oldrows:
        d = row.data
        data = [float(d[0]), yesno(d[1]), yesno(d[2]), 
                float(d[5]), yesno(d[6]), yesno(d[7]), 
                matchcount(d[3], d[8]), milesdistance(d[4], d[9]), row.match]
        newrows.append(matchrow(data))
    return newrows
'''
numericalset = loadnumerical()
print(numericalset[0].data)
'''
def scaledata(rows):
    low = [99999999.0]*len(rows[0].data)
    high = [-99999999.0]*len(rows[0].data)
    for row in rows:
        d = row.data
        for i in range(len(d)):
            if low[i] > d[i]:
                low[i] = d[i]
            if high[i] < d[i]:
                high[i] = d[i]
    
    def scaleinput(d):
        r = []
        for i in range(len(low)):
            if (high[i]-low[i]) != 0:
                r.append((d[i]-low[i]) / (high[i]-low[i]))
            else:
                r.append(0)
        return r

    newrows = [matchrow(scaleinput(row.data)+[row.match]) for row in rows]
    return newrows
nr = scaledata(loadnumerical())
print(nr[0].data)

def rbf(v1,v2,gamma=10):
    dv=[v1[i]-v2[i] for i in range(len(v1))]
    l=veclength(dv)
    return math.e**(-gamma*l)

def nlclassify(point,rows,offset,gamma=10):
    sum0=0.0
    sum1=0.0
    count0=0
    count1=0
    
    for row in rows:
        if row.match==0:
        sum0+=rbf(point,row.data,gamma)
        count0+=1
        else:
        sum1+=rbf(point,row.data,gamma)
        count1+=1
    y=(1.0/count0)*sum0-(1.0/count1)*sum1+offset

    if y>0: return 0
    else: return 1

def getoffset(rows,gamma=10):
    l0=[]
    l1=[]
    for row in rows:
        if row.match==0: l0.append(row.data)
        else: l1.append(row.data)
    sum0=sum(sum([rbf(v1,v2,gamma) for v1 in l0]) for v2 in l0)
    sum1=sum(sum([rbf(v1,v2,gamma) for v1 in l1]) for v2 in l1)
    
    return (1.0/(len(l1)**2))*sum1-(1.0/(len(l0)**2))*sum0