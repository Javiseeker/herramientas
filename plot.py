import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *
data=[]
port=serial.Serial('/dev/ttyACM0',9600)
plt.ion()
cnt=0
def draw_plot():
	plt.ylim(0,256)
	plt.title('sensor')
	plt.grid(True)
	plt.ylabel('Que miden')
	plt.plot(data,'ro-',label='data')
	plt.legend(loc='upper right')
while(True):
	while(port.inWaiting==0):
		pass
	datastr=port.readline()
	dataf=float(datastr)
	data.append(dataf)
	drawnow(draw_plot)
	cnt=cnt+1
	if (cnt>50):
		data.pop(0)
		cnt=cnt-1
