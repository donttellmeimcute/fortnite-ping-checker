from ping3 import ping 
import statistics as st
means=[]
def Average(means):
    return sum(means) / len(means)
for i in range (200):
	pin=ping("qosping-aws-us-west-1.ol.epicgames.com")
	means.insert(i,pin)
	xd=pin*1000
	print(xd,'ms')
mean=Average(means)
mean =mean * 1000
print('El promedio de ping al servidor de west de fortnite es: ' )
mean = round(mean,1)
print(mean, 'ms')