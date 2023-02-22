import matplotlib.pyplot as plt
import gemNumFuncs_old as gnf
import getwordsfromdbs as gwdb

teddy=gnf.DistanceTeddyBear(gwdb.getDeepMem())
teddy.pointBias=0.001
teddy.distanceBias=1.0
teddy.commonNds=1.0
teddy.commonRoot=1.0
teddy.commonRoute=1.0
teddy.commonNumber=0.0
teddy.sameWord=0.0
teddy.ndsDistanceWeight=0.01
teddy.rootDistanceWeight=0.01
teddy.numberDistanceWeight=0.01
teddy.closenessWeight=1.0
teddy.maxDistance=10.0

print(str(teddy))

dataArray=teddy.getRestrictedWordSet_wdxy("tervesairas", "ScaExt")
print(dataArray)

uniqueNumbers=[]
x = []
y = []

for i in dataArray:
       if not i[1] in uniqueNumbers:
              uniqueNumbers+=[i[1]]
              x += [i[3]]
              y += [i[4]]
              

plt.scatter(x, y)

plt.show()

