import serial
import csv 
import time

dev_path = '/dev/ttyACM0'
baudrate = 9600
arduino = serial.Serial(dev_path,baudrate)
now = time.gmtime(time.time())
csv_file = open('/home/mi/smart_farm/{}_{}_{}'.format(now.tm_year,now.tm_mon,now.tm_mday),'w')
csv_writer = csv.writer(csv_file, delimiter=",")
cnt = 0

while(cnt < 10):
	cnt += 1
	try:
		y = arduino.readline()
		pt = y.decode()[:-2]
		print(pt)
		csv_writer.writerow([pt])
	except serial.serialutil.SerialException:
		print("no Data")
		
csv_file.close()
	